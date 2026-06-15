import requests
from bs4 import BeautifulSoup

url = "https://www.mdpi.com/2075-5309/15/18/3298"
html = requests.get(url).text

soup = BeautifulSoup(
    html,
    "html.parser"
)

text = soup.get_text("\n")