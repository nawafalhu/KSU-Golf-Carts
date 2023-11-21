import tkinter
from tkinter import ttk
import sqlite3
import tkinter.messagebox
import hashlib


class sing_up:
    def __init__(self):
        self.main_window = tkinter.Tk()
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        self.main_window.geometry("{}x{}".format(screen_width, screen_height))
        self.main_window.title('KSU Golf Carts Sing UP Window')
        self.main_window.configure(bg='#48A3BC')
        self.main_frame = tkinter.LabelFrame(self.main_window, bg='#89b7c4', text='شاشة التسجيل',
                                             width=screen_width - 200, height=screen_height - 200, font=('Arial', 16))
        self.fname_label = tkinter.Label(self.main_frame, bg='#89b7c4', text='الأسم الأول', font=('Arial', 12, 'bold'))
        self.fname_entry = tkinter.Entry(self.main_frame, width=40, font=('Arial', 12, 'bold'))
        self.lname_label = tkinter.Label(self.main_frame, bg='#89b7c4', text='الأسم الأخير', font=('Arial', 12, 'bold'))
        self.lname_entry = tkinter.Entry(self.main_frame, width=40, font=('Arial', 12, 'bold'))
        self.user_class_label = tkinter.Label(self.main_frame, bg='#89b7c4', text='الفئة', font=('Arial', 12, 'bold'))
        self.class_var = tkinter.StringVar()
        self.user_class = ttk.Combobox(self.main_frame,textvariable=self.class_var,width=38,height=10,font=('Arial', 12, 'bold'))
        self.user_class['values']=['Student','Faculty','Employee']
        self.stu_id_label = tkinter.Label(self.main_frame, bg='#89b7c4', text='رقم الطالب', font=('Arial', 12, 'bold'))
        self.stu_id_entry = tkinter.Entry(self.main_frame, width=40, font=('Arial', 12, 'bold'))
        self.password_label = tkinter.Label(self.main_frame, bg='#89b7c4', text='كلمة المرور',
                                            font=('Arial', 12, 'bold'))
        self.password_entry = tkinter.Entry(self.main_frame, width=40, font=('Arial', 12, 'bold'), show='*')
        self.email_label = tkinter.Label(self.main_frame, bg='#89b7c4', text='الأيميل', font=('Arial', 12, 'bold'))
        self.email_entry = tkinter.Entry(self.main_frame, width=40, font=('Arial', 12, 'bold'))
        self.phone_label = tkinter.Label(self.main_frame, bg='#89b7c4', text='رقم الجوال', font=('Arial', 12, 'bold'))
        self.phone_entry = tkinter.Entry(self.main_frame, width=40, font=('Arial', 12, 'bold'))
        self.submit_bt = tkinter.Button(self.main_frame, text='إنشاء', width=15, height=2, font=('Arial', 12, 'bold'),
                                        command=self.submit_table).grid(column=0, row=20, pady=50)
        self.login_bt = tkinter.Button(self.main_frame, text='تسجيل الدخول ', width=15, height=2,
                                       font=('Arial', 12, 'bold')).grid(column=3, row=20,pady=50)
        self.main_frame.pack(fill='both', padx=50, pady=50)
        self.fname_label.grid(row=4, column=0, pady=50)
        self.fname_entry.grid(row=4, column=1, pady=50)
        self.lname_label.grid(row=6, column=0, pady=10)
        self.lname_entry.grid(row=6, column=1, pady=10)
        self.stu_id_label.grid(column=0, row=10, pady=10)
        self.stu_id_entry.grid(column=1, row=10, pady=10)
        self.password_label.grid(column=0, row=12, pady=10)
        self.password_entry.grid(column=1, row=12, pady=10)
        self.email_label.grid(column=0, row=14, pady=10)
        self.email_entry.grid(column=1, row=14, pady=10)
        self.phone_label.grid(column=0, row=16, pady=10)
        self.phone_entry.grid(column=1, row=16, pady=10)
        self.user_class_label.grid(column=0, row=8, pady=10)
        self.user_class.grid(row=8,column=1,pady=10)
        self.user_privilage_var = tkinter.StringVar()
        self.user_privilage_label = tkinter.Label(self.main_frame, bg='#89b7c4', text='الصلاحيات',
                                                  font=('Arial', 12, 'bold'))
        self.pri_1 = tkinter.Radiobutton(self.main_frame, bg='#89b7c4', text='Admin', value='Admin',
                                         font=('Arial', 12, 'bold'), variable=self.user_privilage_var)
        self.pri_2 = tkinter.Radiobutton(self.main_frame, bg='#89b7c4', text='User', value='User',
                                         font=('Arial', 12, 'bold'), variable=self.user_privilage_var)
        self.user_privilage_var.set('User')
        self.user_privilage_label.grid(row=18, column=0, pady=20)
        self.pri_1.grid(row=18, column=1, pady=20)
        self.pri_2.grid(row=18, column=2, pady=20)
        self.main_window.mainloop()

    def submit_table(self):
        try:
            connect_db = sqlite3.connect('D:\\Final_Project\\KSU_Golf_Carts\\Project_db.db')
            listOfTables = connect_db.execute(
                """SELECT Name FROM sqlite_schema WHERE type='table'
                AND Name='students_info'; """).fetchall()

            if listOfTables == []:
                connect_db.execute('''CREATE TABLE students_info
                            (student_id INT PRIMARY KEY NOT NULL,
                            first_name TEXT NOT NULL,
                            last_name TEXT  NULL,
                            user_class TEXT NULL,
                            Email TEXT NULL,
                            password TEXT NULL,
                            phone TEXT NULL,
                            privilage_type Text);''')
            else:
                if len((self.phone_entry.get())) != 10:
                    tkinter.messagebox.showerror('Error', 'رقم التليفون يجب ان يكون 10 ارقام و يبدأ ب05')
                elif ((self.phone_entry.get()).startswith('05')) == False:
                    tkinter.messagebox.showerror('Error', 'رقم التليفون يجب ان  يبدأ ب05')
                elif len((self.password_entry.get())) < 6:
                    tkinter.messagebox.showerror('Error', 'كلمة المرور يجب أن أن تكون من 6 حروف أو أرقام أو أكثر')
                elif self.is_int(self.stu_id_entry.get()) == False:
                    tkinter.messagebox.showerror('Error', 'رقم الطالب يجب أن يكون أرقام و لا يحتوي على حروف.')
                elif self.class_var.get() == 'Student' and len(self.stu_id_entry.get()) != 10:
                    tkinter.messagebox.showerror('Error', 'رقم الطالب يجب أن يكون 10 أرقام مع حالة الطالب')
                elif self.class_var.get() in ('Faculty', 'Employee') and len(self.stu_id_entry.get()) != 6:
                    tkinter.messagebox.showerror('Error', 'رقم الطالب يجب أن يكون 6 أرقام مع حالة الكلية أو الموظف')
                elif (self.email_entry.get()).endswith('@ksu.edu.sa') == False:
                    tkinter.messagebox.showerror('Error', 'قم بإدخال الأيميل بطريقة صحيحة@ksu.edu.sa')
                else:
                    data_insert_query = '''INSERT INTO students_info (student_id,first_name,last_name,user_class,Email,password,phone,privilage_type) \
                        VALUES (?,?,?,?,?,?,?,?)'''
                    data_insert_tuple = (
                    self.stu_id_entry.get(), self.fname_entry.get(), self.lname_entry.get(), self.class_var.get(),
                    self.email_entry.get(), hashlib.sha256(self.password_entry.get().encode()).hexdigest(),
                    self.phone_entry.get(), self.user_privilage_var.get())
                    connect_db.execute(data_insert_query, data_insert_tuple)
                    connect_db.commit()
                    connect_db.close()
                    tkinter.messagebox.showinfo('Insert', 'تم أضافة الطالب بنجاح')
        except sqlite3.IntegrityError:
            tkinter.messagebox.showerror('Error', 'رقم الطالب مسجل بالفعل؟')
            self.stu_id_entry.delete(0, 'end')
        except:
            connect_db = sqlite3.connect('D:\\Final_Project\\KSU_Golf_Carts\\Project_db.db')
            data_insert_query = '''INSERT INTO students_info (student_id,first_name,last_name,user_class,Email,password,phone,privilage_type) \
            VALUES (?,?,?,?,?,?,?)'''
            data_insert_tuple = (
            self.stu_id_entry.get(), self.fname_entry.get(), self.lname_entry.get(), self.user_class.get(),
            self.email_entry.get(), hashlib.sha256(self.password_entry.get().encode()).hexdigest(),
            self.phone_entry.get(), self.user_privilage_var.get())
            connect_db.execute(data_insert_query, data_insert_tuple)
            connect_db.commit()
            connect_db.close()
            tkinter.messagebox.showinfo('Insert', 'تم أضافة الطالب بنجاح')

    def open_login(self):
        self.main_window.destroy()
        #log = Login_Window()

    def is_int(self, x):
        try:
            x = int(x)
            return True
        except:
            return False

xx=sing_up()