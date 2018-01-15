from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from ..models import User
from .serializers import AccountsSerializer


class AccountListAPIView(ListAPIView):
    """
    This class API view is responsible for returning
    the entire table content
    """
    queryset = User.objects.all()
    serializer_class = AccountsSerializer


class AccountRetrieveAPIView(RetrieveAPIView):
    """
    This class API view is responsible for returning
    a single object/row in the table
    """
    queryset = User.objects.all()
    serializer_class = AccountsSerializer


class AccountEditAPIView(UpdateAPIView):
    """
    This class API view is responsible for updating
    a single object/row in the table
    """
    queryset = User.objects.all()
    serializer_class = AccountsSerializer


