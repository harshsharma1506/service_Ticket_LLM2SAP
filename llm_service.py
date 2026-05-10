import os
import json

from openai import OpenAI
from dotenv import load_dotenv

from prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyze_incident(user_input):

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.2
    )

    text = response.choices[0].message.content

    # cleanup
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)