from django.db.models.expressions import F
from rest_framework import serializers 
from django.db.models import fields
from .models import Song
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'
    def crate(self,validated_data):
        return Song(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.singer = validated_data.get('singer',instance.singer)
        instance.producer = validated_data.get('producer',instance.producer)
        instance.entertainment = validated_data.get('entertainment', instance.entertainment)
        instance.tracknum = validated_data.get('tracknum',instance.tracknum)
        return instance