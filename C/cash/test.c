#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc != 2 || isalpha(argv[1]))
    {
        printf("Usage: ./caesar key\n");
    }
    else
    {
        printf("we good");
    }
}