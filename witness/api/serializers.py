from rest_framework import serializers

from ..models import Witness
from accounts.api.serializers import AccountsSerializer, AccountCreateSerializer
from drf_writable_nested import WritableNestedModelSerializer

from django.contrib.auth import get_user_model
from django.db.models import Q


# class WitnessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Witness
#         fields = ['account', 'reports']User_ = get_user_model()

User_ = get_user_model()


class WitnessSerializer(serializers.ModelSerializer):
    account = AccountsSerializer()

    class Meta:
        model = Witness
        fields = ['account']


class WitnessCreateSerializer(WritableNestedModelSerializer):
    # email_confirm = serializers.EmailField(label='Confirm Email')
    account = AccountCreateSerializer()

    class Meta:
        model = Witness
        fields = ['account']


class WitnessLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    auth_field = serializers.CharField(label="Username or Email")
    # email = serializers.EmailField()

    class Meta:
        model = Witness
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
