from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    mail = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    @property
    def imageURL(self):
        url = 'static/images/no_image.jpg'
        if self.image.url:
            url = self.image.url
        return url


class PlatformSettings(models.Model):
    platform = models.ForeignKey(Platform,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name=("Platform"))
    cpu_count = models.IntegerField()
    ram_count = models.IntegerField()
    hdd_count = models.IntegerField()
    psu_count = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.platform} settings"


PRODUCT_CHOICES = [("CPU", "CPU"),
                   ("RAM", "RAM"),
                   ("HDD", "HDD"),
                   ("PSU", "PSU"),
                   ]


class Product(models.Model):
    type = models.CharField("Type", max_length=5, choices=PRODUCT_CHOICES)
    name = models.CharField("Model", max_length=200)
    price = models.DecimalField("Price", max_digits=7, decimal_places=2)
    image = models.ImageField("Image", null=True, blank=True)
    quantity = models.IntegerField("Qty")
    platform = models.ForeignKey(Platform,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name=("Platform"))

    def __str__(self) -> str:
        return self.name

    @property
    def imageURL(self):
        url = 'static/images/no_image.jpg'
        if self.image.url:
            url = self.image.url
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            if not item.product.digital:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address
