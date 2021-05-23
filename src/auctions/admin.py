from django.contrib import admin
from .models import *
#ToDo : импорт только нужных классов из моделей

admin.site.register(User)
admin.site.register(Lot)
admin.site.register(Pet)
admin.site.register(Bid)
