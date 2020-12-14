from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sa@loni99",
    database="spoon"
)
mycursor=mydb.cursor()
root=Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

def quit():
        root.destroy()
        import home
Canvas1 = Canvas(root)
Canvas1.config(bg="IndianRed4")
Canvas1.pack(expand=True,fill=BOTH)
        
headingFrame1 = Frame(root,bg="black",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
headingLabel = Label(headingFrame1, text="Update records", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
labelFrame = Frame(root,bg='black')
labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
  # Book ID
lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
create = Entry(labelFrame)
create.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

# availability records
lb2 = Label(labelFrame,text="Name of Book: ", bg='black', fg='white')
lb2.place(relx=0.05,rely=0.4, relheight=0.08)
        
bookInfo2 = Entry(labelFrame)
bookInfo2.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)


lb3 = Label(labelFrame,text="Author of Book: ", bg='black', fg='white')
lb3.place(relx=0.05,rely=0.6, relheight=0.08)
        
bookInfo3 = Entry(labelFrame)
bookInfo3.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

lb4= Label(labelFrame,text="Status: ", bg='black', fg='white')
lb4.place(relx=0.05,rely=0.8, relheight=0.08)
        
bookInfo4 = Entry(labelFrame)
bookInfo4.place(relx=0.3,rely=0.8, relwidth=0.62, relheight=0.08)
def updating():   
  stat=bookInfo4.get()
  aut=bookInfo3.get()
  tit=bookInfo2.get()
  kin=create.get()
  update="Update book set Status='%s', Author='%s', Title='%s' where BID='%s'"%(stat,aut,tit,kin)
  mycursor.execute(update)
  mydb.commit()
  messagebox.showinfo("Updated","Your info has been updated")

#Submit Button
SubmitBtn = Button(root,text="UPDATE",bg='#d1ccc0', fg='black', cursor="hand2",command=updating)
SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',cursor="hand2",command=quit)
quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
        
        



        

root.mainloop()