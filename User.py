import tkinter as tk
import Sing_UP
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox
from DB import *
import logging
from datetime import datetime

Color = "#48A3BC"
Font = ('Arial', 12, 'bold')


class UserW:
    def __init__(self, ID, User_Class):
        self.window = tk.Tk()
        self.window.title("User Window")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry("{}x{}".format(screen_width, screen_height))
        self.window.config(padx=10, pady=80, bg=Color)

        self.StudentID = ID
        self.UserClass = User_Class[0]

        # Create a Tabs
        self.Tabs = ttk.Notebook(self.window, width=800, height=350)
        self.Tabs.pack(padx=20, pady=20)
        # Reserve a Golf Carts Tab
        self.Reserve_Tab = ttk.Frame(self.Tabs, width=900, height=450)
        self.Reserve_Tab.pack(fill="both", expand=1)
        self.Tabs.add(self.Reserve_Tab, text="Reserve a Golf Carts")
        # View my Reservations Tab
        self.View_Tab = ttk.Frame(self.Tabs, width=900, height=450)
        self.View_Tab.pack(fill="both", expand=1)
        self.Tabs.add(self.View_Tab, text="View my Reservations")

        self.Treeview_reserve = ttk.Treeview(self.Reserve_Tab)
        
        # Define our columns
        self.Treeview_reserve['columns'] = ('College', 'Golf Cart Plate')
        
        # Create Columns
        self.Treeview_reserve.column("#0", width=0)
        self.Treeview_reserve.column("College", anchor='w', width=150)
        self.Treeview_reserve.column("Golf Cart Plate", anchor='w', width=150)

        # Create Heading
        self.Treeview_reserve.heading("#0", text="")
        self.Treeview_reserve.heading("College", text="College", anchor='w')
        self.Treeview_reserve.heading("Golf Cart Plate", text="Golf Cart Plate", anchor='w')

        colleges = ('Business Administration', "Architecture and Planning", "Computer Sciences", "Agricultural Sciences", "Engineering", "Science")
        
        # insert Data
        id = 0
        for Row in Cursor.execute("""SELECT * FROM GOLF""") :
            self.Treeview_reserve.insert('', index='end', iid=id, text='', values=(Row[1], Row[0]))
            id += 1
        self.Treeview_reserve.pack(side="left", padx=10, pady=10)

        # TreeView for View my Reservations Tab
        self.Treeview_view = ttk.Treeview(self.View_Tab)
        self.Treeview_view['columns'] = ("College", "Golf Cart Plate", "Time","Date")
        self.Treeview_view.column("#0", width=0)
        self.Treeview_view.column("College", width=150, anchor='w')
        self.Treeview_view.column("Golf Cart Plate", width=150, anchor='center')
        self.Treeview_view.column("Time", width=150, anchor='w')
        self.Treeview_view.column("Date", width=150, anchor='w')

        # heading
        self.Treeview_view.heading("#0", text="")
        self.Treeview_view.heading("College", text="College")
        self.Treeview_view.heading("Golf Cart Plate", text="Golf Cart Plate")
        self.Treeview_view.heading("Time", text="Time")
        self.Treeview_view.heading("Date", text="Date")

        # Calender
        self.calender = Calendar(self.Reserve_Tab, selectmode="day", year=2023, month=1, date=1)
        self.calender.place(x=350, y=80)

        # Time
        Student_Time = ['8:00-8:30', '8:30-9:00', '9:00-9:30', '9:30-10:00', '10:00-10:30', '10:30-11:00', '11:00-11:30', '11:30-12:00',
                '12:00-12:30', '12:30-13:00', '13:00-13:30', '13:30-14:00']
        Faculty_Time = ['8:00-9:00', '9:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00']
        Employee_Time = ['8:00-9:30', '9:30-11:00', '11:00-12:30', '12:30-14:00']

        self.Times = ttk.Combobox(self.Reserve_Tab, width=10)
        if self.UserClass == 'Faculty' :
            self.Times['values'] = Faculty_Time
        elif self.UserClass == 'Employee' :
            self.Times['values'] = Employee_Time
        elif self.UserClass == 'Student':
            self.Times['values'] = Student_Time
            
        self.Times.set(Student_Time[0])
        self.Times.place(x=610, y=80)

        # Select Date Button
        self.Select_Button = tk.Button(self.Reserve_Tab, text='Select Date', width=10, height=1, command=self.Date)
        self.Select_Button.place(relx=.60, rely=.90)

        # Reserve button
        self.Reserve_Button = tk.Button(self.Reserve_Tab, text="Reserve", width=10, height=1, command=self.Reserve)
        self.Reserve_Button.place(relx=.15, rely=.90)

        # view button
        self.View_Button = tk.Button(self.View_Tab, text="Show", width=10, height=1, command=self.ViewMyReservations)
        self.View_Button.place(relx=.45, rely=.80)

        # Back Button
        self.buttonBack = tk.Button(self.window, text='Logout', width=10, height=1, command=self.logout)
        self.buttonBack.pack()

        self.window.mainloop()

    def logout(self):
        self.window.destroy()
        Sing_UP.Sign_up()

    def Date(self):
        self.Dates = f"{self.calender.get_date()}"
        self.DateTime = f"{self.Times.get()}"
        messagebox.showinfo("Done", "Date Selected Successfully")        

    def Reserve(self):
            try:
                self.Details = self.Treeview_reserve.item(self.Treeview_reserve.focus())
                self.College_Selected = self.Details.get("values")[0]
                self.Golf_Selected = self.Details.get("values")[1]
                # Check if the Golf cart is reserved or not
                for Row in Cursor.execute("""SELECT * FROM RESERVATIONS""") :
                     if Row[2] == self.Golf_Selected and Row[3] == self.DateTime and Row[4] == self.Dates:
                        messagebox.showerror("Error", "The Golf Cart is Reserved")
                        return False
                     
                Cursor.execute("""INSERT INTO RESERVATIONS (StudentID, COLLEGE, GolfPlate, Time, Date)
                                VALUES (?, ?, ?, ?, ?)""", (self.StudentID, self.College_Selected, self.Golf_Selected, self.DateTime, self.Dates))
                Connection.commit()
                messagebox.showinfo('Done', 'Your Reservation is Complete')
                logging.info(f'Reservation is Complete ID: {self.StudentID} , College: {self.College_Selected}, Golf Plate: {self.Golf_Selected}, Reserve Time: {self.DateTime}, Reserve Date: {self.Dates}')                  

            except AttributeError:
                messagebox.showerror("Error", "Select Date First")
                return False
            except IndexError :
                messagebox.showerror('Error', 'Please Select a Golf Cart')
                return False
            except sqlite3.IntegrityError :
                messagebox.showerror("Error", "Select Another Date and Golf Cart")
                return False
    def ViewMyReservations(self):
        count = 1
        for Reserve in Cursor.execute(f"""SELECT * FROM RESERVATIONS WHERE StudentID == '{self.StudentID}' """) :
            self.Treeview_view.insert('', index='end', iid=count, text='', values=(Reserve[1], Reserve[2], Reserve[3], Reserve[4]))
            count += 1
        self.Treeview_view.pack(padx=10, pady=10)
