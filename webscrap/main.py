from bs4 import BeautifulSoup
import requests
response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
y=response.text
soup=BeautifulSoup(y,"html.parser")
movies=soup.find_all(name="h3",class_="title")
movietitle=[movie.getText() for movie in movies ]
movietitle=movietitle[::-1]

with open("movie.txt",mode="w") as file:
    for movies in movietitle:
     file.write(f"{movies}\n")