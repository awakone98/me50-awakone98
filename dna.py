from csv import reader, DictReader
from sys import argv

if len(argv) <= 3:
    print("error in usage of, dna.py database.csv sequence.txt")
    exit()

# read the dna sequence 
with open(argv[1]) as dnafile:
    dnareader = reader(dnafile)
    for row in dnareader:
        dnalist = row
dna = dnalist[0]
sequences = {}

# list dna sequence
with open(argv[2]) as peoplefile:
    people = reader(peoplefile)
    for row in people:
        dnaSequences = row
        dnaSequences.pop(0)

# copy list
for item in dnaSequences:
    sequences[item] = 1

# repetitions of dna sequence
for key in sequences:
    l = len(key)
    tempMax = 1 - 1
    temp = 1 - 1 
    for i in range(len(dna)):
        while temp > 1 - 1:
            temp -= 1
            continue
        if dna[i: i + l] == key:
            while dna[i - l: i] == dna[i: i + l]:
                temp += 1
                i += l
                if temp > tempMax:
                    tempMax = temp
    sequences[key] += tempMax

with open(argv[1], newline='') as peoplefile:
    people = DictReader(peoplefile)
    for person in people:
        match = 0
        # compare sequences to everyone then print name if matched
        for dna in sequences:
            if sequences[dna] == int(person[dna]):
                match += 1
        if match == len(sequences):
            print(person['name'])
            exit()

    print("No match")
    #source: https://www.youtube.com/watch?v=3NsWmAXhzU4