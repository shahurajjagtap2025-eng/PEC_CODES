
import smtplib
from email.message import EmailMessage

# Email details
sender_email = "your_email@gmail.com"
receiver_email = "receiver@example.com"
app_password = "your_16_digit_app_password"

# Create email
msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = sender_email
msg["To"] = receiver_email
msg.set_content("Hello! This email was sent using Python SMTP.")

try:
    # Connect to Gmail SMTP server
    with smtplib.SMTP_SSL(
        "smtp.gmail.com", 465
    ) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)

    print("Email sent successfully!")

except Exception as e:
    print("Error sending email:", e)
