#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (isalpha(argv[1][i]))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        int key = atoi(argv[1]);

        string plaintext = get_string("plaintext: \n");
        printf("ciphertext: ");
        for (int j = 0, m = strlen(plaintext); j < m; j++)
        {
            if (isupper(plaintext[j]))
            {
                plaintext[j] = ((plaintext[j] + key - 65) % 26 + 65);
                printf("%c", plaintext[j]);
            }
            else if (islower(plaintext[j]))
            {
                plaintext[j] = ((plaintext[j] + key - 97) % 26 + 97);
                printf("%c", plaintext[j]);
            }
            else
            {
                printf("%c", plaintext[j]);
            }

        }
        printf("\n");
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    return 0;
}