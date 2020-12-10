from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import District
from .serializers import DistrictSerializer
from provinces.models import Province


@api_view(['GET'])
def get_district_api(request, format=None):
    if request.GET.get('id') is not None:
        district = District.objects.filter(id=request.GET.get('id'))
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data)
    if request.GET.get('province') is not None:
        province = Province.objects.get(name=request.GET.get('province'))
        district = District.objects.filter(province=province)
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data)
    if request.GET.get('province_id') is not None:
        district = District.objects.filter(
            province_id=request.GET.get('province_id'))
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data)
    province = District.objects.all()
    serializer = DistrictSerializer(province, many=True)
    return Response(serializer.data)
