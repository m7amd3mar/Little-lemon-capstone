from django.urls import path
from .views import *

urlpatterns = [
    path('menu-items', menu_items),
    path('menu-items/<int:id>', menu_item),
]