from .models import *
from .serializers import *


def validate_coupon(coupon_id, cart_items):
    coupon_details = {}
    coupon_details['is_valid_coupon'] = 0
    coupon_details['invalid_coupon_reason'] = ''
    coupon_details['coupon_data'] = None
    coupon = WfMasterCouponCodes.objects.filter(coupon_id=coupon_id).first()
    if not coupon:
        coupon_details['invalid_coupon_reason'] = "coupon doesn't exist"
        return coupon_details
    coupon_details['coupon_details'] = WfMasterCouponCodesSerializer(coupon)
    if coupon.is_expired:
        coupon_details['invalid_coupon_reason'] = 'coupon is expired'
        return coupon_details


def get_cart_amount_details(carts, coupon_data):
    total_cart_price = 0
    for cart in carts:
        total_cart_price += abs(float(cart['item_price'])) * abs(int(cart['item_quantity']))
    for cart in carts:
        item_quantity = abs(int(cart['item_quantity']))
        if item_quantity == 0:
            return {'error': 'Item quantity is not vaild!'}
        item_price = abs(float(cart['item_price']))

        if coupon_data:
            net_price_data = cart_label_discount_price(
                item_sku=cart['item_sku'],
                discount_flat=coupon_data['coupon_flat_discount'],
                discount_percent=coupon_data['coupon_percentage'],
                discount_percent_accessories=coupon_data['coupon_accessories_percentage'],
                discount_percent_cot=coupon_data['coupon_cot_percentage'],
                item_quantity=item_quantity,
                item_price=item_price,
                coupon_type=coupon_data['coupon_type'],
                total_cart_price=total_cart_price
            )
            if net_price_data['status'] == 400:
                return {'message': net_price_data['message'], 'status': 400},
            cart_label_net_price = net_price_data['subtotal_discounted']

        else:
            cart_label_net_price = (item_quantity * item_price)
        cart['net_price'] = cart_label_net_price
