import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, app_password
# Email details
  # NOT normal password

def send_email(receiver_email: str, subject: str, content: str):
    """Send an email to the specified receiver."""
# Create email
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    print("Email sent successfully!")

