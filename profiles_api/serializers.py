from rest_framework import serializers

class HelloSerilaizer(serializers.Serializer):
    """Serialzers a name field for testing APIView"""
    name = serializers.CharField(max_length = 10)
