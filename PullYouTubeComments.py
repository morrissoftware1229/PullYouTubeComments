#Remember to update DEVELOPER_KEY since API keys expire
#REMOVE API KEY BEFORE UPLOADING TO GITHUB
#May need to update IP Address restriction at console.cloud.google.com

#Comments here are returned as if you sorted by "Newest First" on YouTube
#Will make adjustments to return as if sorted by "Top Comments" on YouTube

import os
import googleapiclient.discovery

#Brought in to serialize returned dictionary to Output.json file
import json

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "InsertAPIKeyBeforeNextUse"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    #dictionary to hold API returns
    returnedValues = []

    #Calling the API the first time
    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId="l1LdFUFFRBQ",
        pageToken=None
    )
    response = request.execute()
    returnedValues.append(response)
    nextPageToken = response['nextPageToken']

    #Calling the API subsequent times
    #Does YouTube Data API limit to 400 comments?
    maxPage = 19
    for x in range(0, maxPage):
        request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId="l1LdFUFFRBQ",
        pageToken = nextPageToken
    )
        response = request.execute()
        returnedValues.append(response)
        if x == maxPage:
            nextPageToken=None
        else:
            nextPageToken = response['nextPageToken']
    
    listToWrite = json.dumps(returnedValues, indent=4)
    with open("Output.json", "w") as outfile:
        outfile.write(listToWrite)

    #getting comments
    #The scheme is "items" -> (now in list) "snippet" -> "topLevelComment" -> "snippet" -> "textDisplay"
    #Print the value of each snippet -> topLevelComment -> snippet -> textDisplay inside items[0]
    storedValue = ''
    for i in range(0, len(returnedValues)):
        for j in range(0, len(returnedValues[i]['items'])):
            storedValue = storedValue + (str(i * 20 + j + 1) + ". " + str(returnedValues[i]['items'][j]['snippet']['topLevelComment']['snippet']['textDisplay']) + "\n")
        #storedValue = storedValue + (str(i + 1) + ". " + str(lowerLevel[i]['snippet']['topLevelComment']['snippet']['textDisplay'])) + "\n"
    print(storedValue)
    #Not currently able to encode all of the comments for writing to ExtractedComments.txt file

    #adding this to write to Output file
    #json_object = json.dumps(response, indent=4)
    #with open("Output.json", "w") as outfile:
    #    outfile.write(json_object)

main()