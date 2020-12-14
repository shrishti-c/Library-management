from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
con=mysql.connector.connect(host="localhost",
                       user="root",
                       passwd="Sa@loni99", database="spoon")
cursor=con.cursor()
#cursor.execute("create database spoon")
#cursor.execute("create table book (BID int,Title varchar(250), Author varchar(250),Status varchar(250))")

from tkinter import messagebox
root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")
root.configure(bg="IndianRed4")
same=True
n=0.25

def search_book():
    root.destroy()
    import search

def add_book():
    root.destroy()
    import add

def view_book():
    root.destroy()
    import view

def delete_book():
    root.destroy()
    import delete

def update_book():
    root.destroy()
    import update

    

headingFrame1 = Frame(root,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n SPOONSHOT Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Search Book", fg='white', bg="#c48b95",bd=5, cursor="hand2",command=search_book)
btn1.place(relx=0.23,rely=0.4, relwidth=0.55,relheight=0.1)

btn2 = Button(root,text="Add Book Details", fg='white', bg="black", cursor="hand2",command=add_book)
btn2.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Delete Book",bg='black', fg='white', cursor="hand2",command=delete_book)
btn3.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="Update Book details",bg='black', fg='white', cursor="hand2",command=update_book)
btn4.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="View Book List",bg='black', fg='white', cursor="hand2",command=view_book)
btn5.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

root.mainloop()