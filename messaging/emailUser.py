import sys
import os
import json
import smtplib, ssl



jsonConfigFile = "/home/michael/prophecy/prophecy/messaging/messaging_config.json"


# opens a file, reads all of the lines and then closes it
def parseJson():
    with open(jsonConfigFile, 'r') as j:
        contents = json.loads(j.read())
    
    senderEmail = contents["sender_email"]
    senderEmailPassword = contents["sender_email_password"]
    recipients = contents["recipients"]

    return senderEmail, senderEmailPassword, recipients


def sendEmail(sender, password, recipient, message):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = sender
    

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender, recipient, message)

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 


def main():
    # sys.path.insert(1, '/home/michael/prophecy/prophecy/code/logger')
    message = "testing"

    senderEmail, senderEmailPassword, recipients = parseJson()
    for recipient in recipients.values():
        sendEmail(senderEmail, senderEmailPassword, recipient, message)
    


if __name__ == '__main__':
    main()