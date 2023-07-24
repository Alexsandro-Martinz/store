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
      
        
    def update(self, instance, validated_data):
        self.partial = True
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.expire_date = validated_data.get('expire_date', instance.expire_date)
        instance.units = validated_data.get('units', instance.units)
        instance.save()
        return instance