#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("What is your name?\n")
    String name = Get_String(); 
    printf("hello, %s\n", name);
}
