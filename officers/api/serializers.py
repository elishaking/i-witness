from rest_framework import serializers

from ..models import Officer

from django.contrib.auth import get_user_model
from django.db.models import Q

from ..models import User

# class OfficerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Officer
#         fields = ['account', 'id', 'activity']


User_ = get_user_model()


class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'id', 'gender', 'phone_number', 'image', 'activity']


class OfficerCreateSerializer(serializers.ModelSerializer):
    email_confirm = serializers.EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = ['id', 'email', 'email_confirm', 'password', 'first_name', 'last_name', 'phone_number', 'gender']

    def create(self, validated_data):
        user = User_(id=validated_data['id'], email=validated_data['email'],
                     first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                     phone_number=validated_data['phone_number'], gender=validated_data['gender'])

        user.set_password(validated_data['password'])
        user.save()
        return validated_data

    # General Validation
    # def validate(self, data):
    #     email = data['email']
    #     user_qs = User_.objects.filter(email=email)
    #     if user_qs.exists():
    #         raise serializers.ValidationError("This User is already registered")
    #
    #     return data

    def validated_email(self, value):
        email = value
        user_qs = User_.objects.filter(email=email)
        if user_qs.exists():
            raise serializers.ValidationError("This User is already registered")

        return value

    def validate_email_confirm(self, value):
        data = self.get_initial()
        email = data.get('email')
        email_confirm = value

        if email != email_confirm:
            raise serializers.ValidationError('Emails must match')

        return value


class OfficerLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    auth_field = serializers.CharField(label="Id or Email")
    # email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['auth_field', 'password', 'token']

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, data):
        id_or_email = data.get('auth_field', None)

        if not id_or_email:
            raise serializers.ValidationError('Enter valid Username or Email')

        if str(id_or_email).find('@') != -1:
            user = User_.objects.filter(Q(email=id_or_email)).distinct()
        else:
            user = User_.objects.filter(Q(id=id_or_email)).distinct()

        # print(user)

        if user.exists() and user.count() == 1:
            user_obj = user[0]
        else:
            raise serializers.ValidationError('Incorrect Credentials, please try again')

        if user_obj:
            if not user_obj.check_password(raw_password=data['password']):
                raise serializers.ValidationError("Incorrect Credentials, please try again")

        return data


""""""
