# uvicorn main:app --reload
import os
import re
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

from fastapi import FastAPI

MAILCHIMP_API_KEY = "test"  # os.getenv("MAILCHIMP_API_KEY")
assert MAILCHIMP_API_KEY, "MAILCHIMP_API_KEY is not set"

# Make a regular expression for validating an Email
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

app = FastAPI()


def is_valid_email(email):
    """
    Validate an email address

    Args:
        email (str): Email to validate

    Returns:
        bool: True if valid, False otherwise
    """
    return re.fullmatch(EMAIL_REGEX, email)
    

def subscribe(email):
    """
    Subscribe an email to a list in Mailchimp

    Args:
        email (str): Email to subscribe

    Returns:
        dict: Response from Mailchimp

    Raises:
        ValueError: Email not valid or Mailchimp API error
    """

    if not is_valid_email(email):
        raise ValueError("Email is not valid")
    
    try:
        client = MailchimpMarketing.Client()
        client.set_config({
            "api_key": MAILCHIMP_API_KEY,
            "server": "YOUR_SERVER_PREFIX"
        })

        response = client.lists.add_list_member(
            "list_id",
            {
                "email_address": email,
                "status": "unsubscribed"
            }
        )
        print(response)
    except ApiClientError as error:
        raise ValueError(error.text)


@app.post("/subscribe")
async def subscribe_email(email: str):
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
            -d '{\"email\": \"test@test.com\"}'
    """
    try:
        # subscribe(email)
        return {"status": "success"}
    except ValueError as error:
        return {"status": "error", "message": str(error)}
