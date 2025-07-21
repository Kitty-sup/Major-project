#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


import sqlite3

conn = sqlite3.connect('billing.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS product(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name TEXT,
price INTEGER
)
''')

conn.commit()
print("Table Created Successfully....")


# In[32]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS cart(
idd INTEGER PRIMARY KEY AUTOINCREMENT,
product_ id INTEGER ,
quantity INTEGER
)
''')
conn.commit()
print("Table Created Successfully....")


# In[7]:


def add_item(product_name,price):
    cursor.execute("INSERT INTO product(product_name,price) VALUES (?,?)",(product_name,price))
    conn.commit()
    print("Item added successfully...................")

add_item('bag',2000)
add_item('shoes',1100)
add_item('pen',10)


# In[9]:


def fetch_items():
    cursor.execute("SELECT * FROM product")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
fetch_items()


# In[14]:


def purchase_items(idd,quantity):
    cursor.execute("INSERT INTO cart(idd,quantity) VALUES (?,?)",(idd,quantity))
    conn.commit()
    print("Item added successfully...................")
purchase_items(1,5)
purchase_items(3,8)


# In[17]:


def show_bill():
    cursor.execute('''
    SELECT product.name,product.price,cart.quantity,
    (product.price*cart.quantity) as total

    FROM cart
    JOIN product on product.id = cart.product_id
    ''')

    items = cursor.fetchall()
    grand_total =0

    print("\n Final bill: ")
    for item in items:
        name,price,qty,total=item
        print(f"{name}| {price}x{qty} = {total}")
        grand_total += total

    print(f"Grand Total : {grand_total}")


# In[34]:


def show_bill():
    cursor.execute('''
    SELECT product.product_name, product.price, cart.quantity, 
           (product.price * cart.quantity) as total 
    FROM cart 
    JOIN product ON product.id = cart.idd
    ''')
    items = cursor.fetchall()
    grand_total = 0

    print("\n Final Bill:")
    for item in items:
        name, price, qty, total = item
        print(f"{name} | ₹{price} x {qty} = ₹{total}")
        grand_total += total

    print(f"Grand Total: ₹{grand_total}")


# In[35]:


show_bill()
conn.close


# In[ ]:




