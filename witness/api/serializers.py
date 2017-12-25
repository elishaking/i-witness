from rest_framework import serializers

from ..models import Witness
from accounts.models import User
from accounts.api.serializers import AccountsSerializer, AccountCreateSerializer, AccountLoginSerializer
from reports.api.serializers import ReportSerializer


# class WitnessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Witness
#         fields = ['account', 'reports']User_ = get_user_model()


class WitnessSerializer(serializers.ModelSerializer):
    account = AccountsSerializer()
    # reports = ReportSerializer(many=True)

    class Meta:
        model = Witness
        fields = ['account', 'reports']


class WitnessCreateSerializer(serializers.ModelSerializer):
    # email_confirm = serializers.EmailField(label='Confirm Email')
    account = AccountCreateSerializer()

    class Meta:
        model = Witness
        fields = ['account']

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        # print(account_data)
        account = User.objects.create(**account_data)
        witness = Witness.objects.create(account=account, **validated_data)

        return witness


class WitnessLoginSerializer(serializers.ModelSerializer):
    account = AccountLoginSerializer()

    class Meta:
        model = Witness
        fields = ['account']


""""""
