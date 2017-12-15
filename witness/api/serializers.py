from rest_framework import serializers

from ..models import Witness


from ..models import User
from django.contrib.auth import get_user_model
from django.db.models import Q


# class WitnessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Witness
#         fields = ['account', 'reports']User_ = get_user_model()

User_ = get_user_model()


class WitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'gender', 'phone_number', 'image']


class WitnessCreateSerializer(serializers.ModelSerializer):
    email_confirm = serializers.EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'email_confirm', 'password', 'first_name', 'last_name', 'phone_number', 'gender']

    def create(self, validated_data):
        user = User_(username=validated_data['username'], email=validated_data['email'],
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


class WitnessLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    auth_field = serializers.CharField(label="Username or Email")
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
        username_or_email = data.get('auth_field', None)

        if not username_or_email:
            raise serializers.ValidationError('Enter valid Username or Email')

        if str(username_or_email).find('@') != -1:
            user = User_.objects.filter(Q(email=username_or_email)).distinct()
        else:
            user = User_.objects.filter(Q(username=username_or_email)).distinct()

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
