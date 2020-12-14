from tkinter import *
from tkinter import ttk
import mysql.connector
con=mysql.connector.connect(host="localhost",
                       user="root",
                       passwd="Sa@loni99",
                           database="spoon")
cursor=con.cursor()

root=Tk()
root.geometry("600x600")
wrapper1=LabelFrame(root, text="Deatails of Books")
wrapper2=LabelFrame(root, text="Search")


def update(rows):
    for i in rows:
        trv.insert('','end', values=i)
    
trv=ttk.Treeview(wrapper1, column=(1,2,3,4), show="headings", height="5")
trv.pack()
trv.heading(1, text="Author")
trv.heading(2, text="Title")
trv.heading(3, text="Status")
trv.heading(4, text="ISBN")


cursor.execute("select Author, Title, Status from book")
rows=cursor.fetchall()
update(rows)
def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('',0, values=i)
    

q=StringVar()
lbl=Label(wrapper2, text="BID")
lbl.pack(side=LEFT, padx=10)
ent=Entry(wrapper2, textvariable=q)
ent.pack(side=LEFT, padx=10)
def search():
    e2=q.get()
    query="select Author, Title, Status from book where BID=q.get()"
    cursor.execute(query)
    rows=cursor.fetchall()
    update(rows)
btn=Button(wrapper2, text="SEARCH", command=search)
btn.pack(side=LEFT, padx=10)
wrapper1.pack(fill="both", expand="yes", padx=20, pady=20)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=20)

root.mainloop()