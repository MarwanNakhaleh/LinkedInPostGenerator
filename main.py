import requests
import os

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

def get_unposted_post():
    pass    

def generate_linkedin_payload():
    pass

if __name__ == "__main__":
    linkedin_request_headers = {
        "LinkedIn-Version": "X-Restli-Protocol-Version",
        "X-Restli-Protocol-Version": "2.0.0",
        "Authorization": "Bearer " + os.environ["ACCESS_TOKEN"]
    }
    payload = generate_linkedin_payload()
    r = requests.post('https://httpbin.org/post', headers=linkedin_request_headers, data=payload)