# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from dynamoDB import get_item,put_item

# Create your views here.


def menu_list(request):
    table = "NTSFoodCouponMenu"
    if request.method == 'GET':
        day = str(request.path.split("/")[-1])
        get_key = {'Day': day}
        data = get_item(table, get_key)
        return JsonResponse(data)
