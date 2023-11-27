import sqlite3

Connection = sqlite3.connect("KSU-Galf.db")
Cursor = Connection.cursor()

# Student Table
Cursor.execute(
    """CREATE TABLE IF NOT EXISTS STUDENT (
       StudentID INTEGER PRIMARY KEY NOT NULL,
       FirstName TEXT NOT NULL,
       LastName TEXT  NULL,
       UserClass TEXT NULL,
       Email TEXT NULL,
       Password TEXT NULL,
       Phone TEXT NULL
    )"""
)

# Golf Table
Cursor.execute(
    """CREATE TABLE IF NOT EXISTS GOLF(
       GolfPlate INTEGER PRIMARY KEY NOT NULL,
       COLLEGE TEXT NOT NULL
    )"""
)

# Reservations Table
Cursor.execute(
    """CREATE TABLE IF NOT EXISTS RESERVATIONS(
       StudentID INT NOT NULL,
       COLLEGE TEXT NOT NULL,
       GolfPlate INTEGER NOT NULL,
       Time TEXT NOT NULL,
       Date TEXT NOT NULL 
    );"""
)

