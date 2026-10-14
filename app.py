print("Akshat Jaiswal")
print("Application is starting...")
print("Security checks will be added later.")

import sqlite3
import math
from contextlib import closing

def get_all_products():
    try:
        with closing(sqlite3.connect('shop.db')) as conn:
            cursor=conn.execute('SELECT * FROM products')
            rows=cursor.fetchall()
    except sqlite3.Error as e:
        print("Database error:", e)
        return None

    return rows

def get_product_under_price(price):
    try:
        with closing(sqlite3.connect("shop.db")) as conn:
            cursor=conn.execute("SELECT * FROM products WHERE price < ?", (price,))
            rows=cursor.fetchall()
    except sqlite3.Error as e:
        print("Database error:", e)
        return None

    return rows
    
def user_input():
    while True:
        price=input("Enter a maximum price: ")
        try:
            price=float(price)
        except ValueError:
            print("Hello Sir by mistake you entered some invalid input. Please enter a valid number.")
            continue
        if not math.isfinite(price):
            print("Please enter a finite number, not NaN or infinity.")
        elif price < 0:
            print("Hello Sir by mistake you entered a negative number. Please enter a valid positive number.")
        elif price == 0:
            print("Hello Sir by mistake you entered zero. Please enter a valid positive number.")
        else:
            return (price)



price=user_input()
ans=get_product_under_price(price)
if ans is None:
    print("Sorry, a database error occurred. Please try again.")
elif not ans:
    print("No products found under ₹",price,".")
else:
    print("Products under ₹",price,":")
    for product in ans:
        print("ID: ",product[0], "|  Name: ",product[1], "|  Price: ₹",product[2],"|  Sales: ",product[3])



# res=get_all_products()
# print("Products in the database:",res)