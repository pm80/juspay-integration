from django.urls import path

from api import views

urlpatterns = [
    path('paymentmethods', views.PaymentViewSet.as_view({'get': 'payment_methods'}), name='payment_methods'),
    path('orders', views.OrderViewSet.as_view({'post': 'create_order'}), name='create_order'),
    path('orders/<slug:order_id>/', views.OrderViewSet.as_view({'get': 'order_status'}), name='order_status'),
    path('cardbins/<slug:cardbins>', views.CardViewSet.as_view({'get': 'card_info'}), name='card_info'),
    path('apply-coupon', views.CouponViewSet.as_view({'post': 'apply_coupon'}), name='apply_coupon'),
    path('remove-coupon', views.CouponViewSet.as_view({'post': 'remove_coupon'}), name='remove_coupon'),
]
