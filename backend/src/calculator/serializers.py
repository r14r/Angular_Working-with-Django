from rest_framework import serializers

from django.contrib.auth.models import User

class CalculatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "id", "username"]
