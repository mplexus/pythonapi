import rest_framework import serializers


class HelloSerializer(serializers.Serializers):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    
