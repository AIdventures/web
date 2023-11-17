"""
Runs a FastAPI server to subscribe emails to a Mailchimp list

Info:
> https://shorturl.at/sMRVW

Run the server with:
> uvicorn main:app --reload
"""
import os
import re
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY")
assert MAILCHIMP_API_KEY, "MAILCHIMP_API_KEY is not set"
MAILCHIMP_SERVER = "us11"
MAILCHIMP_AUDIENCE_ID = "34d62a2625"

# Make a regular expression for validating an Email
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

app = FastAPI()

# Replace the list of allowed origins with your localhost URL
origins = [
    "http://localhost",
    "http://localhost:4321",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify specific HTTP methods if needed
    allow_headers=["*"],  # You can specify specific HTTP headers if needed
)


def _is_valid_email(email):
    """
    Validate an email address

    Args:
        email (str): Email to validate

    Returns:
        bool: True if valid, False otherwise
    """
    return re.fullmatch(EMAIL_REGEX, email)
    

def _subscribe_email(email):
    """
    Subscribe an email to a list in Mailchimp

    Args:
        email (str): Email to subscribe

    Returns:
        dict: Response from Mailchimp

    Raises:
        ValueError: Email not valid or Mailchimp API error

    Information:
        https://mailchimp.com/developer/marketing/api/list-members/add-member-to-list/
    """

    if not _is_valid_email(email):
        raise ValueError("Email is not valid")
    
    try:
        client = MailchimpMarketing.Client()
        client.set_config({
            "api_key": MAILCHIMP_API_KEY,
            "server": MAILCHIMP_SERVER
        })

        response = client.lists.add_list_member(
            MAILCHIMP_AUDIENCE_ID,
            {
                "email_address": email,
                "status": "subscribed"
            }
        )
        print(response)
    except ApiClientError as error:
        raise ValueError(error.text)


# https://stackoverflow.com/a/59947209
class RequestData(BaseModel):
    email: str


@app.post("/subscribe")
async def subscribe(data: RequestData):
    """
    Subscribe an email to a list in Mailchimp

    Args:
        email (str): Email to subscribe

    Returns:
        dict: Response with the status of the request

    Examples:
        >>> curl -X POST "http://localhost:8000/subscribe" \
            -H "accept: application/json" \
            -H "Content-Type: application/json" \
            -d '{"email": "mario@tester.com"}'
    """
    try:
        _subscribe_email(data.email)
        return {"status": "success"}
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
