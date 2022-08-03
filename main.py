import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input the GitHub username: ")
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_pic = soup.find('img', {'alt' : 'Avatar'})['src']
print(profile_pic)


