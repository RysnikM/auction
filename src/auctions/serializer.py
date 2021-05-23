from .models import User, Pet, Lot, Bid
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'
