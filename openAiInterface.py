import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
#MODEL = "gpt-3.5-turbo"
MODEL = "gpt-3.5-turbo-1106"
ROLE = "helpful assistant"

def get_completion(prompt, roleToUse=ROLE,modelToUse=MODEL):
    messages = [
        {"role": "system", "content": "You are a " + roleToUse + " designed to deliver what is prompted in the best and most complete way possible and format result output as JSON."},
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model=modelToUse,
        messages=messages,
        temperature=0,
        response_format={"type":"json_object"}
    )
    return response.choices[0].message


def get_json_formatted(prompt, roleToUse=ROLE,modelToUse=MODEL):
    messages = [
        {"role": "system", "content": "You are a " + roleToUse + " designed to deliver what is prompted in the best and most complete way possible and format result output as JSON."},
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model=modelToUse,
        messages=messages,
        temperature=0,
        response_format={"type":"json_object"}
    )
    return response.choices[0].message

def get_openai_result(prompt, roleToUse=ROLE,modelToUse=MODEL):
    messages = [
        {"role": "system", "content": "You are a " + roleToUse + " designed to deliver what is prompted in the best and most complete way possible."},
        {"role": "user", "content": prompt}
    ]
    response = openai.chat.completions.create(
        model=modelToUse,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message