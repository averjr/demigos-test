from django.contrib import admin

from .models import Currency, Pair, Price

admin.site.register(Currency)
admin.site.register(Pair)
admin.site.register(Price)
