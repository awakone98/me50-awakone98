from cs50 import SQL
from sys import argv

# check for correct usage
if len(argv) < 2:
    print("usage error, roster.py houseName")
    exit()

# open in variable then list house members in alphabetical order
db = SQL("sqlite:///students.db")
students = db.execute("SELECT * FROM students WHERE house = (?) ORDER BY last", argv[1])

# print full name
for student in students:
    if student['middle'] != None:
        print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")
    else:
        print(f"{student['first']} {student['last']}, born {student['birth']}")