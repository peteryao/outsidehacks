from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Zone, Badge, Cateogry, Quest, UserQuest, UserBadge

class ZoneSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Zone
        fields = ('id', 'name', 'description', 'image', 'time_start', 'time_end', 'owner', )

class BadgeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Badge
        fields = ('id', 'name', 'description', 'image', 'owner', )

class CateogrySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Cateogry
        fields = ('id', 'name', 'description', 'image', 'owner', )

class QuestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Quest
        fields = ('id', 'name', 'cateogry', 'description', 'image', 'points_awarded', 'zone', 'owner', )

class UserQuestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserQuest
        fields = ('id', 'user', 'quest', 'completed', 'owner', )

class UserBadgeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UserBadge
        fields = ('id', 'user', 'badge', 'owner', )


class UserSerializer(serializers.ModelSerializer):
    zones = serializers.HyperlinkedRelatedField(many=True, view_name='zone-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'zones')
