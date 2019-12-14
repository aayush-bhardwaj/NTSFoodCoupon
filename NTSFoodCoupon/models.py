# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

def create_dynamodb_NTSFoodCouponMenu(session):
    """Create Dyanamodb table NTSFoodCoupon"""
    client = session.client('dynamodb')
    try:
        tables = client.list_tables()['TableNames']
        if "NTSFoodCouponMenu" not in tables:
            response = client.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': "Day",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "Menu",
                        'AttributeType': 'S'
                    }
                ],
                KeySchema=[
                    {
                        'AttributeName': "Day",
                        'KeyType': 'HASH'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5,
                },
                TableName="NTSFoodCouponMenu"
            )
        else:
            response = "Table already exists!"

    except Exception as e:
        print(e)
        exit(1)

    return response



def create_dynamodb_NTSguest(session):
    """Create Dyanamodb table NTSguest"""
    client = session.client('dynamodb')
    try:
        tables = client.list_tables()['TableNames']
        if "NTSguest" not in tables:
            response = client.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': "Date",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "Breakfast",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "Dinner",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "Lunch",
                        'AttributeType': 'S'
                    }
                ],
                KeySchema=[
                    {
                        'AttributeName': "Date",
                        'KeyType': 'HASH'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5,
                },
                TableName="NTSguest"
            )
        else:
            response = "Table already exists!"

    except Exception as e:
        print(e)
        exit(1)

    return response


def create_dynamodb_NTSUserList(session):
    """Create Dyanamodb table NTSFoodCOupon"""
    client = session.client('dynamodb')
    try:
        tables = client.list_tables()['TableNames']
        if "NTSUserList" not in tables:
            response = client.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': "emp_id",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "email",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "password",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "shift",
                        'AttributeType': 'S'
                    }
                ],
                KeySchema=[
                    {
                        'AttributeName': "emp_id",
                        'KeyType': 'HASH'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5,
                },
                TableName="NTSUserList"
            )
        else:
            response = "Table already exists!"

    except Exception as e:
        print(e)
        exit(1)

    return response


def create_dynamodb_NTSUser(session):
    """Create Dyanamodb table NTSUser"""
    client = session.client('dynamodb')
    try:
        tables = client.list_tables()['TableNames']
        if "NTSUserList" not in tables:
            response = client.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': "user_string",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "Breakfast",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "Dinner",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "Lunch",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "date",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "emp_id",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "rating",
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': "username",
                        'AttributeType': 'S'
                    }
                ],
                KeySchema=[
                    {
                        'AttributeName': "user_string",
                        'KeyType': 'HASH'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5,
                },
                TableName="NTSUserList"
            )
        else:
            response = "Table already exists!"

    except Exception as e:
        print(e)
        exit(1)

    return response
