import random
import os
import logging

import boto3
from boto3.dynamodb.conditions import Key

logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", level=logging.ERROR)

def get_unposted_post(category):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(os.environ["POST_TABLE"]) 
    resp = table.query(
        IndexName="unpostedPosts",
        KeyConditionExpression=Key('hasBeenPosted').eq('false') & Key("category").eq(category)
    )
    try:
        return random.choice(resp['Items'])
    except:
        return {}
    
def get_random_category():
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table(os.environ["CATEGORY_TABLE"]) 
    try:
        response = table.scan()
        return random.choice(response["Items"])
    except Exception as e:
        logging.ERROR("Unable to get table items: " + e)
        return ""
    