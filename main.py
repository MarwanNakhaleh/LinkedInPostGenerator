import os
import logging

import boto3
from boto3.dynamodb.conditions import Key

import requests

logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)

post_without_link = {
    "author": "urn:li:person:_Lng4gTp4g",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello World! This is my first Share on LinkedIn!"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

post_with_link = {
    "author": "urn:li:person:_Lng4gTp4g",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Learning more about LinkedIn by reading the LinkedIn Blog!"
            },
            "shareMediaCategory": "ARTICLE",
            "media": [
                {
                    "status": "READY",
                    "description": {
                        "text": "Official LinkedIn Blog - Your source for insights and information about LinkedIn."
                    },
                    "originalUrl": "https://blog.linkedin.com/",
                    "title": {
                        "text": "Official LinkedIn Blog"
                    }
                }
            ]
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

def get_unposted_post(category):
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("LinkedInPosts") 
    resp = table.scan(
        IndexName="unpostedPosts",
        KeyConditionExpression=Key('hasBeenPosted').eq('false') & Key("category").eq(category),
    )
    for item in resp['Items']:
        print(item)

def generate_linkedin_payload():
    pass

def lambda_handler(event, context):
    get_unposted_post()

if __name__ == "__main__":
    linkedin_request_headers = {
        "LinkedIn-Version": "X-Restli-Protocol-Version",
        "X-Restli-Protocol-Version": "2.0.0",
        "Authorization": "Bearer " + os.environ["ACCESS_TOKEN"]
    }
    payload = generate_linkedin_payload()
    r = requests.post('https://httpbin.org/post', headers=linkedin_request_headers, data=payload)
    