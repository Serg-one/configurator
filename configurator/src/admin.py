from django.contrib import admin
from src.models import Platform, PlatformSettings, Product, Customer, Order, ShippingAddress

class PlatformAdmin(admin.ModelAdmin):
    admin_order_field = 'id'
    list_display = ('id', 'name', 'price', 'image')
admin.site.register(Platform, PlatformAdmin)

class PlatformSettingsAdmin(admin.ModelAdmin):
    admin_order_field = 'id'
    list_display = ('id', 'platform', 'cpu_count', 'ram_count', 'hdd_count', 'psu_count')
admin.site.register(PlatformSettings, PlatformSettingsAdmin)

class ProductAdmin(admin.ModelAdmin):
    admin_order_field = 'id'
    list_display = ('id', 'type', 'name', 'price', 'quantity', 'platform', 'image')
admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    admin_order_field = 'id'
    list_display = ('id', 'name', 'mail')
admin.site.register(Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    admin_order_field = 'id'
    list_display = ('id', 'customer', 'date_ordered', 'transaction_id', 'complete')
admin.site.register(Order, OrderAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    admin_order_field = 'id'
    list_display = ('id', 'customer', 'order', 'address', 'city', 'state', 'zip_code', 'date_added')
admin.site.register(ShippingAddress, ShippingAddressAdmin)
