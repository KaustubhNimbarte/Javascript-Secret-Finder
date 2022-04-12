import requests
from bs4 import BeautifulSoup


#Provide full URL for Scanning
url = "https://www."
r = requests.get(url)

soup = BeautifulSoup(r.content,'html.parser')

for script in soup.find_all("script"):
    if script.attrs.get("src"):
        print(script.attrs.get("src"))
        data = requests.get(script.attrs.get("src"))
        a = data.text
        #print(a)
        if "password" in a:
            print(a)
        if "secret" in a:
            print(a)
        if "credentials" in a:
            print(a)

