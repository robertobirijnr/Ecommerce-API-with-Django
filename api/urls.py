from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products', views.ProductsListCreate.as_view()),
    path('category', views.CategoryListCreate.as_view()),

]
