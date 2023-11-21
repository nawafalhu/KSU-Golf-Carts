import tkinter  as tk
import tkinter.messagebox
from DB import *
import hashlib

Color = "#48A3BC"
Font = ('Arial', 12, 'bold')

class Login_W:
    def __init__(self):
        self.Login = tk.Tk()
        self.Login.title("Login")
        self.Login.minsize(width="600", height="450")
        self.Login.config(padx=10, pady=80, bg=Color)
        self.UserID = tk.Label(self.Login, text="ID",font=Font, bg=Color, justify=tk.CENTER)
        self.UserID.grid(row=0, column=0)
        self.IDText = tk.Entry(self.Login, width=40,highlightthickness=1,  justify=tk.CENTER, font=Font)
        self.IDText.grid(row=0, column=1, padx=10, pady=10)
        self.Password = tk.Label(self.Login, text="Password",font=Font, bg=Color, justify=tk.CENTER)
        self.Password.grid(row=1, column=0)
        self.passwordText = tk.Entry(self.Login, show="*", width=40, highlightthickness=1, justify=tk.CENTER, font=Font)
        self.passwordText.grid(row=1, column=1, padx=10, pady=10)
        self.buttonLogin = tk.Button(self.Login, text="Login", justify=tk.CENTER, font=Font, command=self.go_admin)
        self.buttonLogin.grid(row=2, column=1, padx=10, pady=10)
        self.buttonBack = tk.Button(self.Login, text='Signup',justify=tk.CENTER, font=Font, command=self.go_signup)
        self.buttonBack.grid(row=3, column=1, padx=10, pady=10)
        self.Login.mainloop()

    def go_admin(self):
        if self.IDText.get()=="Admin" and self.passwordText.get()=="123456":
            self.Login.destroy()
            from Admin import Admin
            Admin()
        else:
            self.correctness()
    def correctness(self):
        if len(self.IDText.get()) != 10 and len(self.IDText.get()) != 6:
            tk.messagebox.showerror('Error', "The ID must be equal to 10 or 6 digits")
        elif (self.IDText.get().isdecimal()==False):
            tk.messagebox.showerror('Error', "The ID must be digits")
        elif len (self.passwordText.get()) < 6:
            tk.messagebox.showerror('Error', 'Password must be 6 or more letters, numbers')
        else:
            self.accept()
    def accept(self):
        IDlist=[]
        for i in Cursor.execute("""SELECT * FROM STUDENT"""):
            IDlist.append(i[1])
        if self.IDText.get() not in IDlist:
            tk.messagebox.showerror('Error','The ID not found')
            return
        else:
            pas = hashlib.sha256(self.Password.get().encode()).hexdigest()
            pasDB = ''
            for x in Cursor.execute(f"""SELECT * FROM STUDENT WHERE SID = {self.IDText.get()}"""):
                pasDB = x[2]
            if pas != pasDB:
                tk.messagebox.showerror("Error", "Password is Incorrect")
                return
            else:
                self.go_user()
    def go_user(self):
        self.Login.destroy()
        from User import User
        User()


    def go_signup(self):
        self.Login.destroy()
        from Sing_UP import Sign_Up_Window
        Sign_Up_Window()


