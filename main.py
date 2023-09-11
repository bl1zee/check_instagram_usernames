from bs4 import BeautifulSoup  
import requests

website = 'https://www.vulnhub.com/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())