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