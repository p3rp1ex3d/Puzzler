from tkinter import *
import mysql.connector

con=mysql.connector.connect(user='root',password='mysql',host='127.0.0.1',database='puzzler')
cur = con.cursor()

def check():
    global root
    name=username.get()
    
    if name.isalpha():
        name=name.lower()
        cur.execute("select username from scoreboard;")
        e=cur.fetchall()
        
        cur.execute("insert into scoreboard values(%s,%s,%s,%s);",(len(e)+1,name,0,0))
        con.commit()
        over()
    else:
        print("username can only have letters")
        usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)
        loginButton = Button(root, text="Login", command=check).grid(row=4, column=0)

    
    

root = Tk()  
root.geometry('400x150')  
root.title('Login')

username = StringVar()
usernameLabel = Label(root, text="User Name").grid(row=0, column=0)
usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)
loginButton = Button(root, text="Login", command=check).grid(row=4, column=0)

def over():
    root.destroy()

root.mainloop()



