from django.db import models


class User(models.Model):
    """
    класс описывает модель пользователя

    Attributes
    ===========
    - name -  имя пользователя
    - balance - баланс пользователя
    """
    name = models.CharField(max_length=100, default='no name')
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Pet(models.Model):
    """
    класс описывает модель котика или ежика

    Attributes
    ===========
    - nikname - кличка;
    - breed - порода;
    - owner - FK -> User владелец;
    ===========
    PET - список питомцев на выбор "котик" или "ежик"
    """

    PET = (
        ('CAT', 'Cat'),
        ('HADGEHOGS', 'Hadgehogs'),
    )

    nikname = models.CharField(max_length=100)
    breed = models.CharField(max_length=20, choices=PET)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nikname


class Lot(models.Model):
    """
       класс описывает модель Лота

       Attributes
       ===========
       - start_price - стартовая цена
       - owner -  FK -> внешний ключь для пользователя, выставившего лот на продажу
       - lot - FK -> ключь на выставленный на продажу котика или ежика
            (в данной реализаци принимается возможным выставить на продажу только один лот)
       """

    start_price = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lot = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # ToDo: продумать выборку только нужных лотов в зависимости от выбранног владельца

    def __str__(self):
        return 'User: %s, lot: %s' % (self.owner, self.lot)


class Bid(models.Model):
    """
       класс описывает модель ставки

       Attributes
       ===========
       - owner -  FK -> внешний ключь для пользователя, выставившего лот на продажу
       - rate - размер ставки

       """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    def __str__(self):
        return 'User: %s, make rate %s' % (self.owner, self.rate)