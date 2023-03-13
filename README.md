# LinkedIn Poster
I like posting to LinkedIn and sharing my thoughts. I'm just not very consistent with it. This project is going to allow me to save future LinkedIn posts to a NoSQL table and post them regularly using a cron job.

## Post Table Schema
```json
{
    "hasBeenPosted": false,
    "content": "",
    "linkUrl": "", // blank if no link
    "onlyFriends": false
}
```