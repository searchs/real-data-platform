from bs4 import BeautifulSoup
import requests
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s", "%m-%d-%Y %H:%M:%S"
)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler("scraper.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

url = "https://www.immoscout24.ch/en/house/buy/city-bern?r=7&map=1"

logger.info("Navigating to domain with Properties to extract buttons")
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
buttons = soup.findAll("button")
logger.info("Collected all buttons on page")
p = []
for item in buttons:
    if len(item) <= 3 & len(item.text) != 0:
        print(item)
        p.append(item)

if p:
    # print(p.pop())
    logger.info(f"\n\tPopping first item {p.pop()}\n")
    last_page = p.pop()
else:
    last_page = "1"

print(last_page)
logger.info("\n\tProcessing now complete. Next!\n")
