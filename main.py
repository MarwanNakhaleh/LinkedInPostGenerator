import os
import logging
import json

import boto3
from boto3.dynamodb.conditions import Key

import requests

from random_selection import get_random_category, get_unposted_post

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

def generate_linkedin_payload(post):
    has_link = None
    try:
        has_link = post["linkUrl"]
    except KeyError:
        pass
    try:
        only_friends = post["onlyFriends"]
    except KeyError:
        pass
    if has_link:
        new_post = post_with_link
        new_post["specificContent"]["com.linkedin.ugc.ShareContent"]
    else:
        new_post = post_without_link
    new_post["specificContent"]["com.linkedin.ugc.ShareContent"]["shareCommentary"]["text"] = post["content"]
    return new_post
    
def post_to_linkedin(payload):
    linkedin_request_headers = {
        "LinkedIn-Version": "X-Restli-Protocol-Version",
        "X-Restli-Protocol-Version": "2.0.0",
        "Authorization": "Bearer " + os.environ["ACCESS_TOKEN"]
    }
    r = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=linkedin_request_headers, data=json.dumps(payload))
    print(r.json())
    print(r.status_code)

def lambda_handler(event, context):
    category = get_random_category()
    if category != "":
        post = get_unposted_post("story")
    payload = generate_linkedin_payload(post)
    post_to_linkedin(payload)

if __name__ == "__main__":
    linkedin_request_headers = {
        "LinkedIn-Version": "X-Restli-Protocol-Version",
        "X-Restli-Protocol-Version": "2.0.0",
        "Authorization": "Bearer " + os.environ["ACCESS_TOKEN"]
    }
    payload = generate_linkedin_payload()
    r = requests.post('https://api.linkedin.com/v2/ugcPosts', headers=linkedin_request_headers, data=payload)
    