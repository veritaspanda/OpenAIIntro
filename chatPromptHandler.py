import pandas as pd
import json
import openAiInterface
import updateIndexHtml
# import singlePageFlask

#openAiRole = "UX/UI developer"
#promptExample = "Make a single page website that shows off different neat javascript features for drop-downs and things to display information. The website should be an HTML file with embedded javascript and CSS."

def scrape_and_reformat(html = "<html><body> ... generated html string ... </body></html>"):
    updateIndexHtml.updateHtml(html=html)
    #singlePageFlask.setHtml(html=html)
    return

openAiRole = input("Enter AI Role (Act as a...): ")
prompt = input("Enter Prompt: ")
promptResponse = openAiInterface.get_json_formatted(prompt,openAiRole)
jsonResponse = json.loads(promptResponse.content)
print("Role: " + promptResponse.role)

for jsonItem in jsonResponse:
    if jsonItem.lower() == "response":
        try:
            print(jsonResponse["response"])
        except KeyError:
            print("KeyError Occured.")
        
    elif jsonItem.lower() == "html":
        try:
            scrape_and_reformat(jsonResponse[jsonItem])
            #singlePageFlask.catch_all("/")
            # singlePageFlask.index()
        except KeyError:
            print("KeyError Occured.")
    elif jsonItem.lower() == "website":
        try:
            scrape_and_reformat(jsonResponse[jsonItem])
            #singlePageFlask.catch_all("/")
            # singlePageFlask.index()
        except KeyError:
            print("KeyError Occured.")
    else:
        try:
            print("jsonItem: " + jsonItem)
            print(jsonResponse[jsonItem])
        except KeyError:
            print("KeyError Occured.")

