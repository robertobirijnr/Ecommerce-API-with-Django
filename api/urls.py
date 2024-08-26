from django.contrib import admin
from django.urls import path
from . import views
from .views import update_product, delete_product

urlpatterns = [
    path('products', views.ProductsListCreate.as_view()),
    path('product/<int:pk>',views.GetSinleProduct.as_view()),
    path('product/<int:pk>/update', update_product),
    path('product/<int:pk>/delete', delete_product),
    path('category', views.CategoryListCreate.as_view()),

]
