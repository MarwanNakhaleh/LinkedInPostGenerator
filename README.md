# LinkedIn Poster
I like posting to LinkedIn and sharing my thoughts. I'm just not very consistent with it. This project is going to allow me to save future LinkedIn posts to a NoSQL table and post them regularly using a cron job.

## Post Table Schema
```json
{
    "hasBeenPosted": "", // string because GSI
    "category": "",
    "content": "",
    "linkUrl": "", // blank if no link
    "onlyFriends": false
}
```

## Limitations
The LinkedIn token provided has a two month lifespan. Therefore, I will need to update it and add its new value to the CircleCI project settings I have around May 15th, 2023.
