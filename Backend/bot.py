import os
from sqlops import upload
from python-dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY","nothing")

from langchain_OpenAi import chatopen

model = chatopen(api_key, )

while True:
    user_input = input("user: ")

    if user_input.lower() == "bye":
        break
    output = model.invoke(user_input)
    print(f"bot: {output}")
    upload(user_input,output)
model.invoke("hi")