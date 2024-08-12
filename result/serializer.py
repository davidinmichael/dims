from rest_framework import serializers

from account.models import Account
from .models import *



class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        models = Result
        fields = "__all__"        



