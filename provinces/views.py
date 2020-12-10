from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Province
from .serializers import ProvinceSerializer


@api_view(['GET'])
def get_province_api(request, format=None):
    if request.GET.get('id') is not None:
        province = Province.objects.filter(id=request.GET.get('id'))
        serializer = ProvinceSerializer(province, many=True)
        return Response(serializer.data)
    province = Province.objects.all()
    serializer = ProvinceSerializer(province, many=True)
    return Response(serializer.data)
