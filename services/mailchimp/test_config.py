import os
from mailchimp_marketing import Client

MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY")
assert MAILCHIMP_API_KEY, "MAILCHIMP_API_KEY is not set"

# https://us11.admin.mailchimp.com/audience/settings?id=727858
MAILCHIMP_SERVER = "us11"

mailchimp = Client()
mailchimp.set_config({
    "api_key": MAILCHIMP_API_KEY,
    "server": MAILCHIMP_SERVER
})

response = mailchimp.ping.get()
print(response)