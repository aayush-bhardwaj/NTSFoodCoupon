# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from dynamoDB import get_item,put_item, get_all_items
from django.views.decorators.csrf import csrf_exempt
import datetime
import calendar
import json


# with open('NTSFoodCouponconfig.json') as f:
#   MealTime = json.load(f)

"""
STATUS CODES:
0 = INACTIVE
1 = ACTIVE
2 = USED
3 = NO SHOW
4 = CANCELLED
"""

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

shiftCoupon = {
    "nts-shift-5": ["Dinner"],
    "nts-shift-6": ["Dinner", "Breakfast"]
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
    if request.method == 'POST':
	return JsonResponse({"a":"b"})

@csrf_exempt 
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
        get_key = {'user_string': '225623_12-14-2019'}
        data = get_item(table, get_key)
        if present_hour >= MealTime.get("MealTime").get("Breakfast").get("start") and present_hour < MealTime.get("MealTime").get("Breakfast").get("end"):
            if data["Breakfast"] == 1:
                coupon_option = "Breakfast"
        elif present_hour >= MealTime.get("MealTime").get("Lunch").get("start") and present_hour < MealTime.get("MealTime").get("Lunch").get("end"):
            if data["Lunch"] == 1:
                coupon_option = "Lunch"
        elif present_hour >= MealTime.get("MealTime").get("Dinner").get("start") and present_hour < MealTime.get("MealTime").get("Dinner").get("end"):
            if data["Dinner"] == 1:
                coupon_option = "Dinner"

        if coupon_option == "":
            return JsonResponse({"response":"You don't have any active coupon."})
        else:
            response = {"response": coupon_option}
            return JsonResponse(response)

    if request.method == 'POST':
        body = str(request.body)
        emp_id = "225623"
        now = datetime.datetime.now()
        user_string = emp_id + "_" + str(now.month) + "-" + str(now.day) + "-" + str(now.year)
        put_key = {"user_string": user_string}
        data = get_item("NTSUser", put_key)
        data[body] = 2
        put_item(table, data)
        return JsonResponse({"response": "Enjoy your %s." %body})


@csrf_exempt
def feedback(request):
    """
    Feedback for a user and date

    :param request:
    :return:
    """
    table = "NTSUser"
    if request.method == 'POST':
        body = str(request.body).split("&")
        foodQuality = body[0].split("=")[1]
        hygiene = body[1].split("=")[1]
        staffBehaviour = body[2].split("=")[1]
        feedback = body[3].split("=")[1]
        meal = body[4].split("=")[1]
        emp_id = "225623"
        now = datetime.datetime.now()
        user_string = emp_id + "_" + str(now.month) + "-" + str(now.day) + "-" + str(now.year)
        put_key = {"user_string": user_string}
        data = get_item("NTSUser", put_key)
        data["rating"][meal]["Feedback"] = str(feedback)
        data["rating"][meal]["FoodQuality"] = int(foodQuality)
        data["rating"][meal]["Hygiene"] = int(hygiene)
        data["rating"][meal]["StaffBehaviour"] = int(staffBehaviour)
        put_item(table, data)
        return JsonResponse({"response": "Your Feedback has been submitted."})


@csrf_exempt
def cancel(request):
    """
    Feedback for a user and date

    :param request:
    :return:
    """
    table = "NTSUser"
    if request.method == 'POST':
        body = str(request.body).split("&")
        date = body[0].split("=")[1].split("/")
        meals = str(body[1].split("=")[1]).split(",")
        month = date[1]
        day = date[0]
        emp_id = "225623"
        now = datetime.datetime.now()
        if str(day) == str(now.day):
            return JsonResponse({"response": "You cannot cancel today's meal."})
        user_string = emp_id + "_" + str(month) + "-" + str(day) + "-" + str(now.year)
        put_key = {"user_string": user_string}
        data = get_item("NTSUser", put_key)
        for meal in meals:
            if data[meal] == 1:
                data[meal] = 4
        put_item(table, data)
        return JsonResponse({"response": "Your meal has been cancelled."})

@csrf_exempt
def guest(request):
    """
    Feedback for a user and date

    :param request:
    :return:
    """
    table = "NTSguest"
    if request.method == 'POST':
        meals = str(request.body).split("=")[-1].split(",")
        now = datetime.datetime.now()
        date = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
        get_key = {"Date": date}
        data = get_item(table, get_key)
        if data == -1:
            put_key = {"date": date, "Breakfast" : 0, "Lunch": 0, "Dinner": 0}
            put_item(table, put_key)
        else:
            for meal in meals:
                data[meal] = data[meal] + 1
        put_item(table, data)
        return JsonResponse({"response": "Guest has been added meals."})

@csrf_exempt
def add(request):
    """
    Feedback for a user and date

    :param request:
    :return:
    """
    table = "NTSUser"
    if request.method == 'POST':
        body = request.body.split("&")
        employeeID = body[0].split("=")[1]
        meals = body[1].split("=")[1].split(",")
        date = body[2].split("/")
        day = date[0]
        month = date[1]
        year = date[2]
        user_string = employeeID + "_" + month + "-" + day + "-" + year
        get_key = {"user_string": user_string}
        data = get_item(table, get_key)
        for meal in meals:
            data[meal] = 1
        put_item(table, data)
        return JsonResponse({"response": "Added meals for User."})

@csrf_exempt
def provision(request):
    """
    Feedback for a user and date

    :param request:
    :return:
    """
    tableUserList = "NTSUserList"
    tableUser = "NTSUser"
    if request.method == 'POST':
        body = request.body.split("&")
        month = body[0].split("=")[1]
        year = body[1].split("=")[1]
        days = []
        cal = calendar.Calendar()
        for x in cal.itermonthdays2(year, month):
            if x[0] != 0 and x[1] < 5:
                days.append(x[0])

        user_list = get_all_items(tableUserList)
        for user in user_list:
            for day in days:
                token_date = str(month) + "-" + str(day) + "-" + str(year)
                user_string = user["emp_id"] + "_" + token_date
                breakfast = 0
                lunch = 0
                dinner = 0
                if "Breakfast" in shiftCoupon[user["shift"]]:
                    breakfast = 1
                if "Lunch" in shiftCoupon[user["shift"]]:
                    lunch = 1
                if "Dinner" in shiftCoupon[user["shift"]]:
                    dinner = 1

                put_key = {"username": user["email"], "emp_id": user["emp_id"], "date": token_date,
                           "user_string": user_string, "Breakfast": breakfast, "Lunch": lunch, "Dinner": dinner, "rating": {
                        "Breakfast": {"Hygiene": -1, "FoodQuality": -1, "StaffBehaviour": -1, "average": 0,
                                      "Feedback": "0"},
                        "Lunch": {"Hygiene": -1, "FoodQuality": -1, "StaffBehaviour": -1, "Feedback": "0",
                                  "average": 0},
                        "Dinner": {"Hygiene": -1, "FoodQuality": -1, "StaffBehaviour": -1, "Feedback": "0",
                                   "average": 0}}}
                put_item(tableUser, put_key)
        return JsonResponse({"response": "Coupons have been assigned."})


