#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //getting user input for his name
    string answer = get_string("What's your name? ");
    //printing his name with %s and variable answer
    printf("hello, %s\n", answer);
}