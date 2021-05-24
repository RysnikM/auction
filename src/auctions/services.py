from .models import User, Pet, Lot, Bid


def close_lot(lot_id: int, bid_id: int):
    """ закрывает лот
    id - ссылка на закрываемый лот,
    bid_id - id выигровшей ставки,
    """

    update_user_balance(
        Lot.objects.get(id=lot_id).owner.id,
        Bid.objects.get(id=bid_id).rate
    )
    update_user_balance(
        Bid.objects.get(id=bid_id).owner.id,
        -Bid.objects.get(id=bid_id).rate
    )
    change_pet_owner(
        Lot.objects.get(id=lot_id).lot.id,
        Bid.objects.get(id=bid_id).owner.id,
    )

    delete_lot(lot_id)

def delete_lot(id):
    """ удаляет запить в базе данных о лоте """

    Lot.objects.filter(id=id).delete()

def update_user_balance(user_id: int, value: int):
    """ обновляет баланс юзера """

    user = User.objects.get(id=user_id)
    new_balance = user.balance + value
    user.balance = new_balance
    user.save(update_fields=['balance'])

def change_pet_owner(pet_id: int, new_owner_id: int):
    """ изменяет владельца питамца """

    pet = Pet.objects.get(id=pet_id)
    pet.owner = User.objects.get(id=new_owner_id)
    pet.save(update_fields=['owner'])
