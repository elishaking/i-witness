from rest_framework import serializers

from ..models import Witness
from accounts.models import User
from media.models import Media
from accounts.api.serializers import AccountSerializer, AccountCreateSerializer, AccountLoginSerializer
from reports.api.serializers import ReportSerializer


# class WitnessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Witness
#         fields = ['account', 'reports']User_ = get_user_model()


class WitnessSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    # reports = ReportSerializer(many=True)

    class Meta:
        model = Witness
        fields = ['account', 'reports']


class WitnessEditSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Witness
        fields = ['account']


class WitnessCreateSerializer(serializers.ModelSerializer):
    # email_confirm = serializers.EmailField(label='Confirm Email')
    account = AccountCreateSerializer()

    class Meta:
        model = Witness
        fields = ['account']

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        # print(account_data)
        # media_data = account_data['image']
        # media = Media.objects.create(**media_data)
        # account_data['image'] = media
        account = User.objects.create(**account_data)
        witness = Witness.objects.create(account=account, **validated_data)

        return witness


class WitnessLoginSerializer(serializers.ModelSerializer):
    account = AccountLoginSerializer()

    class Meta:
        model = Witness
        fields = ['id', 'account']


""""""
