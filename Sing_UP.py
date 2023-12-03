import tkinter
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import hashlib
from DB import * 
import re
import logging
from datetime import datetime

Color = "#48A3BC"
Font = ('Arial', 12, 'bold')

logging.basicConfig(filename='logging.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

class Sign_up:
    def __init__(self):
        self.window = tkinter.Tk()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry("{}x{}".format(screen_width, screen_height))
        self.window.title('KSU Golf Carts Sing UP Window')
        self.window.configure(bg=Color) # AAAAAA
        
        # Sign up frame
        self.Frame = tkinter.LabelFrame(self.window, bg=Color, text='Sign up Window', width=screen_width - 200, height=screen_height - 200, font=Font)
        
        #First name label and entry
        self.fname_label = tkinter.Label(self.Frame, bg=Color, text="First Name", font=Font)
        self.fname_label.grid(row=4, column=0, pady=50)
        self.fname_entry = tkinter.Entry(self.Frame, width=40, font=Font)
        self.fname_entry.grid(row=4, column=1, pady=50)

        #Last name label and entry
        self.lname_label = tkinter.Label(self.Frame, bg=Color, text="Last Name", font=Font)
        self.lname_label.grid(row=6, column=0, pady=10)
        self.lname_entry = tkinter.Entry(self.Frame, width=40, font=Font)
        self.lname_entry.grid(row=6, column=1, pady=10)
        
        # user class
        self.user_class_label = tkinter.Label(self.Frame, bg=Color, text="User Class", font=Font)
        self.user_class_label.grid(column=0, row=8, pady=10)
        self.class_var = tkinter.StringVar()
        self.user_class = ttk.Combobox(self.Frame,textvariable=self.class_var,width=38,height=10,font=Font)
        self.user_class['values']=['Student','Faculty','Employee']
        self.user_class.grid(row=8,column=1,pady=10)

        # student id
        self.stu_id_label = tkinter.Label(self.Frame, bg=Color, text="ID", font=Font)
        self.stu_id_label.grid(column=0, row=10, pady=10)
        self.stu_id_entry = tkinter.Entry(self.Frame, width=40, font=Font)
        self.stu_id_entry.grid(column=1, row=10, pady=10)

        # password
        self.password_label = tkinter.Label(self.Frame, bg=Color, text="Password", font=Font)
        self.password_label.grid(column=0, row=12, pady=10)
        self.password_entry = tkinter.Entry(self.Frame, width=40, font=Font, show='*')
        self.password_entry.grid(column=1, row=12, pady=10)

        #email
        self.email_label = tkinter.Label(self.Frame, bg=Color, text="Email", font=Font)
        self.email_label.grid(column=0, row=14, pady=10)
        self.email_entry = tkinter.Entry(self.Frame, width=40, font=Font)
        self.email_entry.grid(column=1, row=14, pady=10)
        
        # Phone number
        self.phone_label = tkinter.Label(self.Frame, bg=Color, text="Phone Number", font=Font)
        self.phone_label.grid(column=0, row=16, pady=10)
        self.phone_entry = tkinter.Entry(self.Frame, width=40, font=Font)
        self.phone_entry.grid(column=1, row=16, pady=10)

        # Submit Button
        self.submit_bt = tkinter.Button(self.Frame, text="Submit", width=15, height=1, font=Font, command=self.Validation)
        self.submit_bt.grid(column=0, row=20, pady=50, padx=10)
        
        # Login button
        self.login_bt = tkinter.Button(self.Frame, text="Login", width=15, height=1, font=Font, command=self.open_login)
        self.login_bt.grid(column=3, row=20,pady=50)
        
        
        self.Frame.pack(fill='both', padx=50, pady=50)
    
    def checkIfAlreadyThere(self):
        for Row in Cursor.execute("""SELECT * FROM STUDENT""") :
            if Row[0] == self.stu_id_entry.get() or Row[4] == self.email_entry.get() or Row[6] == self.phone_entry.get():
                return False
        return True

    def Validation(self):
        StudentID = self.stu_id_entry.get()
        FirstName = self.fname_entry.get()
        LastName = self.lname_entry.get()
        UserClass = self.class_var.get()
        Email = self.email_entry.get()
        Password = self.password_entry.get()
        Phone = self.phone_entry.get()

        # check the entry 
        check = len(FirstName) > 0 and FirstName.isalpha()
        if check is True :
            check = len(LastName) > 0 and LastName.isalpha()
            if check is True :
                check = (UserClass == "Student" and len(StudentID) == 10 and StudentID.isdecimal()) or (UserClass == "Faculty" or UserClass == "Employee" and len(StudentID) == 6 and StudentID.isdecimal())
                if check is True :
                    check = len(Password) >= 6 and Password.isalnum()
                    if check is True :
                        check = re.match("^[a-zA-Z0-9-_]+@[a-z]+\.[a-z]+\.[a-z]{1,2}$", Email) and Email.endswith("@ksu.edu.sa")
                        if check is True:
                            check = len(Phone) == 10 and Phone.startswith("05") and Phone.isdecimal()
                            if check is True :
                                check = UserClass == "Student" or UserClass == "Employee" or UserClass == "Faculty"                                   
                                if check is True :
                                    if self.checkIfAlreadyThere() :
                                        Password = hashlib.sha256(self.password_entry.get().encode()).hexdigest()

                                        Cursor.execute("""INSERT INTO STUDENT (StudentID, FirstName, LastName, UserClass, Email, Password, Phone) 
                                        VALUES (?,?,?,?,?,?,?)""", (StudentID, FirstName, LastName, UserClass, Email, Password, Phone))
                                        Connection.commit()
                                        tkinter.messagebox.showinfo("Welcome", "Account created successfully")
                                        logging.info(f"Create Account ID: {StudentID}")
                                        self.fname_entry.delete(0, "end")
                                        self.lname_entry.delete(0, "end")
                                        self.stu_id_entry.delete(0, "end")
                                        self.email_entry.delete(0, "end")
                                        self.password_entry.delete(0, "end")
                                        self.phone_entry.delete(0, "end")
                                        self.user_class.delete(0, "end")
                                        self.window.destroy()
                                        from Log_IN import Login_W
                                        Login_W(self.class_var.get())
                                    else :
                                        tkinter.messagebox.showerror("Error", "The User is already exist")
                                else :
                                    tkinter.messagebox.showerror("Error", "Select a correct User class")
                            else :
                                tkinter.messagebox.showerror("Error", "check your phone")
                        else :
                            tkinter.messagebox.showerror("Error", "Your Email must end with @ksu.edu.sa")
                    else :
                        tkinter.messagebox.showerror("Error", "Check your Password")
                else :
                    tkinter.messagebox.showerror("Error", "ID must be 10 digit for Student and 6 for Faculty and Employee and a number")
            else :
                tkinter.messagebox.showerror("Error", "Last name must be string and not empty")
        else :
            tkinter.messagebox.showerror("Error", "First name must be string and not empty")

    def open_login(self):
        self.window.update()
        self.window.destroy()
        from Log_IN import Login_W
        Login_W()
        
if __name__ == "__main__":
    mywindow = Sign_up()
    mywindow.window.mainloop()