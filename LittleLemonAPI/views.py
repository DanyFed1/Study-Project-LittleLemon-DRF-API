from django.shortcuts import render
from rest_framework import generics, permissions, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from .models import MenuItem, Category, Cart, Order
from .serializers import MenuItemSerializer, CategorySerializer, CartSerializer, OrderSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins can create categories

class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

@api_view(['POST', 'DELETE'])
def manage_manager_group(request, user_id=None):
    manager_group = get_object_or_404(Group, name='Manager')

    if user_id:
        user = get_object_or_404(User, id=user_id)
    else:
        user = get_object_or_404(User, id=request.data.get('user_id'))

    if request.method == 'POST':
        manager_group.user_set.add(user)
        return Response({"message": "User added to Manager group"}, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        manager_group.user_set.remove(user)
        return Response({"message": "User removed from Manager group"}, status=status.HTTP_200_OK)

@api_view(['POST', 'DELETE'])
def manage_delivery_crew_group(request, user_id=None):
    delivery_crew_group = get_object_or_404(Group, name='Delivery Crew')

    if user_id:
        user = get_object_or_404(User, id=user_id)
    else:
        user = get_object_or_404(User, id=request.data.get('user_id'))

    if request.method == 'POST':
        delivery_crew_group.user_set.add(user)
        return Response({"message": "User added to Delivery Crew group"}, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        delivery_crew_group.user_set.remove(user)
        return Response({"message": "User removed from Delivery Crew group"}, status=status.HTTP_200_OK)

class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.groups.filter(name="Manager").exists():
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.groups.filter(name="Manager").exists():
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
    
