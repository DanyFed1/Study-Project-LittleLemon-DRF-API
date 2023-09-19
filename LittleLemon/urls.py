"""
URL configuration for LittleLemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from LittleLemonAPI import views

#superuser: danyfed danyfed@danyfed.com     pass:testuser 

urlpatterns = [
    path("admin/", admin.site.urls),

    # User registration and token generation endpoints
    path('api/users/', include('djoser.urls')),
    path('api/users/', include('djoser.urls.authtoken')),
    path('api/users/', include('djoser.urls.jwt')),

    # Menu items and categories
    path('api/menu-items/', views.MenuItemListCreateView.as_view(), name='menu-items'),
    path('api/menu-items/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-item-detail'),
    path('api/categories/', views.CategoryListCreateView.as_view(), name='categories'),

    # User group management
    path('api/groups/manager/users/', views.manage_manager_group, name='manage-manager-group'),
    path('api/groups/manager/users/<int:user_id>/', views.manage_manager_group, name='manage-manager-user'),
    path('api/groups/delivery-crew/users/', views.manage_delivery_crew_group, name='manage-delivery-crew-group'),
    path('api/groups/delivery-crew/users/<int:user_id>/', views.manage_delivery_crew_group, name='manage-delivery-crew-user'),

    # Cart management
    path('api/cart/menu-items/', views.CartView.as_view(), name='cart-items'),

    # Order management
    path('api/orders/', views.OrderView.as_view(), name='orders'),
    path('api/orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]
