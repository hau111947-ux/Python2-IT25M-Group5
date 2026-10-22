from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('foods/add/', views.food_create, name='food_create'),
    path('foods/<int:pk>/', views.food_detail, name='food_detail'),
    path('foods/<int:pk>/edit/', views.food_update, name='food_update'),
    path('foods/<int:pk>/delete/', views.food_delete, name='food_delete'),
    path('foods/<int:pk>/order/', views.order_create, name='order_create'),
    path('compare/', views.food_compare, name='food_compare'),
    path('orders/', views.my_orders, name='my_orders'),
    path('orders/<int:pk>/<str:action>/', views.order_action, name='order_action'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
