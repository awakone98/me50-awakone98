#include cs50 
#include get_string

from cs50 import get_string

text = get_string("Text: \n")
counter = 0
words = 0
letters = 0
sentences = 0


def main():
    if (index < 1): 
       print("Before Grade 1")
    if (index >= 16):
       print("Grade 16+")
    else:
       print(f"Grade {index}")

#User input
for index in text: 
            counter += 1
for index in range(counter):
    
         #lettercount
         if (ord(text[index]) >= 65 and ord(text[index]) <= 122):
           letters += 1
L = letters * 100 / words

         #wordcount
if (ord(text[index]) == 32 and (ord(text[index - 1]) != 33 and ord(text[index - 1]) != 46 and ord(text[index - 1]) != 63)):
          words += 1
          
         #sentancecount
if (ord(text[index]) == 33 or ord(text[index]) == 46 or ord(text[index]) == 63):
          sentences += 1
          words += 1
S = sentences * 100 / words

index = round(0.0588 * L - 0.296 * S - 15.8)   

#source https://www.youtube.com/watch?v=3NsWmAXhzU4
