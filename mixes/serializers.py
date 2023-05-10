from rest_framework import serializers
from mixes.models import Mix

class MixSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mix
        fields = '__all__'
