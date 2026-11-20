1. SQLITE3 MODULE


Purpose:

SQLite3 is a built-in Python module used for creating, managing, and accessing databases. It allows programs to store information in an organized way.

How it is used in the Student Organization Event Management System:

SQLite3 stores event information and student registration records. It creates two tables: one for events and another for participants. It also allows the program to add, retrieve, and delete records.

Code:

import sqlite3

connection = sqlite3.connect("event_management.db")
cursor = connection.cursor()

Explanation:

- "import sqlite3" loads the SQLite3 module.
- "sqlite3.connect()" connects the program to a database file.
- ""event_management.db"" is the name of the database.
- "connection.cursor()" creates a cursor used to execute SQL commands.

Other Uses:

SQLite3 can be used to store customer information, manage inventory, record student grades, organize employee records, and develop other database-driven applications.

Installation:

SQLite3 is included in Python's standard library. No additional installation is required.

---

2. RE MODULE (REGULAR EXPRESSIONS)

---

Purpose:

The "re" module is a built-in Python module used for searching, matching, and checking patterns in text.

How it is used in the Student Organization Event Management System:

The "re" module is used to validate the email addresses entered by students during registration. It checks whether the email follows a basic email format before allowing the program to save the registration.

Code:

import re

def validate_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.match(pattern, email)

Explanation:

- "import re" loads the Regular Expressions module.
- "def validate_email(email)" creates a function that receives an email address.
- "pattern" defines the expected email format.
- "re.match()" checks whether the entered email matches the pattern.
- The function returns a match if the format is valid; otherwise, it returns "None".

Other Uses:

The "re" module can be used to validate usernames, check phone number formats, find specific words in text, identify patterns, and remove unwanted characters from strings.

Installation:

The "re" module is included in Python's standard library. No additional installation is required.


3. UUID MODULE (UNIVERSALLY UNIQUE IDENTIFIER)


Purpose:

UUID is a built-in Python module used to generate unique identification codes. These codes help distinguish one record or object from another.

How it is used in the Student Organization Event Management System:

The UUID module generates a registration ID for every student who successfully registers for an event. This ID is stored in the database and can be used to identify or cancel a specific registration.

Code:

import uuid

registration_id = str(uuid.uuid4())[:8].upper()

Explanation:

- "import uuid" loads the UUID module.
- "uuid.uuid4()" generates a random UUID.
- "str()" converts the generated UUID into a string.
- "[:8]" selects the first eight characters.
- ".upper()" converts the characters into uppercase letters.

The result is a shorter registration code that can be displayed to the student.

Other Uses:

The UUID module can be used to generate unique IDs for users, products, transactions, database records, files, and other applications that require identification codes.

Installation:

The UUID module is included in Python's standard library. No additional installation is required.


SUMMARY

The three modules work together in the Student Organization Event Management System:

1. SQLite3 – Stores and manages event and participant information.
2. RE – Checks the format of student email addresses.
3. UUID – Generates registration identification codes.

By combining these three modules, the program becomes more organized and functional. Each module performs a different task that contributes to the overall operation of the system.