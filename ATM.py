#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:


#for basic understanding
import sqlite3


conn = sqlite3.connect('students.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS stu (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')

conn.commit()
print("Table created successfully.")



# In[ ]:


def insert_student(name, age, grade):
    cursor.execute("INSERT INTO stu (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("Student inserted successfully.")

# Sample inserts
insert_student('Riya', 20, 'A')
insert_student('Divyank', 22, 'B')



# In[ ]:


def fetch_students(): 
    cursor.execute("SELECT * FROM stu")  # corrected table name
    rows = cursor.fetchall()
    for row in rows:
        print(row)

fetch_students()


# In[ ]:


def update_student(student_id, new_name, new_age, new_grade):
    cursor.execute("UPDATE stu SET name=?, age=?, grade=? WHERE id=?", (new_name, new_age, new_grade, student_id))
    conn.commit()
    print("Student updated successfully.")

update_student(1, 'Riya Sharma', 21, 'A+')


# In[ ]:


def delete_student(student_id):
    cursor.execute("DELETE FROM stu WHERE id=?", (student_id,))
    conn.commit()
    print("Student deleted successfully.")

delete_student(2)


# In[ ]:


conn.close()
print("Database connection closed.")


# In[ ]:


#major project on atm


# In[1]:


import sqlite3

conn = sqlite3.connect('atm.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS atmm(
account_no INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
pin TEXT,
balance REAL
)
''')

conn.commit()
print("Table Created Successfully....")


# In[2]:


def insert_account(name,pin,balance):
    cursor.execute("INSERT INTO atmm(name,pin,balance) VALUES (?,?,?)",(name,pin,balance))
    conn.commit()
    print("Account inserted successfully......")

insert_account('palak','1234',2000)
insert_account('athira','1235',5000)
insert_account('anshika','1236',3000)


# In[3]:


def login(account_no,pin):
    cursor.execute("SELECT * FROM atmm WHERE account_no=? AND pin=?",(account_no,pin))
    user = cursor.fetchone()
    if user:
        print(f"Welcome {user[1]}!!!!!")
        return user
    else:
        print("Invalid account number or Pin...!")
        return None


# In[4]:


def check_balance(account_no):
    cursor.execute("SELECT * FROM atmm WHERE account_no=?",(account_no,))
    balance=cursor.fetchone()[0]
    print(f"Your Balance is {balance}!!!!!!")


# In[5]:


def fetch_account():
    cursor.execute("SELECT * FROM atmm")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
        
fetch_account()


# In[6]:


def deposit(account_no,amount):
    cursor.execute("UPDATE atmm SET balance = balance + ? WHERE account_no = ?", (amount, account_no))
    conn.commit()
    print(f"{amount} deposited successfully......")


# In[7]:


def withdraw(account_no,amount):
    cursor.execute("SELECT balance FROM atmm WHERE account_no=?",(account_no,))
    current_balance = cursor.fetchone()[0]

    if amount > current_balance:
        print("Insufficiant balance!")
    else:
        cursor.execute("UPDATE atmm SET balance = balance - ? WHERE account_no = ?",(amount,account_no))
        conn.commit()
        print(f"{amount} withdraw successfully.....")


# In[8]:


def atm_menu():
    print("---------------welcome to python ATM-------------------")
    account_no = int(input("Enter  account number: "))
    pin = input("Enter PIN: ")

    user = login(account_no,pin)
    if not user:
        return
    while True:
        print("\n----menu----")
        print("1. CHECK BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. EXIT")
        choice = input("ENTER YOUR CHOICE: ")

        if choice == '1':
            check_balance(account_no)
        elif choice == '2':
            amt = float(input("Enter amount to deposit: "))
            deposit(account_no,amt)
        elif choice == '3':
            amt = float(input("Enter amount to withdraw: "))
            withdraw(account_no,amt)
        elif choice == '4':
            print("Thank youuuuuu")
            break
        else:
            print("Invalid choice.")
        


# In[9]:


atm_menu()
conn.close


# In[ ]:




