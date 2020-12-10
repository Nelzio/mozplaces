from rest_framework import serializers
from .models import District


class DistrictSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = District
        fields = '__all__'
