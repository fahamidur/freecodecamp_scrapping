import requests
from bs4 import BeautifulSoup
import time
h_url = 'https://www.freecodecamp.org/news/tag/software-development/'
html_text = requests.get(h_url).text
soup = BeautifulSoup(html_text, 'lxml')

print("Extracting resources.Please Wait.....")
item_count = 0
time.sleep(3)

a = soup.find_all('h2',class_="post-card-title")
f = open("Extracted Files/soft_dev.txt", "a")
for a in a:
    x = a.find('a')
    title = x.text.strip()
    y = str(x)
    url = "freecodecamp.com"
    for y in y:
        if y == '>':
            break
        else:
            url = url+y
    url = url.replace("<a href=","")
    url = url.replace('"','')
    stra = f"""Title-{item_count + 1}: {title} \n Url: '{url}' \n"""
    f.write(stra)
    f.write('\n')
    item_count+=1
print(f"{item_count} Links has been extracted")
print("file is being saved in 'Extracted Files' folder")
f.close()
input()
