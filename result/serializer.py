from rest_framework import serializers
from .models import *



class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        models = Result
        fields = "__all__"        



