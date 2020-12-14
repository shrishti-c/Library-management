from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import mysql.connector
con=mysql.connector.connect(host="localhost",
                       user="root",
                       passwd="Sa@loni99", database="spoon")
cursor=con.cursor()

from tkinter import messagebox
def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root) 
    Canvas1.config(bg="IndianRed4")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    Label(labelFrame, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    def quit():
        root.destroy()
        import home
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
    try:
        cursor.execute("Select * from book")
        row=cursor.fetchall()
        for i in row:
            Label(labelFrame,text="%-10s%-40s%-30s%-20s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=quit)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08) 
    root.mainloop()
View()