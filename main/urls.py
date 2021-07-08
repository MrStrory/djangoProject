from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    re_path(r"^products", views.products, name="products"),
    re_path(r"^product_unit", views.product_unit, name="product_unit"),
    re_path(r"^contacts", views.contacts, name="contacts"),
]