import requests
import smtplib
import os
from bs4 import BeautifulSoup

MY_EMAIL = os.environ['EMAIL']
PASS = os.environ['PASS']
MY_PRICE = 100
URL ='https://www.amazon.com/Ninja-Kitchen-BL770-Processor-Smoothies/dp/B00939I7EK/ref=sr_1_5?' \
     'keywords=ninja+blenders&qid=1681270349&s=home-garden&sprefix=ninja+%2Cgarden%2C194&sr=1-5'
header = {
    "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=header)

web_page_data = response.text
soup = BeautifulSoup(web_page_data, 'html.parser')

curr_float_price = float(soup.select(selector='.a-offscreen')[0].getText()[1::])
product_title = soup.find(id='productTitle').getText()

if curr_float_price <= MY_PRICE:
    message = f'{product_title} is now ${curr_float_price}\n{URL}'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f'Subject:Amazon Price alert for {product_title}\n\n{message}'
                            )
