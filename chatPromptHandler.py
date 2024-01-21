import pandas as pd
import json
import openAiInterface
import updateIndexHtml
#import singlePageFlask

#openAiRole = "UX/UI developer"

def scrape_and_reformat(html = "<html><body> ... generated html string ... </body></html>"):
    updateIndexHtml.updateHtml(html=html)
    #singlePageFlask.setHtml(html=html)
    return

openAiRole = input("Enter AI Role (Act as a...): ")
prompt = input("Enter Prompt: ")
promptResponse = openAiInterface.get_completion(prompt,openAiRole)
jsonResponse = json.loads(promptResponse.content)
print("Role: " + promptResponse.role)

for jsonItem in jsonResponse:
    if jsonItem == "response":
        try:
            print(jsonResponse["response"])
        except KeyError:
            print("KeyError Occured.")
        
    elif jsonItem == "html":
        try:
            #print(jsonResponse["html"])
            #openHtmlInBrowser.openHtml(jsonResponse[jsonItem])
            #basicFlaskHtmlPage.scrape_and_reformat(jsonResponse[jsonItem])
            scrape_and_reformat(jsonResponse[jsonItem])
            #singlePageFlask.catch_all("/")
        except KeyError:
            print("KeyError Occured.")
    else:
        try:
            print("jsonItem: " + jsonItem)
            print(jsonResponse[jsonItem])
        except KeyError:
            print("KeyError Occured.")

