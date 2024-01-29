from tkinter import *
import sqlite3
root=Tk()
lbl=Label(root,text="Hospital", font=("Arial Bold", 50))
lbl.place(x=200, y=0)
root.geometry("500x1500")


conn=sqlite3.connect("gender_database.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS employee(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    uname           TEXT,
    adr             TEXT,
    rl              TEXT,
    slr             INT
                         
)""")
conn.commit()
conn.close()


label_username=Label(root,text="Username", font=("Arial Bold",20))
label_username.place(x=0,y=90)

label_address=Label(root,text="Address", font=("Arial Bold",20))
label_address.place(x=0,y=140)

label_role=Label(root,text="Role", font=("Arial Bold",20))
label_role.place(x=0,y=190)

label_password=Label(root,text="Salary", font=("Arial Bold",20))
label_password.place(x=0,y=240)

label_delete=Label(root,text="Delete_Record", font=("Arial Bold",20))
label_delete.place(x=0,y=370)


username=Entry(root,width=30)
username.place(x=170,y=100,height=30)

address=Entry(root,width=30)
address.place(x=170,y=150,height=30)


role=Entry(root,width=30)
role.place(x=170,y=200,height=30)

salary=Entry(root,width=30)
salary.place(x=170,y=250,height=30)

delete_box=Entry(root,width=30)
delete_box.place(x=210,y=370,height=30)



def add():
    conn=sqlite3.connect("gender_database.db")
    c=conn.cursor()
    c.execute("INSERT INTO employee(uname,adr,rl,slr) VALUES(?,?,?,?)",
             (username.get(),address.get(),role.get(),salary.get()))
    conn.commit()
    conn.close()
    username.delete(0, END)
    address.delete(0,END)
    role.delete(0, END)
    salary.delete(0,END)



def retrieve():
    conn=sqlite3.connect("gender_database.db")
    c=conn.cursor()
    #execute a SELECT query to retrive all records from the "employee"b table
    c.execute("SELECT * FROM employee")
    #fetch all records return by the query
    records=c.fetchall()
    print_record=' '
    for record in records:
        print_record += str(record[0])+ ' ' + str(record[1]) + ' ' + str(record[2]) + ' ' + str(record[3]) + '' + str(record[4]) + "\n"
    query_label=Label (root, text=print_record)
    query_label.place(x=0, y=450)
       


btn_add=Button(root,text="Add", font=("Arial Bold", 20), command=add)
btn_add.place(x=0,y=300)

btn_retrieve=Button(root,text="Retrieve", font=("Arial Bold", 20), command=retrieve)
btn_retrieve.place(x=100,y=300)

btn_delete=Button(root,text="Delete", font=("Arial Bold", 20))
btn_delete.place(x=250,y=410)

root.mainloop()