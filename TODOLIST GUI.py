#!/usr/bin/env python
# coding: utf-8

# In[15]:


import sqlite3
import tkinter as tk 
from tkinter import messagebox
import getpass

conn = sqlite3.connect('To_do_list.db')
cursor = conn.cursor()


# In[16]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
id INTEGER PRIMARY KEY AUTOINCREMENt,
name TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
)
''')
conn.commit()
print("Table created successfully............")


# In[17]:


cursor.execute('''
CREATE TABLE IF NOT EXISTS task(
id INTEGER PRIMARY KEY AUTOINCREMENT,
task_name TEXT,
status TEXT
)
''')
conn.commit()
print("Table successfully created.................")
current_user = None
task_id_map = {}


# In[18]:


def sign_up():
    name = signup_name.get()
    password = signup_pass.get()

    if not name or not password:
        messagebox.showerror("Error","All fields required!")
        return
        
    try:
        cursor.execute("INSERT INTO user(name,password) VALUES (?,?)",(name,password))
        conn.commit()
        messagebox.showinfo("Success","sign-up successful! Please log in.")
        signup_name.delete(0,tk.END)
        signup_pass.delete(0,tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error","Usernam already exists!")
        


# In[19]:


def login():
    global current_user
    
    name = login_name.get()
    password = login_pass.get()

    cursor.execute("SELECT * FROM user WHERE name=? AND password=?",(name,password))
    user = cursor.fetchone()

    if user:
        current_user = user
        login_name.delete(0,tk.END)
        login_pass.delete(0,tk.END)
        show_todo_page()
        
    else:
        messagebox.showerror("Error","Invalid username or password!!!!")


# In[20]:


def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showerror("Error","Enter a task!")
        return
    cursor.execute("INSERT INTO task(task_name,status,user_id) VALUES (?,'PENDING❌',?)",(task,current_user[0]))
    conn.commit()
    task_entry.delete(0,tk.END)
    load_tasks()


# In[21]:


def load_tasks():
    task_list.delete(0,tk.END)
    task_id_map.clear()
    cursor.execute("SELECT id, task_name, status FROM task Where user_id=?",(current_user[0],))
    for index,row in enumerate(cursor.fetchall()):
        task_id, name, status = row
        task_list.insert(tk.END, f"{name} | {status}")
        task_id_map[index] = task_id


# In[22]:


def mark_complete():
    try:
        selection_index = task_list.curselection()[0]
        task_id = task_id_map[selection_index]
        cursor.execute("UPDATE task SET status = 'DONE✅' WHERE id = ?",(task_id,))
        conn.commit()
        load_tasks()
    except IndexError:
        messagebox.showerror("Error","Select a task!!!!!!!!!")


         


# In[23]:


def delete_task():
    try:
        selection_index = task_list.curselection()[0]
        task_id = task_id_map[selection_index]
        cursor.execute("DELETE FROM task WHERE id = ?",(task_id,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showerror("Error","Select a task!!!!!")


# In[24]:


def logout():
    global current_user
    current_user = None
    todo_frame.pack_forget()
    login_frame.pack()


# In[ ]:





# In[25]:


root = tk.Tk()
root.title("To Do List")
root.geometry("500x500")

login_frame = tk.Frame(root)
login_frame.pack(fill = "both", expand = True)

tk.Label(login_frame, text = "Login", font = ("Arial", 18)).pack(pady=10)
login_name = tk.Entry(login_frame, width=30)
login_name.pack(pady=5)
login_name.insert(0,"Username")
login_pass = tk.Entry(login_frame, width=30, show = "*")
login_pass.pack(pady=5)
login_pass.insert(0,"Password")

tk.Button(login_frame, text = "Login", command = login).pack(pady =10)


tk.Label(login_frame, text = "Sign Up", font = ("Arial", 18)).pack(pady=10)
signup_name = tk.Entry(login_frame, width =30)
signup_name.pack(pady =5)
signup_name.insert(0,"New Username")
signup_pass = tk.Entry(login_frame, width =30, show ="*")
signup_pass.pack(pady = 5)
signup_pass.insert(0,"New Password")

tk.Button(login_frame, text = "Sign Up", command = sign_up).pack(pady=10)


# In[26]:


todo_frame = tk.Frame(root)

tk.Label(todo_frame, text= "Your Tasks", font = ("Arial", 18)).pack(pady=10)

task_entry = tk.Entry(todo_frame,width = 30)
task_entry.pack(pady =5)

tk.Button(todo_frame, text = "Add Task", command = add_task).pack(pady=5)
tk.Button(todo_frame, text = "Mark Complete", command = mark_complete).pack(pady=5)
tk.Button(todo_frame, text="Delete Task", command=delete_task).pack(pady=5)
tk.Button(todo_frame, text="Logout", command=logout).pack(pady=5)

task_list = tk.Listbox(todo_frame, width=50, height=15)
task_list.pack(pady=10)

def show_todo_page():
    login_frame.pack_forget()
    todo_frame.pack(fill="both", expand =True)
    load_tasks()
    
root.mainloop()


# In[ ]:





# In[ ]:




