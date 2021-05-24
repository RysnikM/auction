from .models import User, Pet, Lot, Bid
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ сериализация листа пользователей """

    class Meta:
        model = User
        fields = '__all__'


class PetsSerializer(serializers.ModelSerializer):
    """ сериализация листа питомцев """

    class Meta:
        model = Pet
        fields = '__all__'


class LotSerializer(serializers.ModelSerializer):
    """ сериализация листа лотов """

    class Meta:
        model = Lot
        fields = '__all__'


class BidSerializer(serializers.ModelSerializer):
    """ сериализация листа ставок """

    class Meta:
        model = Bid
        fields = '__all__'


class LotCloseSerializer(serializers.ModelSerializer):
    """ сериализация запроса на закрытие лота """

    class Meta:
        model = Lot
        fields = '__all__'
