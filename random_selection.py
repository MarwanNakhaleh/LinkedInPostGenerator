import random
import logging

from boto3.dynamodb.conditions import Key

logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", level=logging.ERROR)

def get_unposted_post(table, category): 
    resp = table.query(
        IndexName="unpostedPosts",
        KeyConditionExpression=Key('hasBeenPosted').eq('false') & Key("category").eq(category)
    )
    try:
        return random.choice(resp['Items'])
    except:
        return {}
    
def get_random_category(table):
    try:
        response = table.scan()
        return random.choice(response["Items"])["category"]
    except Exception as e:
        logging.ERROR("Unable to get table items: " + e)
        return ""
    