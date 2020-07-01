from rest_framework import viewsets
from rest_framework.response import Response

from .juspay_apis import *

from .utils import *


class OrderViewSet(viewsets.ViewSet):
    def create_order(self, request, *args, **kwargs):
        pass

    def order_status(self, request, *args, **kwargs):
        pass


class PaymentViewSet(viewsets.ViewSet):
    def payment_methods(self, request, *args, **kwargs):
        juspay_resp = Payments.payment_methods()
        return Response(juspay_resp)


class CardViewSet(viewsets.ViewSet):
    def card_info(self, request, *args, **kwargs):
        cardbins = kwargs['cardbins']
        juspay_resp = Card.card_info(cardbins)
        return Response(juspay_resp) # todo status 400 handle


class CouponViewSet(viewsets.ViewSet):
    def apply_coupon(self, request, *args, **kwargs):
        coupon_id = request.data['coupon_id']
        cart_items = request.data['cart_items']
        coupon_details = validate_coupon(coupon_id, cart_items)
        resp = {}
        resp.update(coupon_details)
        is_valid_coupon = coupon_details['is_valid_coupon']
        if not is_valid_coupon:
            return Response(resp)
        carts = {}
        cart_amount_details = get_cart_amount_details(carts, coupon_details['coupon_data'])
        resp.update(cart_amount_details)
        return Response(resp)

    def remove_coupon(self, request, *args, **kwargs):
        pass
