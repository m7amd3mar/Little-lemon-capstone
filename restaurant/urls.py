from django.urls import path
from .views import *

urlpatterns = [
    path('', MenuItemsView.as_view()),
    path('<int:pk>', MenuItemDetailView.as_view()),
]