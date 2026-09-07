import os
import aiosmtplib
from email.message import EmailMessage

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")


@app.get("/")
def home():
    return {
        "message": "Farm application backend is running!"
    }


@app.get("/test-email")
async def test_email():

    message = EmailMessage()

    message["From"] = EMAIL_ADDRESS
    message["To"] = "yinthong0323@gmail.com"
    message["Subject"] = "Farm Application Test Email"

    message.set_content(
        """
Hello!

This is a test email from your Farm application backend.

If you received this email, Gmail SMTP is working successfully.

FarmTab
"""
    )

    await aiosmtplib.send(
        message,
        hostname="smtp.gmail.com",
        port=587,
        start_tls=True,
        username=EMAIL_ADDRESS,
        password=EMAIL_APP_PASSWORD,
    )

    return {
        "message": "Test email sent successfully!"
    }
