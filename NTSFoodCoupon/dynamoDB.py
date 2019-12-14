import boto3
import json

ACCESS_KEY = "AKIAUOKXMQ67NFPZF6HC"
SECRET_KEY = "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"
dynamo = boto3.resource('dynamodb',aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      region_name="us-east-1")


def get_item(table, key):
    try:
        table = dynamo.Table(table)
        response = table.get_item(
            Key=key
        )
        item = response['Item']
    except Exception as error:
        print("Key is not present in table.")
        return -1
    return item

def put_item(table, key):
    table = dynamo.Table(table)

    table.put_item(
        Item=key
    )

"""
# Test NTSFoodCoupon
put_key = {'Day':'Sunday', 'Menu':{"Breakfast":["Bread","Butter","Omelette","Tea","coffee","idli","vada"],"Lunch":{"Starters":["BabyCornChillie","Salad"],"MainCourse":["Rice","Chapatti","Panner Butter masala","Rice","Dal","Boiled eggs","Fries","Curd"],"Desserts":["Rasagulla","Fruits"]},"Dinner":{"Starters":["BabyCornChillie","Salad"],"MainCourse":["Rice","Chapatti","Panner Butter masala","Rice","Dal","Boiled eggs","Fries","Curd"],"Desserts":["Rasagulla","Fruits"]}}}
put_item("NTSFoodCouponMenu", put_key)
get_key = {'Day':'Wednesday'}
print get_item("NTSFoodCouponMenu", get_key)
"""


# Test NTSUser
# put_key = {"username":"aayush.bharadwaj@ntsindia.co.in","emp_id":225623,"date":"12-20-2019","user_string":"225623_12-20-2019","Breakfast":0,"Lunch":0,"Dinner":1,"rating":{"Breakfast":{"Hygiene":-1,"FoodQuality":-1,"StaffBehaviour":-1,"average":0,"Feedback":"0"},"Lunch":{"Hygiene":-1,"FoodQuality":-1,"StaffBehaviour":-1,"Feedback":"0","average":0},"Dinner":{"Hygiene":-1,"FoodQuality":-1,"StaffBehaviour":-1,"Feedback":"0","average":0}}}
# put_item("NTSUser", put_key)
get_key = {'user_string' : '223317'}
print get_item("NTSUser", get_key)["tokens"]["Lunch"]==0

