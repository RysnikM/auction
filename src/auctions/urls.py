from .views import UserList, UserDetail, PetList, LotList, CteateNewLot, BidsList, MakeBid, CloseLot
from django.urls import path


urlpatterns=[

    path("pets/", PetList.as_view()),

    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),

    path("lots/", LotList.as_view()),
    path("add_lot/", CteateNewLot.as_view()),
    path("close_lot/", CloseLot.as_view()),

    path("bids/", BidsList.as_view()),
    path("make_bids/", MakeBid.as_view()),
]