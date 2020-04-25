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
    wordcount = 1;
    sentencecount = 0;

#Wordcount
  for (int i = 0; i < strlen(text); i++)
         if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
            letterscount++;
         else if (text[i] == ' ')
              wordcount++;
         else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
             sentencecount++;
#print("letterscount and wordcount = %i, sentencecount = %i\n");

    float grade = 0.0588 * (100 * (float) letterscount / (float) wordcount) - 0.296 * (100 * (float) sentencecount / 
                  (float) wordcount) - 15.8;
    if (grade < 16 && grade >= 0)
        print("Grade %i\n", (int) round(grade));
    else if (grade >= 16)
        print("Grade 16+\n");
    else:
        print("Before Grade 1\n");

if __name__ == "__main__":
     main()
     