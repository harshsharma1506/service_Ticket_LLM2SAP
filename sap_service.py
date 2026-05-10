import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()

SAP_URL = os.getenv("SAP_URL")

# Paste browser cookies here
COOKIES = {
   
    # Add more cookies if needed
}


def save_incident(payload):

    session = requests.Session()

    session.cookies.update(COOKIES)

    # STEP 1 — Fetch CSRF token
    token_response = session.get(
        SAP_URL,
        headers={
            "x-csrf-token": "fetch",
            "Accept": "application/json"
        },
        verify=False
    )

    print("TOKEN STATUS:", token_response.status_code)

    csrf_token = token_response.headers.get("x-csrf-token")

    if not csrf_token:
        return (
            token_response.status_code,
            token_response.text
        )

    # STEP 2 — Payload
    body = {

        "raw_input":
            payload.get("raw_input", ""),

        "business_summary":
            payload.get("business_summary", ""),

        "technical_summary":
            payload.get("technical_summary", ""),

        "sap_module":
            payload.get("sap_module", ""),

        "incident_type":
            payload.get("incident_type", ""),

        "priority":
            payload.get("priority", ""),

        "business_impact":
            payload.get("business_impact", ""),

        "probable_root_cause":
            payload.get("probable_root_cause", ""),

        "suggested_team":
            payload.get("suggested_team", ""),

        "sap_object":
            payload.get("sap_object", ""),

        "keywords":
            json.dumps(
                payload.get("keywords", [])
            ),

        "reproducibility":
            payload.get("reproducibility", ""),

        "debugging_steps":
            json.dumps(
                payload.get(
                    "suggested_debugging_steps",
                    []
                )
            ),

        "confidence_score":
            str(
                payload.get(
                    "confidence_score",
                    0
                )
            )
    }

    # STEP 3 — POST
    response = session.post(
        SAP_URL,
        headers={
            "x-csrf-token": csrf_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        json=body,
        verify=False
    )

    return response.status_code, response.text