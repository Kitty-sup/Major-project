#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
book_name TEXT,
qty INTEGER
)
''')

conn.commit()
print("Table Created Successfully....")


# In[2]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
idd INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT ,
password INTEGER
)
''')
conn.commit()
print("Table Created Successfully....")


# In[3]:


def sign_up():
    name = input("Please enter username:")
    password = getpass.getpass("Password for your future login:")

    try:
        cursor.execute("INSERT INTO user(name,password) VALUES (?,?)",(name,password))
        conn.commit()
        print("SIGN_UP IS DONE✅")
    except:
        print("ERROR")


# In[4]:


def login():
    global current_user
    name = input("PLEASE ENTER YOUR USERNAME: ")
    password = getpass.getpass("PASSWORD:")
    
    cursor.execute("SELECT * FROM user WHERE name=? AND password=?",(name,password))
    user = cursor.fetchone()
    if user:
        print(f"Welcome {user[1]}!!!!!")
        return user
    else:
        print("Invalid account number or Pin...!")
        return None


# In[10]:


def add_book(book_name,qty):
    cursor.execute("INSERT INTO books(book_name,qty) VALUES (?,?)",(book_name,qty))
    conn.commit()
    print("book added successfully...................")
add_book("kitty is being cute",3)


# In[6]:


def fetch_books():
    cursor.execute("SELECT * FROM books")
    rows=cursor.fetchall()
    for row in rows:
        print(row)


# In[19]:


def issue_book():
    title =  input("Enter book title to issue: ")
    
    cursor.execute("SELECT * FROM books WHERE book_name=?",(book_name,))
    book = cursor.fetchone()
    
    if book and book[2] > 0:
        cursor.execute("UPDATE books SET qty = qty - 1 WHERE book_name = ? ",(book_name,))
        conn.commit()
        print(f"'{book_name}' issued.\n")
    else:
        print("Book not available")
   


# In[8]:


def return_book():
    book_name = input("Enter book to return: ")
    cursor.execute("SELECT * FROM books where book_name = ?",(book_name,))
    book = cursor.fetchone()
    if book:
        cursor.execute("UPDATE books SET qty = qty + 1 WHERE book_name = ?",( book_name,))
    else:
        cursor.execute("INSERT INTO books(book_name,qty) VALUES (?,1)",(book_name,))
    conn.commit()
    print(f"'{book_name}' RETURNED.\n")


# In[20]:


def menu():
    print("--------library menu-------")
    print("1. view books")
    print("2. Add books")
    print("3. Issue book")
    print("4. Return book")
    print("5. Logout")

while True:
    print("----Welcome to our library------")
    print("1. Ragister")
    print("2. Login")
    print("3. exit")
    choice = input("Choose: ")

    if choice == '1':
        sign_up()
    elif choice == '2':
        current_user = login()
        if current_user:
            while True:
                menu()
                ch = input("Choose: ")
                if ch == '1':
                    fetch_books()
                elif ch=='2':
                    book_name = input("Enter book name: ")
                    qty = int(input("Enter quantity: "))
                    add_book(book_name,qty)
                elif ch=='3':
                    issue_book()
                elif ch=='4':
                    return_book()
                elif ch=='5':
                    print("logout")
                    current_user= None
                    break
                else:
                    print("invalid choice")
    elif choice=='3':
        print("Thanks for visting,byeeeeeeee")
        break
    else:
        print("Wrong choice")

conn.close()
        
    


# In[ ]:




