import datetime
import time
import requests
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import json

load_dotenv('./config.env')

# Enviorn layer for security 
API_URL = os.getenv('API_URL')
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')

print("Starting...")
# API
url = API_URL
response = requests.get(url)

# Check for errors if it's connected
print("Connecting...")
if response.status_code == 200:
    data = json.loads(response.text)
else:
    print(f"Error: {response.status_code}")

# Bin data  
result = data

# List Comprehension to filter out each list.
filter = [data_st for data_st in result if data_st["status"] == "red"]
data_list = filter

# Dispaly full lenght of values in the list
def convert():
    list_lenght = []
    for i in range(len(data_list)):
        text = f'{data_list[i]["street"]} {data_list[i]["number"]}'
        list_lenght.append(text)
    return list_lenght

# Store the value 
option = convert()
check_option = option

# Convert into string
string = ', '.join(str(e) for e in check_option)

# Checking wich value is right
def check():
    if check_option == []:
        option_text = "Šiukšlinės šiuo metu visos tuščios."
    elif len(check_option) <= 1:
        option_text = f'Šioje gatvėje: {string}, šiukšlės neišveštos.'            
    else:
        option_text = f'Šiose gatvėse: {string}, šiukšlės neišveštos.'
    return option_text


# Return value
email_message = check()
print(email_message)

# OOP
# Email
class Email:
     # Inistial value
    def __init__(self, apiData):
        self.apiData = apiData

    # Email connection
    def send_email(self):
       subject = "Šiukšlių dėžės"
       body = self.apiData

       # Client credentials
       sender_email = SENDER_EMAIL
       receiver_email = RECEIVER_EMAIL
       email_passowrd = EMAIL_PASSWORD

       # Header   
       message = EmailMessage()
       message["From"] = sender_email
       message["To"] = receiver_email
       message["Subject"] = subject

       # Body    
       html = f"""
       <html>
           <body>
               <h1>{subject}</h1>
               <p>{body}</p>
           </body>
       </html>
       """
       # Convert to html   
       message.add_alternative(html, subtype="html")

       
       print("Sending email...")
       # Security
       context = ssl.create_default_context()       
       # Socket layer for security
       with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=context) as server:
           server.login(sender_email, email_passowrd)
           server.sendmail(sender_email, receiver_email, message.as_string())

# Return
email = Email(email_message)

# Interval
# 1 hour 60 * 60
# 30 minut 30 * 60
# 3 days interval 3*24*60*60
print("Loading to send...")
while True:
    email.send_email()
    time.sleep(3*24*60*60)
    print("Success!")
