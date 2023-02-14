#Remember to update DEVELOPER_KEY since API keys expire
#REMOVE API KEY BEFORE UPLOADING TO GITHUB
#May need to update IP Address restriction at console.cloud.google.com

#Comments here are returned as if you sorted by "Newest First" on YouTube
#Will make adjustments to return as if sorted by "Top Comments" on YouTube

import os
import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "InsertAPIKeyBeforeNextUse"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId="l1LdFUFFRBQ"
    )
    response = request.execute()

    print(response)

main()