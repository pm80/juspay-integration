from rest_framework import viewsets
from rest_framework.response import Response

from .juspay_apis import Payments


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
        pass


class CouponViewSet(viewsets.ViewSet):
    def apply_coupon(self, request, *args, **kwargs):
        pass

    def remove_coupon(self, request, *args, **kwargs):
        pass
