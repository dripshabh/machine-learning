import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

content = input("User: ")
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": content}
  ]
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')

messages = [
    {"role": "system", "content": "You're a recruiter who asks tough interview questions"}
]