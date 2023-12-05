import tkinter as tk
from tkinter import ttk
from DB import *
from tkinter import messagebox
import csv
import Log_IN

Color = "#48A3BC"
Font = ('Arial', 12, 'bold')

class Admin:
   def __init__(self):
      self.window = tk.Tk()
      self.window.title("Admin")
      screen_width = self.window.winfo_screenwidth()
      screen_height = self.window.winfo_screenheight()
      self.window.geometry("{}x{}".format(screen_width, screen_height))
      self.window.config(padx=10, pady=80, bg=Color)

      # Enter the golf cart plate number
      self.Golf_Plate_label = tk.Label(self.window, text="Enter The golf cart plate number: ", font=Font, bg=Color, justify=tk.CENTER)
      self.Golf_Plate_label.grid(row=0, column=0)

      self.Golf_Plate_Entry = tk.Entry(self.window, width=40, highlightthickness=1, justify=tk.CENTER, font=Font)
      self.Golf_Plate_Entry.grid(row=0, column=1, padx=10, pady=10)

      # Enter the college to which this golf cart belongs.
      Colleges = ["Business Administration", "Architecture and Planning", "Computer Sciences", "Agricultural Sciences", "Engineering", "Science"]
      self.College_label = tk.Label(self.window, text="Enter the college: ",width=40, padx=10, pady=10, bg=Color, font=Font, justify=tk.CENTER)
      self.College_label.grid(row=1, column=0)

      self.College_Combobox = ttk.Combobox(self.window, values=Colleges, width=38, justify=tk.CENTER, font=Font)
      self.College_Combobox.grid(row=1, column=1, padx=10, pady=10)

      # Create button
      self.Create_Button = tk.Button(self.window, text="Create", width=30, justify=tk.CENTER, font=Font, command=self.Added_golf)
      self.Create_Button.grid(row=2, column=1, padx=10, pady=10)

      # BackUp Button
      self.BackUp_Button = tk.Button(self.window, text="BackUp", justify=tk.CENTER, font=Font, command=self.BackUpButton)
      self.BackUp_Button.grid(row=3, column=1, padx=10, pady=10)

      # Logout Button 
      self.buttonBack = tk.Button(self.window, text='Logout', justify=tk.CENTER, font=Font, command=self.logout)
      self.buttonBack.grid(row=4, column=1, padx=10, pady=10)
      self.window.mainloop()

   def logout(self):
      self.window.update()
      self.window.destroy()
      from Sing_UP import Sign_up
      Sign_up()

   def Validation(self) :
      GolfPlate = self.Golf_Plate_Entry.get()
      College = self.College_Combobox.get()
      # Check if Golf cart exist or not
      for ID in Cursor.execute("""SELECT GolfPlate FROM GOLF""") :
         if ID[0] == GolfPlate :
            return False
      # Check if the entry empty or not digit 
      if len(GolfPlate) > 0 and len(College) > 0 and GolfPlate.isdigit() and College.isalpha:
         return True
      else :
         return False

   def Added_golf(self) :
      try :
         if self.Validation() :
            Plate = self.Golf_Plate_Entry.get()
            College = self.College_Combobox.get()
            # Store the information in the central database
            Cursor.execute(f"""INSERT INTO GOLF VALUES ("{Plate}", "{College}")""")
            Connection.commit()

            messagebox.showinfo("Done", "Golf Added Successfully")
            self.Golf_Plate_Entry.delete(0,"end")
            self.College_Combobox.delete(0, "end")
         else :
            # Can't create empty entry
            # Golf is already exist
            # Enter a digit number
            # College is not correct
            messagebox.showerror("Error", "Something wrong, Try again")
      except sqlite3.IntegrityError:
         messagebox.showerror("Error", "Something wrong, Try again")

   def BackUpButton(self) :
      # Student 
      with open("Student.csv", "w", newline='') as file :
         csv_writer = csv.writer(file)
         row = ["StudentID", "FirstName", "LastName", "UserClass", "Email", "Password", "Phone"]
         csv_writer.writerow(row)
         for student in Cursor.execute("""SELECT * FROM STUDENT""") :
            csv_writer.writerow(student)
      # Goalf
      with open("Golf.csv", "w", newline='') as file :
         csv_writer = csv.writer(file)
         row = ["GolfPlate", "College"]
         csv_writer.writerow(row)
         for Goalf in Cursor.execute("""SELECT * FROM GOLF""") :
            csv_writer.writerow(Goalf)
      # RESERVATIONS
      with open("Reservations.csv", "w", newline='') as file :
         csv_writer = csv.writer(file)
         # 112,Architecture and Planning,12,"9:30-10:00, 1/12/23"
         row = ["StudentID","College", "Golf Cart Plate", "Time", "Date"]
         csv_writer.writerow(row)
         for Reser in Cursor.execute("""SELECT * FROM RESERVATIONS""") :
            csv_writer.writerow(Reser)
      messagebox.showinfo("Done", "Backup Created")