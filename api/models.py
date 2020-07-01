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

    objects = models.Manager()

    class Meta:
        # managed = True
        db_table = 'wf_temp_online_order_history'


class WfMasterCouponClassifications(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    order_by = models.SmallIntegerField()

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'wf_master_coupon_classifications'


class WfMasterCouponCodes(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_uid = models.CharField(max_length=20)
    coupon_type = models.IntegerField()
    coupon_classification_id = models.SmallIntegerField()
    coupon_code = models.CharField(unique=True, max_length=100)
    coupon_percentage = models.IntegerField()
    coupon_accessories_percentage = models.SmallIntegerField(default=0)
    coupon_cot_percentage = models.IntegerField(default=0)
    coupon_flat_discount = models.FloatField()
    coupon_max_discount = models.FloatField()
    coupon_min_amount = models.FloatField()
    coupon_description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    is_expired = models.IntegerField(default=0)
    created_by = models.IntegerField()
    created_timestamp = models.DateTimeField()
    updated_by = models.SmallIntegerField()
    update_timestamp = models.DateTimeField(blank=True, null=True)
    is_public = models.IntegerField(default=1)
    is_active = models.IntegerField()

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'wf_master_coupon_codes'

    # def get_percentage(self, item_sku):
    #     sku_code = get_item_sku_code(item_sku)
    #     if sku_code is None:
    #         return None
    #     if sku_code in MATTRESS_SKUS:
    #         return self.coupon_percentage
    #     if sku_code in T2_SKUS:
    #         return self.coupon_cot_percentage
    #     return self.coupon_accessories_percentage


class WfMasterCouponTypes(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.IntegerField()
    show_order = models.IntegerField()

    objects = models.Manager()

    class Meta:
        managed = False
        db_table = 'wf_master_coupon_types'
