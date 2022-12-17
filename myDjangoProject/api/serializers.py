from rest_framework import serializers

class DiagSerializer(serializers.Serializer):
    cols = serializers.IntegerField()
    rows = serializers.IntegerField()
    args = serializers.CharField()
    result = serializers.CharField()
