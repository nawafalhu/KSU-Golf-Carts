import tkinter as tk
import Sing_UP
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import messagebox

Color = "#48A3BC"
Font = ('Arial', 12, 'bold')

class User:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("User Window")
        self.window.minsize(width="900", height="450")
        self.window.config(padx=10, pady=80, bg=Color)

        # Create a Tabs
        self.Tabs = ttk.Notebook(self.window)
        self.Tabs.pack(padx=10, pady=10)
        # Reserve a Golf Carts Tab
        self.Reserve_Tab = ttk.Frame(self.Tabs, width=800, height=350)
        self.Reserve_Tab.pack(fill="both", expand=1)
        self.Tabs.add(self.Reserve_Tab, text="Reserve a Golf Carts")
        # View my Reservations Tab
        self.View_Tab = ttk.Frame(self.Tabs, width=800, height=350)
        self.View_Tab.pack(fill="both", expand=1)
        self.Tabs.add(self.View_Tab, text="View my Reservations")

        treeview_reserve = ttk.Treeview(self.Reserve_Tab, columns=("College",), show="headings")
        treeview_reserve.heading("College", text="College")
        colleges = ("Business-Administration", "Architecture-and-Planning", "Computer-and-Information-Sciences", "Food-and-Agricultural-Sciences", "Engineering", "Science")
        treeview_reserve.insert("", "0", "item1", text="Item 1", values=colleges[0])
        treeview_reserve.insert("", "1", "item2", text="Item 2", values=colleges[1])
        treeview_reserve.insert("", "2", "item3", text="Item 3", values=colleges[2])
        treeview_reserve.insert("", "3", "item4", text="Item 4", values=colleges[3])
        treeview_reserve.insert("", "4", "item5", text="Item 5", values=colleges[4])
        treeview_reserve.insert("", "5", "item6", text="Item 6", values=colleges[5])
        treeview_reserve.pack(side="left", padx=10, pady=10)

        # TreeView for View my Reservations Tab
        treeview_view = ttk.Treeview(self.View_Tab, columns=("College", "Golf Cart", "Date"), show="headings")
        treeview_view.heading("College", text="College")
        treeview_view.heading("Golf Cart", text="Golf Cart")
        treeview_view.heading("Golf Cart", text="Golf Cart")
        treeview_view.heading("Date", text="Date")
        treeview_view.pack()

        # Calender
        self.calender = Calendar(self.Reserve_Tab, selectmode="day", year=2023, month=1, date=1)
        self.calender.place(x=250, y=0)

        # Time
        Time = ['8:00-8:30', '8:30-9:00', '9:00-9:30', '9:30-10:00', '10:00-10:30', '10:30-11:00', '11:00-11:30', '11:30-12:00',
                '12:00-12:30', '12:30-13:00', '13:00-13:30', '13:30-14:00']  # options
        self.Times = ttk.Combobox(self.Reserve_Tab, values=Time, width=10)  # Combobox
        self.Times.set(Time[0])

        self.Times.place(x=510, y=20)

        # Book button
        self.Button1 = tk.Button(self.Reserve_Tab, text="Reserve", width=10, height=1)
        self.Button1.place(relx=.45, rely=.80)

        # view button
        self.Button3 = tk.Button(self.View_Tab, text="Show", width=10, height=1)
        self.Button3.place(relx=.45, rely=.80)

        # Back Button
        self.buttonBack = tk.Button(self.window, text='Logout', command=self.logout)
        self.buttonBack.pack()

        self.window.mainloop()

    def logout(self):
        self.window.destroy()
        Sing_UP.sing_up()
    
    def create_tab(self, tab_name):
        tab = ttk.Frame(self.Tabs)
        self.Tabs.add(tab, text=tab_name)

User()