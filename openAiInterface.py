import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
#MODEL = "gpt-3.5-turbo"
MODEL = "gpt-3.5-turbo-1106"
htmlPath = os.path.abspath('temp.html')
urlTouse = 'file://' + htmlPath
ROLE = "helpful assistant"

def get_completion(prompt, roleToUse=ROLE,modelToUse=MODEL):
    messages = [
        {"role": "system", "content": "You are a " + roleToUse + " designed to output JSON."},
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model=modelToUse,
        messages=messages,
        temperature=0,
        response_format={"type":"json_object"}
    )
    return response.choices[0].message