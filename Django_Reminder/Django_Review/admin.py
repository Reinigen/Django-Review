from django.contrib import admin
from .models import weapon, weapon_order, order

# Register your models here.
admin.site.register(weapon)
admin.site.register(weapon_order)
admin.site.register(order)