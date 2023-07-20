from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view

from api_products.models import Category
from api_products.serializers import CategorySerializer

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def categories_list(request):
    
    if request.method == "GET":
        categories = Category.objects.all()
        serialized = CategorySerializer(categories, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    
    elif request.method == 'POST':
        serialize = CategorySerializer(data=request.data)
        category = serialize.create()
        if category is not None:
            return Response(CategorySerializer(category).data)  


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def categories_detail(request):
    pass