from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializers import *
# Create your views here.
# def index(request):
#    return render(request, 'index.html', {})

@api_view(['GET'])
def menu_items(request):
    all_items = Menu.objects.all()
    serialized_items = MenuItemSerializer(all_items, many=True)
    return Response(serialized_items.data)

@api_view(['GET'])
def menu_item(request, id):
    item = get_object_or_404(Menu, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)