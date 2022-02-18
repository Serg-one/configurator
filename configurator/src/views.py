import json
from urllib import response
from django.http import JsonResponse
from django.shortcuts import render

from src.models import Platform, PlatformSettings, Product, Order, OrderItem


def platform(request):
    """ PLatform choice for user """

    platforms = Platform.objects.all()
    context = {"platforms": platforms}

    return render(request, 'src/platform.html', context)


def configurator(request):
    """ Configurator for choosen platform """

    platform_id = request.GET.get('platform')
    platform = Platform.objects.get(id=platform_id)
    platform_settings = PlatformSettings.objects.get(platform_id=platform_id)
    cpus = Product.objects.filter(type="CPU").filter(platform=platform_id)
    rams = Product.objects.filter(type="RAM").filter(platform=platform_id)
    hdds = Product.objects.filter(type="HDD").filter(platform=platform_id)
    psus = Product.objects.filter(type="PSU").filter(platform=platform_id)

    context = {"platform": platform,
               "platform_settings": platform_settings,
               "cpu_list": cpus,
               "ram_list": rams,
               "hdd_list": hdds,
               "psu_list": psus}

    return render(request, 'src/configurator.html', context)


def checkout(request):
    cpu_name = request.GET.get('cpuSelect')
    ram_name = request.GET.get('ramSelect').rsplit('+', 1)
    hdd_name = request.GET.get('hddSelect').rsplit('+', 1)
    psu_name = request.GET.get('psuSelect').rsplit('+', 1)
    cpu_price = request.GET.get('cpuSelect').rsplit('+', 1)
    ram_price = request.GET.get('ramSelect').rsplit('+', 1)
    hdd_price = request.GET.get('hddSelect').rsplit('+', 1)
    psu_price = request.GET.get('psuSelect').rsplit('+', 1)

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, _ = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    # else:
    items = []
    items.append(cpu_price)
    items.append(ram_price)
    items.append(hdd_price)
    items.append(psu_price)
    print(items)
    order = {"get_cart_total": 0,
             "get_cart_items": 0,
             "shipping": False}

    context = {"items": items,
               "order": order}

    return render(request, 'src/checkout.html', context)


def update_current_config(request):
    # data = json.loads(request.body)
    # print(data)
    # product_id = request.GET.get('product')
    # product = Product.objects.get(id=product_id)

    response_data = {
        # "product_name": product,
    }
    return JsonResponse(response_data)


def login(request):
    context = {}
    return response(request, "src/login.html", context)


def cart(request):
    context = {}
    return response(request, "src/cart", context)
