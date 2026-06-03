from rest_framework import serializers
from .models import ScanJob


class ScanJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScanJob
        fields = "__all__"