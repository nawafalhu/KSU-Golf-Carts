from DB import *


StudentID = 72847
FirstName = 666
LastName = 66666
UserClass = 7777
Email = 33333
Password = 222
Phone = 77777

Cursor.execute("""INSERT INTO STUDENT (StudentID, FirstName, LastName, UserClass, Email, Password, Phone) 
                                        VALUES (?,?,?,?,?,?,?)""", (StudentID, FirstName, LastName, UserClass, Email, Password, Phone))