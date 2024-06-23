import os
import time
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Insert your API key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(
    api_key=API_KEY,
)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
# Prompt Gemini to respond in certain ways using built-in instructions
instruction = "Please respond like a baby."

while True:
    print("You can exit the chatbot by typing 'q' to quit.")
    question = input("You:  ")

    # Break loop, exit program
    if question.strip() == "q" or question.strip() == "":
        break

    response = chat.send_message(instruction + question)
    print("\n")
    print(f"Bot: {response.text}")
    print("\n")
    instruction = ""
