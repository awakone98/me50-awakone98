from cs50 import SQL
from csv import reader
from sys import argv

db = SQL("sqlite:///students.db")

#check that correct codes being used 
if len(argv) < 2:
    print("usage error, import.py characters.csv")
    exit()

# open students csv file into list
with open(argv[1], newline='') as charactersFile:
    characters = reader(charactersFile)
    for character in characters:
        if character[0] == 'name':
            continue
        # insert full name
        fullName = character[0].split()
        # insert full name and info, NULL theres no middle name
        if len(fullName) < 3:
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       fullName[0], None, fullName[1], character[1], character[2])

        else:
            db.execute("INSERT INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                       fullName[0], fullName[1], fullName[2], character[1], character[2])