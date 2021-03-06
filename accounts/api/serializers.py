from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from django.db.models import Q

from ..models import User

User_ = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'gender', 'phone_number',
                  'image', 'witness', 'officer']


class AccountEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'image']


class AccountCreateSerializer(serializers.ModelSerializer):
    # email_confirm = serializers.EmailField(label='Confirm Email')
    class Meta:
        model = User
        # fields = ['username', 'email', 'email_confirm', 'password', 'first_name', 'last_name', 'phone_number',
        # 'gender']
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'gender', 'image']

    def create(self, validated_data):
        # FIXME: THIS METHOD IS NOT CALLED
        # media_data = validated_data.pop('image')
        # media = Media.objects.create(**media_data)
        # print(media)

        user = User_(username=validated_data['username'], email=validated_data['email'],
                     first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                     phone_number=validated_data['phone_number'], gender=validated_data['gender'])

        user.set_password(validated_data['password'])
        user.save()

        return user

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

    # def validate_email_confirm(self, value):
    #     data = self.get_initial()
    #     print('data: ', data)
    #     email = '' # data.get('email')
    #     email_confirm = value
    #     print('email1: ' + email, 'email2: ' + email_confirm)
    #
    #     if email != email_confirm:
    #         raise serializers.ValidationError('Emails must match')
    #
    #     return value


class AccountLoginSerializer(serializers.ModelSerializer):
    owner_id = serializers.IntegerField(allow_null=True, read_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)
    auth_field = serializers.CharField(label="Username or Email", write_only=True)

    # email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['owner_id', 'auth_field', 'password', 'token']

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
            if not user[0].password == data['password']:  # user_obj.check_password(raw_password=data['password']):
                raise serializers.ValidationError("Incorrect Credentials, please try again")

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        data['token'] = jwt_encode_handler(payload)
        data['owner_id'] = user_obj.witness.id or user_obj.officer.id

        return data


""""""
