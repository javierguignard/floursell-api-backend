from rest_framework import serializers
from .models import User, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user_type',)


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False, read_only=True)


    class Meta:
        model = User
        fields = ('account','first_name','last_name','is_superuser','email')