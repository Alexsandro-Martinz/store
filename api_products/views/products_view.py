from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api_products.models import Product
from api_products.serializers import ProductSerializer


class ProductsList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductsDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, pk):
        
        instance = get_object_or_404(Product, pk=pk)
        serialize = ProductSerializer(data=request.data, partial=True)
        if serialize.is_valid():
            validated_data = serialize.validated_data
            instance.product_name = validated_data.get('product_name', instance.product_name)
            instance.description = validated_data.get('description', instance.description)
            instance.category = validated_data.get('category', instance.category)
            instance.expire_date = validated_data.get('expire_date', instance.expire_date)
            instance.units = validated_data.get('units', instance.units)
            instance.save()
            data = ProductSerializer(instance).data
            return Response(status=status.HTTP_200_OK, data=data)
            
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
