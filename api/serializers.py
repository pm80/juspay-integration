from rest_framework import serializers
from .models import *


class WfMasterCouponCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WfMasterCouponCodes
        fields = '__all__'
