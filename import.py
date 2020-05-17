import sqlite3
import csv
import sys


def main():

    # checking argv 
    if (len(sys.argv) != 2):
        sys.exit("Usage: import.py file.csv")

    filename = sys.argv[1]

    if not (filename.endswith(".csv")):
        sys.exit("provide a *.csv")

    # use .db file and make a cursor
    sqlite_file = "students.db"
    con = sqlite3.connect(sqlite_file)

    cur = con.cursor()

    # import from csv file
    with open("characters.csv", "r") as characters:

        # dictionary reader that iterates through rows
        reader = csv.DictReader(characters)

        for row in reader:
            names = []

            for part in row["name"].split(" "):
                names.append(part)

            names.append(row["house"])
            names.append(row["birth"])

            if (len(names) == 5):
                cur.execute("students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", names[:5])

            if (len(names) == 4):
                cur.execute("students (first, last, house, birth) VALUES(?, ?, ?, ?)", names[:4])

  

