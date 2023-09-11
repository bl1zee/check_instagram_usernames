from bs4 import BeautifulSoup  
import requests

website = 'https://www.instagram.com/accounts/emailsignup/'
params = {'emailOrPhone':'test.sadfadsfsdafgsdfgsdfg@gmail.com', 'fullName':'test', 'username':'paabloo_mtn', 'password':'Adfer:1@ddfD'}
response = requests.post(website, data = params)
content = response.text

soup = BeautifulSoup(content, 'lxml')

box = soup.find_all('div', class_="_aaht")
filter = box.find('p').get_text()

print(filter)