# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse

# Create your views here.


def menu_list(request):
    print("Hello")
    if request.method == 'GET':
        data = {
            'name': 'Vitor',
            'location': 'Finland',
            'is_active': True,
            'count': 28
        }
        return JsonResponse(data)
