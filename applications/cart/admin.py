from django.contrib import admin

from applications.cart.models import Cart


class CartAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cart, CartAdmin)

