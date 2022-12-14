"""Checkout app admin file"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Allows to add and edit line items in the admin right from
    inside the order model
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """Extends the built in model admin class for Categoriy model"""
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email',
              'phone_number', 'address_line1', 'address_line2', 'postcode',
              'town_or_city', 'county', 'order_total', 'original_bag',
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
