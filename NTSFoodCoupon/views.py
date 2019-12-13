# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from dynamoDB import get_item,put_item
import datetime
import json


# with open('NTSFoodCouponconfig.json') as f:
#   MealTime = json.load(f)

MealTime = {
  "MealTime": {
    "Breakfast": {
      "start": 7,
      "end": 11
    },
    "Lunch": {
      "start": 12,
      "end": 16
    },
    "Dinner": {
      "start": 19,
      "end": 23
    }
  }
}

# Create your views here.

def menu_list(request):
    """
    Get Menu List for NTSFoodCoupon

    :param request:
    :return:
    """
    table = "NTSFoodCouponMenu"
    if request.method == 'GET':
        day = str(request.path.split("/")[-1])
        get_key = {'Day': day}
        data = get_item(table, get_key)
        return JsonResponse(data)

def token_list(request):
    """
    Token for a user and date

    :param request:
    :return:
    """
    table = "NTSUser"
    if request.method == 'GET':
        now = datetime.datetime.now()
        present_hour = now.hour
        coupon_option = ""
        get_key = {'user_string': '225623_12-13-2019'}
        data = get_item(table, get_key)
        if present_hour >= MealTime.get("MealTime").get("Breakfast").get("start") and present_hour < MealTime.get("MealTime").get("Breakfast").get("end"):
            if data["tokens"]["Breakfast"] == 1:
                coupon_option = "Breakfast"
        elif present_hour >= MealTime.get("MealTime").get("Lunch").get("start") and present_hour < MealTime.get("MealTime").get("Lunch").get("end"):
            if data["tokens"]["Lunch"] == 1:
                coupon_option = "Lunch"
        elif present_hour >= MealTime.get("MealTime").get("Dinner").get("start") and present_hour < MealTime.get("MealTime").get("Dinner").get("end"):
            if data["tokens"]["Dinner"] == 1:
                coupon_option = "Dinner"

        if coupon_option == "":
            return JsonResponse("You don't have any active coupon.")
        else:
            response = {"coupon": coupon_option}
            return JsonResponse(response)
