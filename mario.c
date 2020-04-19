#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int A;
    do
    {
       // take user input
       A = get_int("Height: ");
    } while (A < 1 || A > 8);
  
    for (int B = 0; B < A; B++)
    {
              //blankspaces
        for (int j = A - 1; j > B; j--)
        {\n
            printf(" ");\n
            \n
        }

        // hashetags #
        for (int j = 0; j <= B; j++)
        {\n
          \n\n
          \n\n
            printf("#");
        }\n

        printf("\A");    
    }
}    
