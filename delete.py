from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
con=mysql.connector.connect(host="localhost",
                       user="root",
                       passwd="Sa@loni99", database="spoon")
cursor=con.cursor()

def quit():
        root.destroy()
        import home

def deleteBook():
    
    bid = bookInfo1.get()
    
    deleteSql = "delete from book where BID =bid"
    try:
        cursor.execute(deleteSql)
        con.commit()

        messagebox.showinfo('Success',"Book Record Deleted Successfully")

    except:
        messagebox.showinfo("Error","Please check Book ID")
    
    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)
    Canvas1.config(bg="IndianRed4")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=quit)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
delete()
