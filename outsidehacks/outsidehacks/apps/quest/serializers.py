from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Zone

class ZoneSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Zone
        fields = ('id', 'name', 'description', 'image', 'time_start', 'time_end', 'owner', )

class UserSerializer(serializers.ModelSerializer):
    zones = serializers.HyperlinkedRelatedField(many=True, view_name='zone-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'zones')
