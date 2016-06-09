from productscraper import request
from supersecret import *
import pymysql.cursors

#Some observations: the product ID is always a zero-padded 5 digit number
base_url = "http://www.vinbudin.is/Heim/v%C3%B6rur/stoek-vara.aspx/?productid="
valid = 0

#Database connection
connection = pymysql.connect(
    host=login_info["server"],
    user=login_info["user"],
    password=login_info["password"],
    db=login_info["database"],
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

#Bruteforce the entire product range because fuck messing with dynamic content!
for i in range(1000, 100000, 5):
    urls = []
    for n in range(5):
        #10 async HTTP requests seems to be the fastest I can get this
        #This results in about 2 - 3 responses per second. Slow!
        urls.append(base_url + str(i + n).zfill(5))
    products = request(urls)
    valid += len(products)
    for p in products:
        #Insert the things
        insertion_query = "INSERT INTO booze (id, name, price, category, subcategory, description, abv, volume, country) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(insertion_query, (
            p["product_id"],
            p["name"],
            float(p["price"]),
            p["category"],
            p["subcategory"],
            p["description"],
            float(p["abv"]),
            p["volume"],
            p["country"]
        ))
        connection.commit()
    print("Scraped: {}\nValid: {}\n".format(i, valid))
connection.close()

