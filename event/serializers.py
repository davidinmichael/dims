from rest_framework import serializers
from .models import *
from account.models import Account


class EventSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field="first_name", queryset=Account.objects.all(), required=False)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "image",
            "event_date",
            "event_time",
            "venue_address",
            "created_at",
            "created_by",
        ]
