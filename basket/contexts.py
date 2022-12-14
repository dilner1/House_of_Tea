from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def current_basket(request):

    basket_items = []
    total = 0
    product_quantity = 0
    basket = request.session.get('basket', {})

    for pk, product_data in basket.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=pk)
            total += product_data * product.price
            name = product.name
            product_quantity += product_data
            basket_items.append({
                'pk': pk,
                'total': total,
                'product': product,
                'quantity': product_data,
                'price': product.price * product_data,
            })
        else:
            product = get_object_or_404(Product, pk=pk)
            for weight, quantity, in product_data['item_weight'].items():
                product = get_object_or_404(Product, pk=pk)
                total += quantity * product.price
                product_quantity += quantity
                weight_quantity = product_data['item_weight']
                basket_items.append({
                    'pk': pk,
                    'total': total,
                    'product': product,
                    'quantity': product_data,
                    'weight': weight,
                    'price': product.price * quantity,
                    'weight_quantity': weight_quantity,
                })

    if total < settings.DELIVERY_CHARGE_MAX:
        delivery = total * settings.DELIVERY_CHARGE / 50
        delivery_threshold = settings.DELIVERY_CHARGE_MAX - delivery

    else:
        delivery = 30
        delivery_threshold = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_quantity': product_quantity,
        'delivery': delivery,
        'delivery_threshold': delivery_threshold,
        'grand_total': grand_total,
        'delivery_charge': settings.DELIVERY_CHARGE,
        'delivery_charge_max': settings.DELIVERY_CHARGE_MAX,
     }

    return context
