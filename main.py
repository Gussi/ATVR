from ajaxscrape import scrape_all
from supersecret import *
import pymysql.cursors

#Database connection
connection = pymysql.connect(
    host=login_info["server"],
    user=login_info["user"],
    password=login_info["password"],
    db=login_info["database"],
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

products = scrape_all()
for p in products:
    #Insert the things
    insertion_query = "INSERT INTO booze (id, name, category, price, abv, volume, country) \
    VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(insertion_query, (
        p["product_id"],
        p["name"],
        p["category"],
        float(p["price"]),
        float(p["abv"]),
        float(p["volume"]),
        p["country"]
    ))
    connection.commit()
connection.close()
print("Success! (probably))
