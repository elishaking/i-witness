from rest_framework import serializers

from ..models import Officer
from accounts.models import User
from accounts.api.serializers import AccountsSerializer, AccountCreateSerializer, AccountLoginSerializer

from django.contrib.auth import get_user_model
from django.db.models import Q

from ..models import Officer

# class OfficerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Officer
#         fields = ['account', 'id', 'activity']


class OfficerSerializer(serializers.ModelSerializer):
    account = AccountsSerializer()

    class Meta:
        model = Officer
        fields = ['account']


class OfficerCreateSerializer(serializers.ModelSerializer):
    # email_confirm = serializers.EmailField(label='Confirm Email')
    account = AccountCreateSerializer()

    class Meta:
        model = Officer
        fields = ['account']

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        #print(account_data)
        account = User.objects.create(**account_data)
        officer = Officer.objects.create(account=account, **validated_data)

        return officer


class OfficerLoginSerializer(serializers.ModelSerializer):
    account = AccountLoginSerializer()

    class Meta:
        model = Officer
        fields = ['account']


""""""
