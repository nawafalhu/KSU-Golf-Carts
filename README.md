# KSU-Golf-Carts
Electric golf carts provide efficient mobility for students, faculty, and staff, reducing walking distances and enhancing accessibility.
# KSUGolfCarts - Campus Golf Cart Reservation System

## Overview

KSUGolfCarts is a reservation system designed to manage golf cart reservations within the KSU campus. The system provides a user-friendly interface for students, faculty, and staff to reserve golf carts conveniently.

## Contributors
NAWAF ALHOMAIDHI 442101288
<br>
OMAR ALMOHSEN 443101907
<br>
TURKI ALJAMMAZ 443102093
<br>

## Features

- **Sign-Up Window:**
  - Capture user information, including first name, last name, user class, student ID, password, email address, and phone number.
  - Submit button sends user information to the central database, securely storing only the password hash.
  - Input validation ensures data integrity.
  - Login button opens the Login window.

- **Login Window:**
  - Fields for user or admin ID and password.
  - Login button connects to the central database to verify credentials.
  - Error messages for validation issues.
  - Opens User or Admin window based on success.

- **Admin Window:**
  - Fields for the admin to enter golf cart plate number and associated college.
  - Create button sends information to the central database.
  - Logout button returns to the Sign-Up window.
  - Backup button creates a CSV backup of the central database.

- **User Window:**
  - Two tabs: Reserve a Cart and View my Reservations.
  - **Reserve a Cart Tab:**
    - Displays a list of colleges for user selection.
    - Fields for entering start and end time & date of the reservation.
    - Reservation period constraints based on user class.
    - Reserve button checks availability and reserves the selected golf cart.
    - Logout button returns to the Sign-Up window.
    - Logs transactions with time, user ID, golf cart plate number, location, and reservation times.
  - **View my Reservations Tab:**
    - Displays active reservations, including golf cart plate numbers, locations, and reservation times.
    - Show button retrieves all reservations for the logged-in user.
    - Logout button returns to the Sign-Up window.
