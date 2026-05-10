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

MODELS = [
    "openai/gpt-oss-120b:free",
    "openrouter/free"
]

def analyze_incident(user_input):

    last_error = None

    for model_name in MODELS:

        try:

            response = client.chat.completions.create(
                model=model_name,
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
                temperature=0.1
            )

            text = response.choices[0].message.content

            text = text.replace("```json", "")
            text = text.replace("```", "")

            return json.loads(text)

        except Exception as e:
            last_error = str(e)

    return {
        "business_summary": "LLM processing failed",
        "technical_summary": last_error,
        "sap_module": "UNKNOWN",
        "incident_type": "UNKNOWN",
        "priority": "Low",
        "business_impact": "Unable to analyze incident",
        "probable_root_cause": "LLM provider failure",
        "suggested_team": "UNKNOWN",
        "sap_object": "UNKNOWN",
        "keywords": [],
        "reproducibility": "Unknown",
        "suggested_debugging_steps": [],
        "confidence_score": 0.0
    }