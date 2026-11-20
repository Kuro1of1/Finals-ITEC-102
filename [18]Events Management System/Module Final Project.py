
import sqlite3
import re
import uuid

# Connect to the database
connection = sqlite3.connect("event_management.db")
cursor = connection.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date TEXT NOT NULL,
    location TEXT NOT NULL,
    max_participants INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS participants (
    registration_id TEXT PRIMARY KEY,
    student_name TEXT NOT NULL,
    email TEXT NOT NULL,
    event_id INTEGER,
    FOREIGN KEY (event_id) REFERENCES events(event_id)
)
""")

connection.commit()


# Validate email address
def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.match(pattern, email)


# Add a new event
def add_event():
    print("\n--- ADD NEW EVENT ---")

    name = input("Event name: ")
    date = input("Event date (YYYY-MM-DD): ")
    location = input("Event location: ")

    try:
        maximum = int(input("Maximum participants: "))

        if maximum <= 0:
            print("Maximum participants must be greater than zero.")
            return

        cursor.execute("""
        INSERT INTO events
        (event_name, event_date, location, max_participants)
        VALUES (?, ?, ?, ?)
        """, (name, date, location, maximum))

        connection.commit()
        print("Event successfully added!")

    except ValueError:
        print("Please enter a valid number.")


# Display available events
def view_events():
    print("\n--- AVAILABLE EVENTS ---")

    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()

    if not events:
        print("No events available.")
        return

    for event in events:
        print("\nEvent ID:", event[0])
        print("Name:", event[1])
        print("Date:", event[2])
        print("Location:", event[3])
        print("Maximum Participants:", event[4])


# Register a student
def register_student():
    print("\n--- STUDENT REGISTRATION ---")

    view_events()

    try:
        event_id = int(input("\nEnter Event ID: "))

        cursor.execute(
            "SELECT * FROM events WHERE event_id = ?",
            (event_id,)
        )
        event = cursor.fetchone()

        if event is None:
            print("Event not found.")
            return

        cursor.execute(
            "SELECT COUNT(*) FROM participants WHERE event_id = ?",
            (event_id,)
        )
        count = cursor.fetchone()[0]

        if count >= event[4]:
            print("This event is already full.")
            return

        name = input("Student name: ")
        email = input("Email address: ")

        if not validate_email(email):
            print("Invalid email address.")
            return

        registration_id = str(uuid.uuid4())[:8].upper()

        cursor.execute("""
        INSERT INTO participants
        (registration_id, student_name, email, event_id)
        VALUES (?, ?, ?, ?)
        """, (registration_id, name, email, event_id))

        connection.commit()

        print("\nRegistration successful!")
        print("Registration ID:", registration_id)

    except ValueError:
        print("Please enter a valid Event ID.")


# View registered participants
def view_participants():
    print("\n--- REGISTERED PARTICIPANTS ---")

    cursor.execute("""
    SELECT participants.registration_id,
           participants.student_name,
           participants.email,
           events.event_name
    FROM participants
    JOIN events
    ON participants.event_id = events.event_id
    """)

    participants = cursor.fetchall()

    if not participants:
        print("No registered participants yet.")
        return

    for person in participants:
        print("\nRegistration ID:", person[0])
        print("Student Name:", person[1])
        print("Email:", person[2])
        print("Event:", person[3])


# Search for an event
def search_event():
    print("\n--- SEARCH EVENT ---")

    keyword = input("Enter event name: ")

    cursor.execute("""
    SELECT * FROM events
    WHERE event_name LIKE ?
    """, ('%' + keyword + '%',))

    results = cursor.fetchall()

    if not results:
        print("No matching event found.")
        return

    for event in results:
        print("\nEvent ID:", event[0])
        print("Event Name:", event[1])
        print("Date:", event[2])
        print("Location:", event[3])


# Cancel a registration
def cancel_registration():
    print("\n--- CANCEL REGISTRATION ---")

    registration_id = input("Enter Registration ID: ").upper()

    cursor.execute("""
    SELECT * FROM participants
    WHERE registration_id = ?
    """, (registration_id,))

    participant = cursor.fetchone()

    if participant:
        cursor.execute("""
        DELETE FROM participants
        WHERE registration_id = ?
        """, (registration_id,))

        connection.commit()
        print("Registration successfully cancelled.")

    else:
        print("Registration ID not found.")


# Main menu
def main():
    while True:
        print("\n================================================")
        print(" STUDENT ORGANIZATION EVENT MANAGEMENT SYSTEM")
        print("================================================")
        print("1. Add New Event")
        print("2. View Available Events")
        print("3. Register Student")
        print("4. View Participants")
        print("5. Search Event")
        print("6. Cancel Registration")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_event()

        elif choice == "2":
            view_events()

        elif choice == "3":
            register_student()

        elif choice == "4":
            view_participants()

        elif choice == "5":
            search_event()

        elif choice == "6":
            cancel_registration()

        elif choice == "7":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please try again.")


main()

connection.close()
