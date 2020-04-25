#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include get_string
from cs50 import get_string

#user input
text = get_string("Text: \n")
    
def main(void):
    letterscount = 0;
    wordcount = 0;
    sentencecount = 0;

for i in range(counter):
    # letterscount
    if (ord(text[i]) >= 65 and ord(text[i]) <= 122):
        letters += 1

    #  wordcount
    else if (ord(text[i]) == 32 and (ord(text[i - 1]) != 33 and ord(text[i - 1]) != 46 and ord(text[i - 1]) != 63)):
        words += 1

    # sentencecount
    else if (ord(text[i]) == 33 or ord(text[i]) == 46 or ord(text[i]) == 63):
        sentences += 1
        words += 1

L = letters * 100 / words
S = sentences * 100 / words

# index formula
index = round(0.0588 * L - 0.296 * S - 15.8)

# output
if (index < 1):
    print("Before Grade 1")

else if (index >= 16):
    print("Grade 16+")

else:
    print("Grade {index}")
    
if __name__ == "__main__":
     main()

#source https://github.com/me50/awakone98/blob/cs50/problems/2020/x/readability/readability.c