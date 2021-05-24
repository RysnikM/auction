from .models import User, Pet, Lot, Bid


def add_lot(owner_id: int, pet_id: int, start_price: int):
    """ дабавляет лот """

    if check_owner_of_pet(id_pet=pet_id, id_user=owner_id):
        Lot(
            start_price=start_price,
            owner=User.objects.get(id=owner_id),
            lot=Pet.objects.get(id=pet_id)
        ).save()
        return True
    else:
        return False

def make_bid(id_lot: int, rate: int):
    """ делает ставку на лот """
    pass

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

def check_owner_of_pet(id_pet: int, id_user: int):
    """ принадлежит ли питомец пользователю? """
    return Pet.objects.get(id=id_pet).owner.id == id_user

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
