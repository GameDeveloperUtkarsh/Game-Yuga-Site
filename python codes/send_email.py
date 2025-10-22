# send_email.py
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(name, email, body):
    sender = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")  # where to send mail (your email)

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = f"Message from {name}"

    text = f"From: {name}\nEmail: {email}\n\nMessage:\n{body}"
    msg.attach(MIMEText(text, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)

    print("✅ Email sent successfully!")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python send_email.py <name> <email> <body>")
        sys.exit(1)

    _, name, email, body = sys.argv
    send_mail(name, email, body)
