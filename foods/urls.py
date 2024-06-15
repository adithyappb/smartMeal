from django.urls import path
from . import views

urlpatterns = [
    path('food-table/', views.food_table, name='food-table'),
]