import requests
import random
import string
import time

def generate_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "1secmail.com"
    email = f"{name}@{domain}"
    return name, domain, email

def check_inbox(login, domain):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    response = requests.get(url)
    print("Checking inbox URL:", url)
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    try:
        return response.json()
    except Exception as e:
        print("Error parsing JSON:", e)
        return []

def read_email(login, domain, mail_id):
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={mail_id}"
    response = requests.get(url)
    return response.json()

def main():
    login, domain, email = generate_email()
    print("Generated email:", email)

    print("Waiting for emails...")
    for _ in range(10):  # check 10 times
        inbox = check_inbox(login, domain)
        if inbox and isinstance(inbox, list):
            if inbox:
                print("Emails received!")
                for mail in inbox:
                    mail_id = mail['id']
                    email_content = read_email(login, domain, mail_id)
                    print("From:", email_content['from'])
                    print("Subject:", email_content['subject'])
                    print("Body:", email_content['textBody'])
                break  # exit loop once emails are read
            else:
                print("No emails yet, checking again in 5 seconds...")
                time.sleep(5)
        else:
            print("Invalid or empty response received.")
            time.sleep(5)

if __name__ == "__main__":
    main()
