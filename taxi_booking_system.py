import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="Abirami@623",  # Replace with your MySQL password
    database="taxi_booking"  # Ensure this is the correct database name
)

cursor = db.cursor()

# Function for User Dashboard
def user_dashboard(user_id, role):
    root = Tk()
    root.title("User Dashboard")
    root.geometry("600x400")

    # Add background image
    try:
        bg_image = Image.open("background.jpg")  # Replace with your image path
        bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        bg = ImageTk.PhotoImage(bg_image)
        bg_label = Label(root, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error loading background image: {e}")

    # Dashboard Frame
    frame = Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=200)

    welcome_message = f"Welcome, User {user_id}!"
    Label(frame, text=welcome_message, font=("Times New Roman", 16, "bold"), bg="white").pack(pady=10)

    book_button = Button(frame, text="Book Ride", font=("Times New Roman", 12), bg="green", fg="white", command=lambda: booking_page(user_id))
    book_button.pack(pady=10)

    logout_button = Button(frame, text="Logout", font=("Times New Roman", 12), bg="red", fg="white", command=root.destroy)
    logout_button.pack(pady=10)

    root.mainloop()

# Login Page
def login_page():
    def attempt_login():
        email = email_entry.get()
        password = password_entry.get()

        cursor.execute("SELECT user_id, role FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()

        if user:
            user_id, role = user
            messagebox.showinfo("Success", "Login successful!")
            root.destroy()
            user_dashboard(user_id, role)
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    root = Tk()
    root.title("Login Page")
    root.geometry("600x400")

    try:
        bg_image = Image.open("background.jpg")
        bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        bg = ImageTk.PhotoImage(bg_image)
        bg_label = Label(root, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error loading background image: {e}")

    frame = Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=300, height=250)

    Label(frame, text="Login", font=("Times New Roman", 16, "bold"), bg="white").pack(pady=10)

    Label(frame, text="Email:", font=("Times New Roman", 12), bg="white").pack(pady=5)
    email_entry = Entry(frame, font=("Times New Roman", 12), width=25)
    email_entry.pack(pady=5)

    Label(frame, text="Password:", font=("Times New Roman", 12), bg="white").pack(pady=5)
    password_entry = Entry(frame, font=("Times New Roman", 12), width=25, show="*")
    password_entry.pack(pady=5)

    login_button = Button(frame, text="Login", font=("Times New Roman", 12), bg="blue", fg="white", command=attempt_login)
    login_button.pack(pady=10)

    root.mainloop()

# User Registration Page
def register_user():
    def save_registration():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        phone = phone_entry.get()

        cursor.execute("INSERT INTO users (name, email, password, phone, role) VALUES (%s, %s, %s, %s, 'user')",
                       (name, email, password, phone))
        db.commit()

        messagebox.showinfo("Success", "Registration successful!")
        root.destroy()
        login_page()

    root = Tk()
    root.title("User Registration")
    root.geometry("600x400")

    try:
        bg_image = Image.open("background.jpg")
        bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        bg = ImageTk.PhotoImage(bg_image)
        bg_label = Label(root, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error loading background image: {e}")

    frame = Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=350)

    Label(frame, text="Register for Booking", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

    Label(frame, text="Name:", font=("Times New Roman", 12), bg="white").pack(pady=5)
    name_entry = Entry(frame, font=("Times New Roman", 12), width=30)
    name_entry.pack(pady=5)

    Label(frame, text="Email:", font=("Times New Roman", 12), bg="white").pack(pady=5)
    email_entry = Entry(frame, font=("Times New Roman", 12), width=30)
    email_entry.pack(pady=5)

    Label(frame, text="Password:", font=("Times New Roman", 12), bg="white").pack(pady=5)
    password_entry = Entry(frame, font=("Times New Roman", 12), width=30, show="*")
    password_entry.pack(pady=5)

    Label(frame, text="Phone:", font=("Times New Roman", 12), bg="white").pack(pady=5)
    phone_entry = Entry(frame, font=("Times New Roman", 12), width=30)
    phone_entry.pack(pady=5)

    save_button = Button(frame, text="Save", font=("Arial", 12), bg="green", fg="white", command=save_registration)
    save_button.pack(pady=10)

    root.mainloop()

# Booking Page
def booking_page(user_id):
    def book_ride():
        pickup = pickup_entry.get()
        drop = drop_entry.get()

        cursor.execute("SELECT driver_id FROM drivers LIMIT 1")
        driver = cursor.fetchone()

        if driver:
            driver_id = driver[0]
            try:
                cursor.execute(
                    "INSERT INTO bookings (user_id, driver_id, pickup_location, drop_location, status) VALUES (%s, %s, %s, %s, %s)", 
                    (user_id, driver_id, pickup, drop, 'Pending'))
                db.commit()
                messagebox.showinfo("Success", "Ride booked successfully!")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")
        else:
            messagebox.showerror("Error", "No drivers available. Try later.")

    root = Tk()
    root.title("Booking Page")
    root.geometry("600x400")

    try:
        bg_image = Image.open("booking_background.jpg")
        bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        bg = ImageTk.PhotoImage(bg_image)
        bg_label = Label(root, image=bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error loading background image: {e}")

    frame = Frame(root, bg="white", bd=5)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=350, height=300)

    Label(frame, text="Book a Ride", font=("Times New Roman", 16, "bold"), bg="white").pack(pady=10)

    Label(frame, text="Pickup Location:", font=("Times New Roman", 12), bg="white").pack(pady=5)
    pickup_entry = Entry(frame, font=("Times New Roman", 12), width=25)
    pickup_entry.pack(pady=5)

    Label(frame, text="Drop Location:", font=("Times New Roman", 12), bg="white").pack(pady=5)
    drop_entry = Entry(frame, font=("Times New Roman", 12), width=25)
    drop_entry.pack(pady=5)

    book_button = Button(frame, text="Book Ride", font=("Times New Roman", 12), bg="blue", fg="white", command=book_ride)
    book_button.pack(pady=10)

    root.mainloop()

# Run the login page
login_page()

# Close the database connection
db.close()
