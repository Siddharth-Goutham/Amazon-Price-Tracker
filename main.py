from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import smtplib
import os

load_dotenv()


AMAZON_LINK=("https://www.amazon.in/Motorola-Fusion-Marshmallow-256GB-Storage/dp/B0D4JLSGBB/ref=sr_1_2_mod_"
             "primary_new?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=8-2")

headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}


response=requests.get(url=AMAZON_LINK,headers=headers)
response.raise_for_status()
website=response.text


soup=BeautifulSoup(website,"html.parser")
price=soup.find("span",class_="a-offscreen")
price_text=price.text
without_rupee=price_text.split("₹")[1]
price=float(without_rupee.replace(',',''))

raw_title=soup.find("span",class_="a-size-large product-title-word-break").text
title = " ".join(raw_title.split())


budget=17000
if float(price)<budget:
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"],port=587) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL_ADDRESS"],password=os.environ["EMAIL_PASSWORD"])
        connection.sendmail(from_addr=os.environ["EMAIL_ADDRESS"],
                            to_addrs=os.environ["EMAIL_ADDRESS"],
                            msg=f"Subject:Price Drop⚠️ \n\nThe price for '{str(title)}' in amazon has dropped its "
                                f"price to {price_text}. Go check it NOW 🚨\n {AMAZON_LINK}".encode("utf-8")
                            )

