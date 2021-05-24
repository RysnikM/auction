from .models import User, Pet, Lot, Bid
from .serializer import UserSerializer, PetsSerializer, LotSerializer, BidSerializer, LotCloseSerializer
from .services import add_lot, close_lot, make_bid

from rest_framework.views import APIView
from rest_framework.response import Response


class UserList(APIView):
    """ получение списка пользователей """
    def get(self, request):
        user_list = User.objects.all()
        user_list_serialize = UserSerializer(user_list, many=True)
        return Response(user_list_serialize.data)


class UserDetail(APIView):
    """ получние данных о конкретном пользователе """
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        user_serialize = UserSerializer(user)
        return Response(user_serialize.data)


class PetList(APIView):
    """ получение данных о котиках и ежиках """
    def get(self, request):
        pets = Pet.objects.all()
        pets_serialize = PetsSerializer(pets, many=True)
        return Response(pets_serialize.data)


class LotList(APIView):
    def get(self, request):
        lots = Lot.objects.all()
        lots_serialize = LotSerializer(lots, many=True)
        return Response(lots_serialize.data)


class BidsList(APIView):
    """ получение списка ставок """
    def get(self, request):
        rates = Bid.objects.all()
        rates_serialize = BidSerializer(rates, many=True)
        return Response(rates_serialize.data)


class CteateNewLot(APIView):
    """ добавление нового лота """
    def post(self, request):
        new_lot = LotSerializer(data=request.data)
        if new_lot.is_valid() and add_lot(
                owner_id=new_lot.data['owner'],
                pet_id=new_lot.data['lot'],
                start_price=new_lot.data['start_price']):
            return Response(status=201)
        else:
            return Response(status=400)


class MakeBid(APIView):
    """ сдать ставку """
    def post(self, request):
        new_bid = BidSerializer(data=request.data)
        #ToDo: add validation
        if new_bid.is_valid():
            return Response(status=201)
        else:
            return Response(status=400)


class CloseLot(APIView):
    """ закрыть и удалить лот, удалить связанные ставки, повысить баланс владельца, сменить владельца питомца"""
    def post(self, request):
        lot = LotCloseSerializer(data=request.data)
        if lot.is_valid():
            close_lot(
                lot_id=request.data['id'],
                bid_id=request.data['bid_id'],
            )
            return Response(status=204)
        else:
            return Response(status=400)
