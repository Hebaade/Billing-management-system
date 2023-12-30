from tkinter import*

root=Tk()
root.resizable(False,False)

###
lbl_address=Label(root,text='Welcome to Billing system',font=('tohama',20),fg='#D21312')
lbl_address.grid(row=0,column=0,padx=80,pady=25)
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

###

frame=Frame(root)
frame.place(rely=0.5,relx=0.5,anchor='center')

###
font=("tohama",15)

def login():
    root.destroy()
    import login

def signup():
    root.destroy()
    import signUp

###

btn_sign=Button(frame,text='Sign Up',padx=15,pady=5,font=font,command=signup,fg="#fff",bg='black')
btn_login=Button(frame,text='Login',padx=25,pady=5,font=font,command=login,fg="#fff",bg='black')

###
btn_sign.grid(row=0,column=0,pady=20)
btn_login.grid(row=1,column=0)

root.mainloop()
