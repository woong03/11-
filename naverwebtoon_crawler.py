import requests
from bs4 import BeautifulSoup

title = [[], [], [], [], [], [], []]
title_today = []

url= "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
day = soup.find_all("div", attrs={"class":"col "})
today = soup.find_all("div", attrs={"class":"col col_selected"})
d = 0
for i in day:
  aday = i.find_all("ul")
  for j in aday:
    cartoons = j.find_all("a", attrs={"class":"title"})
    for cartoon in cartoons:
      title[d].append(cartoon.get_text())
  d += 1
    
for k in today:
  atoday = k.find_all("ul")
  for u in atoday:
    tcartoons = u.find_all("a", attrs={"class":"title"})
    for tcartoon in tcartoons:
      title_today.append(tcartoon.get_text())

print(f"today:{title_today}")
for i in range(6):
  print(title[i])
