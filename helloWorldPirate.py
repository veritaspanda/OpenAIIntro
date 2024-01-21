import os
import openai
from openai import OpenAI

#openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL ="gpt-3.5-turbo"

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate!"}
  ]
)

print(completion.choices[0].message)
print(completion.choices[0].message.content)
