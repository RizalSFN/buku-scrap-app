import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import mysql.connector

# KONEKSI DB BRAY
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_buku_scrap"
)

cursor = conn.cursor()

my_url = 'https://www.goodreads.com/list/show/83612.NY_Times_Fiction_Best_Sellers_2015'
# my_url = 'https://www.goodreads.com/search?q=golden&qid='

# opening dan connection to website
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# graps the product
tds = page_soup.find_all("td", {"width":"100%","valign":"top"})
image = page_soup.find_all("tr", {"itemtype": "http://schema.org/Book"})

# file = "databuku.csv"

# header = "title,author,rating,score \n"

# f = open(file, "w")
# f.write(header)

for i, td in enumerate(tds):
    try:
        books = td.a.select("span") if td.a else []
        if books:
            title = books[0].text
        else:
            title = "Unknown"

        authors = td.div.select("a") if td.div else []
        author = authors[0].text if authors else "Unknown"

        ratings = td.find_all("span", {"class":"minirating"})
        rating = ratings[0].text.strip().replace(",",".") if ratings else "Unknown"

        scores = td.find_all("div", {"style":"margin-top: 5px"})
        score = scores[0].span.a.text.strip().replace("score:","").replace(",",".").replace(" ","") if scores else "0"
        
        # SIMPAN KE DATABASE BRAYYY
        cursor.execute(
            """
            INSERT INTO buku (title, authors, ratings, scores)
            VALUES (%s, %s, %s, %s)
            """, (title, author, rating, score)
        )

        print(f"{i+1}. [OK] {title} oleh {author} (Rating : {rating} | Skor : {score}")

    except Exception as e:
        print(f"{i+1}. [GAGAL] Error : {e}")
        
conn.commit()
        
for i, img in enumerate(image):
    try:
        images = img.find_all("img", {"class":"bookCover"})
        image = images[0].get('src') if images else "-"
        
        # SIMPAN KE DATABASE BRAYYY
        cursor.execute(
            """
            UPDATE buku SET images = %s WHERE id = %s
            """, (image, i+1)
        )

        print(f"{i+1}. [OK] Gambar berhasil ditambahkan")

    except Exception as e:
        print(f"{i+1}. [GAGAL] Error : {e}")

# print(ratings)
# print(score)

# Cetak semua hasil
# for book in book_data:
#     print("=================================================")
#     print("Judul: " + book["title"])
#     print("Penulis: " + book["author"])
#     print("Rating: " + book["rating"])
#     print("Score: " + book["score"])
# f.write(title.replace(",","") + ", " + author + ", " + rating + ", " + score +"\n")
# f.close()

conn.commit()
cursor.close()
conn.close()
