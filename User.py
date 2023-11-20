import tkinter as tk
import Sing_UP
from tkinter import ttk

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


        self.buttonBack = tk.Button(self.window, text='Logout', command=self.logout)
        self.buttonBack.grid(row=0, column=0)

        self.window.mainloop()

    def logout(self):
        self.window.destroy()
        Sing_UP.Sing_UP()
    
    def create_tab(self, tab_name):
        tab = ttk.Frame(self.Tabs)
        self.Tabs.add(tab, text=tab_name)

User()