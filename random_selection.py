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
            log.warn("found unposted post")
            return random.choice(resp['Items'])
        else:
            log.info("no posts available")
            quit()
    except:
        return {}
    
def get_random_category(table):
    try:
        response = table.scan()
        return random.choice(response["Items"])["category"]
    except Exception as e:
        log.error("Unable to get table items: " + e)
        return ""
    