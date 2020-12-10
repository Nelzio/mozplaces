from rest_framework import serializers
from .models import Province


class ProvinceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Province
        fields = '__all__'
