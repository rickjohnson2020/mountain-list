from rest_framework import serializers
from mountains.models import Mountain


class MountainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mountain
        fields = '__all__'
