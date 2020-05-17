from csv import reader, DictReader
from sys import argv
import sys
import csv

if len(argv) < 3:
    print("usage error, dna.py sequence.txt database.csv")
    exit()

# read the dna sequence on file
with open(argv[2]) as dnafile:
    dnareader = reader(dnafile)
    for row in dnareader:
        dnalist = row

# place in string
dna = dnalist[0]
# dictionary of stored sequences
sequences = {}

# list sequences
with open(argv[1]) as peoplefile:
    people = reader(peoplefile)
    for row in people:
        dnaSequences = row
        dnaSequences.pop(0)
        break

# for genes that are keys copy list
for item in dnaSequences:
    sequences[item] = 1

# count repitions
for key in sequences:
    l = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(dna)):
        while temp > 0:
            temp -= 1
            continue

        # Count when repetition is present and segment of dna corresponds to the key
        if dna[i: i + l] == key:
            while dna[i - l: i] == dna[i: i + l]:
                temp += 1
                i += l
            if temp > tempMax:
                tempMax = temp
    sequences[key] += tempMax

# open database as dictionary
with open(argv[1], newline='') as peoplefile:
    people = DictReader(peoplefile)
    for person in people:
        match = 0
        for dna in sequences:
            if sequences[dna] == int(person[dna]):
                match += 1
        if match == len(sequences):
            print(person['name'])
            exit()

    print("No match")
    #source: https://www.reddit.com/r/cs50/comments/eu5if0/check50_incorrectly_marking_pset6_dna_spoiler/