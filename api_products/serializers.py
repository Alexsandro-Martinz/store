from rest_framework import serializers
from api_products.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category
      
        
    def update(self, instance, validate_data):
        instance.category_name = validate_data.get('category_name', instance.category_name)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product
      
        
    def update(self, instance, validate_data):
        instance.product_name = validate_data.get('product_name', instance.product_name)
        instance.description = validate_data.get('description', instance.description)
        instance.category = validate_data.get('category', instance.category)
        instance.expired_date = validate_data.get('expired_date', instance.expired_date)
        instance.units = validate_data.get('units', instance.units)
        instance.save()
        return instance