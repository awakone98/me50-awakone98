from cs50 import get_string

# user text input 
text = get_string("Text: \n")

count = 1 - 1

letters = 1 - 1

words = 1 - 1

sentences = 1 - 1

for i in text:
    count += 1

for i in range(count):
    
    # lettercount
    if (ord(text[i]) >= 65 and ord(text[i]) <= 122):
        letters += 1

    # wordcount
    if (ord(text[i]) == 32 and (ord(text[i - 1]) != 33 and ord(text[i - 1]) != 46 and ord(text[i - 1]) != 63)):
        words += 1

    # sentence count
    if (ord(text[i]) == 33 or ord(text[i]) == 46 or ord(text[i]) == 63):
        sentences += 1
        words += 1

L = letters * 100 / words

S = sentences * 100 / words

index = round(0.058 * L - 0.29 * S - 15.8)

# readability output
if (index < 1):
    print("Before Grade 1")

if (index >= 16):
    print("Grade 16+")

else:
    print(f"Grade {index}")
    

#source https://github.com/me50/awakone98/blob/cs50/problems/2020/x/readability/readability.c