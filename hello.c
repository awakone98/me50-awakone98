#include <cs50.h>
#include <stdio.h>

int main(void)
{
    String name = Get_String("What is your name?\n"); 
    printf("hello, %s\n", name);
}
