from django.urls import path
from .views import search_cocktails,cocktail_detail

urlpatterns = [
    path('',search_cocktails, name='search'),
    path('cocktail/<int:drink_id>/',cocktail_detail, name='cocktail_detail'),
]




