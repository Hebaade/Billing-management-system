from tkinter import*
import sqlite3
from tkinter import messagebox
import Database_funs


root=Tk()
root.resizable(False,False)
root.title('Login')
Database_funs.logintable()

####

width=500
height=400
def center():
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    x = int((screenwidth - width)/2)
    y = int((screenheight - height)/2)
    root.geometry(f"{width}x{height}+{x}+{y}")
center()

####
arrow=PhotoImage(file="left-arrow.png")
def back():
    root.destroy()
    import first_fr
arrow_btn=Button(root,image=arrow,width=20,relief=FLAT,command=back)
arrow_btn.place(x=5,y=5)
####
def login():
    flag = False
    username = entry_username.get()
    password = entry_password.get()
    result=Database_funs.showAllUsers()
    for row in result:
        print(row[0])
        if row[0] == username and row[1] == password:
            flag = True
            root.destroy()
            import mainF
    if flag == False:
        messagebox.askokcancel('System', 'Incorrect username or password')

###

font=("tohama",15)
lbl_address=Label(root,text='Log in',font=('tohama',30),fg='#D21312',padx=180)
frame=Frame(root,pady=20)
frame.place(rely=0.5,relx=0.5,anchor='center')

###

lbl_username=Label(frame,text='UserName:',font=font,fg='#070A52')
lbl_password=Label(frame,text="password:",padx=5,pady=10,font=font,fg='#070A52')

###

entry_username=Entry(frame,width=30,relief=RAISED,textvariable=StringVar())
entry_password=Entry(frame,width=30,relief=RAISED,textvariable=StringVar())

###

lbl_address.grid(row=0,column=0,padx=10,pady=30)
lbl_username.grid(row=0,column=0,padx=5,pady=10)
entry_username.grid(row=0,column=1)
entry_password.grid(row=1,column=1)
lbl_password.grid(row=1,column=0,padx=5,pady=10)

###

btn_signup=Button(frame,text="Login",pady=10,padx=20,font=('tohama',13),command=login,bg='#000',fg='#fff')
btn_signup.grid(row=4,column=0,columnspan=2,pady=13)

root.mainloop()