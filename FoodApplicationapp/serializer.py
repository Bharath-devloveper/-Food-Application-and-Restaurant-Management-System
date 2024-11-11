from rest_framework import serializers
from .models import Restarent,Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Food
        fields='__all__'


class RestarentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restarent
        fields='__all__'