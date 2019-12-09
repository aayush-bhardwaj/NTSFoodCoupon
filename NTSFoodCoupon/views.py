# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse

# Create your views here.


def menu_list(request):
    print("Hello")
    if request.method == 'GET':
        data = {
          "Starters" : "Babycorn Chillie",
          "Main Course": "Chicken Curry",
          "Dessert" : "Gulab Jamun"
        }
        return JsonResponse(data)
