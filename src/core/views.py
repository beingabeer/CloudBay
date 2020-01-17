from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


def item_list(request):
    context = {"items": Item.objects.all()}
    return render(request, "item_list.html", context)


# def home(request):
#     return HttpResponse("<h1>Item list</h1>")
