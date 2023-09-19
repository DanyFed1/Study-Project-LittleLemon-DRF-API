from rest_framework import serializers
from .models import MenuItem, Category, Cart, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
        
        
class MenuItemSerializer(serializers.ModelSerializer):
    # Adding a nested serializer here to provide readable category details in the serialized data.
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category']
        

class CartSerializer(serializers.ModelSerializer):
    # Using related_name attribute in model ForeignKey
    user = serializers.StringRelatedField(read_only=True)
    menuitem = MenuItemSerializer(read_only=True) # For user-friendly representation
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']
        
# This will be used as a nested serializer inside the Order Serializer to represent items in an order.
class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'menuitem', 'quantity', 'unit_price', 'price']
        
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    items = OrderItemSerializer(many=True, source='orderitem_set')  # Nested serializer for items in order
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'items']