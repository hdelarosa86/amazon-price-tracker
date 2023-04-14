import requests
import smtplib
import os
from bs4 import BeautifulSoup

MY_EMAIL = os.environ['EMAIL']
PASS = os.environ['PASS']

header = {

    "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get('https://www.amazon.com/Ninja-Kitchen-BL770-Processor-Smoothies/dp/B00939I7EK/ref=sr_1_5?'
                        'keywords=ninja+blenders&qid=1681270349&s=home-garden&sprefix=ninja+%2Cgarden%2C194&sr=1-5',
                        headers=header)

web_page_data = response.text

soup = BeautifulSoup(web_page_data, 'html.parser')

price = float(soup.select(selector='.a-offscreen')[0].getText()[1::])

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASS)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg='Subject:Sample\n\nThis is the body of the email'
                        )

