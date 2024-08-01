from django.urls import path
from . import views


urlpatterns = [
    path('',views.product_list,name='product_list' ),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
]