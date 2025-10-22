import smtplib
from email.message import EmailMessage
import os

# Form data (you can pass these via GitHub Actions inputs)
user_name = os.getenv("USER_NAME")
user_email = os.getenv("USER_EMAIL")
user_body = os.getenv("USER_BODY")

# Sender and recipient from GitHub Secrets
sender_email = os.getenv("GMAIL_EMAIL")
sender_password = os.getenv("GMAIL_APP_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

# Compose email
msg = EmailMessage()
msg['Subject'] = f"New Contact Form Message from {user_name}"
msg['From'] = sender_email
msg['To'] = recipient_email
msg.set_content(f"Name: {user_name}\nEmail: {user_email}\nMessage:\n{user_body}")

# Send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, sender_password)
    smtp.send_message(msg)

print("Email sent successfully!")
