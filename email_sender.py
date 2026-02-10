import smtplib
from email.message import EmailMessage
from secrets import sender_email, receiver_email, app_password
# Email details
  # NOT normal password

# Create email
msg = EmailMessage()
msg.set_content("Hello! This email is sent using Python.")
msg["Subject"] = "Python Email Test"
msg["From"] = sender_email
msg["To"] = receiver_email

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")
