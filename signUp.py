from tkinter import*
from tkinter import messagebox
import Database_funs
import sqlite3
root=Tk()
root.title('Sign Up')
root.resizable(False,False)
font=("tohama",15)
lbl_address=Label(root,text='Sign Up',font=('tohama',30),fg='#D21312')
###
frame=Frame(root)
frame.place(rely=0.5,relx=0.5,anchor='center')
###
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

def signup():
    flag = False
    username = entry_username.get()
    password = entry_password.get()
    conformed_password = entry_confirmpass.get()
    result =Database_funs.showAllUsers()
    for row in result:
        if row[0] == username:
          flag = True
    if flag == True:
        messagebox.askokcancel('System', 'user name alread taken')
        return
    if flag == False:
        if password == conformed_password:
            Database_funs.addUser(username, password)
            root.destroy()
            import mainF
        else:
            messagebox.askokcancel('System', 'you must write the same password in two fields')
            entry_confirmpass.delete(0, END)
            entry_password.delete(0, END)
###
lbl_username=Label(frame,text='UserName:',font=font,fg='#070A52')
lbl_password=Label(frame,text="password:",padx=5,pady=10,font=font,fg='#070A52')
lbl_confirm=Label(frame,text="Confirm Password:",font=("tohama",14),fg='#070A52')
###
entry_username=Entry(frame,width=30,relief=RAISED)
entry_password=Entry(frame,width=30,relief=RAISED)
entry_confirmpass=Entry(frame,width=30,relief=RAISED)
###
lbl_username.grid(row=0,column=0,padx=5,pady=7)
entry_username.grid(row=0,column=1)
entry_password.grid(row=1,column=1)
entry_confirmpass.grid(row=3,column=1,padx=5,pady=7)
lbl_confirm.grid(row=3,column=0)
lbl_password.grid(row=1,column=0,padx=5,pady=7)
lbl_address.grid(row=0,column=0,padx=180,pady=20)
###
btn_signup=Button(frame,text="Sign Up",pady=10,padx=20,font=('tohama',13),command=signup,bg='#000',fg='#fff')
btn_signup.grid(row=4,column=0,columnspan=2,pady=13)
root.mainloop()