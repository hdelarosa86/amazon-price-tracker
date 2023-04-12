import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get('https://www.amazon.com/Ninja-Kitchen-BL770-Processor-Smoothies/dp/B00939I7EK/ref=sr_1_5?'
                        'keywords=ninja+blenders&qid=1681270349&s=home-garden&sprefix=ninja+%2Cgarden%2C194&sr=1-5',
                        headers=header)

web_page_data = response.text

soup = BeautifulSoup(web_page_data, 'html.parser')
print(soup)
