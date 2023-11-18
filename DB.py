import sqlite3

Connection = sqlite3.connect("KSU-Galf.db")
Cursor = Connection.cursor()

Cursor.execute(
    """CREATE TABLE IF NOT EXISTS STUDENT (
       StudentID INT PRIMARY KEY NOT NULL,
       FirstName TEXT NOT NULL,
       LastName TEXT  NULL,
       UserClass TEXT NULL,
       Email TEXT NULL,
       Password TEXT NULL,
       Phone TEXT NULL
    )"""
)

Cursor.execute(
    """CREATE TABLE IF NOT EXISTS GOALF(
       GolfPlate INT PRIMARY KEY NOT NULL,
       COLLEGE TEXT NOT NULL
    )"""
)


# Cursor.execute(
#     """CREATE TABLE IF NOT EXISTS Reservations(
       
#     )"""
# )

