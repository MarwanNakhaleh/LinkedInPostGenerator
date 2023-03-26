import random
import logging

from boto3.dynamodb.conditions import Key

logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s")
log = logging.getLogger("LinkedInPoster")
log.setLevel(logging.INFO)

def get_unposted_post(table, category): 
    resp = table.query(
        IndexName="unpostedPosts",
        KeyConditionExpression=Key('hasBeenPosted').eq('false') & Key("category").eq(category)
    )
    try:
        if len(resp["Items"]) > 0:
            log.info("found unposted post")
            return random.choice(resp['Items'])
        else:
            log.warn("no posts available")
            quit()
    except:
        return {}
    
def get_categories(table):
    try:
        response = table.scan()
        return [cat["category"] for cat in response["Items"]]
    except Exception as e:
        log.error("Unable to get categories from table: " + e)
        return ""
    
def get_random_choice(options):
    try:
        return random.choice(options)
    except Exception as e:
        log.error("Unable to choose random value: " + e)
        return ""
    