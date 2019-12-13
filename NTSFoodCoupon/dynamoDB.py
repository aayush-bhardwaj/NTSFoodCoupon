import boto3
import json

ACCESS_KEY = "AKIAUOKXMQ67BXK2MEM3"
SECRET_KEY = "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"
dynamo = boto3.resource('dynamodb',aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      region_name="us-east-1")


def get_item(table, key):
    table = dynamo.Table(table)
    response = table.get_item(
        Key=key
    )
    item = response['Item']
    return item

def put_item(table, key):
    table = dynamo.Table(table)

    table.put_item(
        Item=key
    )

put_key = {'Day':'Sunday', 'Menu':{"Breakfast":["Bread","Butter","Omelette","Tea","coffee","idli","vada"],"Lunch":{"Starters":["BabyCornChillie","Salad"],"MainCourse":["Rice","Chapatti","Panner Butter masala","Rice","Dal","Boiled eggs","Fries","Curd"],"Desserts":["Rasagulla","Fruits"]},"Dinner":{"Starters":["BabyCornChillie","Salad"],"MainCourse":["Rice","Chapatti","Panner Butter masala","Rice","Dal","Boiled eggs","Fries","Curd"],"Desserts":["Rasagulla","Fruits"]}}}
put_item("NTSFoodCouponMenu", put_key)
get_key = {'Day':'Wednesday'}
print get_item("NTSFoodCouponMenu", get_key)


