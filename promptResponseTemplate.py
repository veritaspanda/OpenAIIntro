import openai
import os
import pandas as pd
import time
import json


openai.api_key = os.getenv("OPENAI_API_KEY")
#MODEL = "gpt-3.5-turbo"
MODEL = "gpt-3.5-turbo-1106"

def get_completion(prompt, modelToUse=MODEL):
    messages = [
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model=modelToUse,
        messages=messages,
        temperature=0,
        response_format={"type":"json_object"}
    )
    return response.choices[0].message

prompt = input("Enter Prompt: ")
promptResponse = get_completion(prompt)
jsonResponse = json.loads(promptResponse.content)
print("Role: " + promptResponse.role)
#print(jsonResponse["response"])
responseType = "response"
lenResponse = len(jsonResponse)

for jsonItem in jsonResponse:
    if jsonItem == "response":
        try:
            print(jsonResponse["response"])
        except KeyError:
            print("KeyError Occured.")
        
    elif jsonItem == "html":
        try:
            print(jsonResponse["html"])
        except KeyError:
            print("KeyError Occured.")
    else:
        try:
            print("jsonItem: " + jsonItem)
            print(jsonResponse[jsonItem])
        except KeyError:
            print("KeyError Occured.")

