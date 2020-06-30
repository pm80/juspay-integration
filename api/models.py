from django.db import models

# Create your models here.
class WfTempOnlineOrderHistory(models.Model):
    payment_platform = models.CharField(max_length=128)
    transaction_id = models.CharField(max_length=20)
    login_id = models.IntegerField()
    cart_items = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email_address = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=20)
    alternate_mobile_number = models.CharField(max_length=20)
    address = models.TextField()
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.IntegerField()
    pincode = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    gst_organization = models.CharField(max_length=100)
    additional_comments = models.TextField()
    coupon_id = models.IntegerField()
    coupon_code = models.CharField(max_length=255)
    coupon_percentage = models.CharField(max_length=20)
    coupon_flat_discount = models.CharField(max_length=20)
    create_timestamp = models.DateTimeField()

    class Meta:
        # managed = True
        db_table = 'wf_temp_online_order_history'
