#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    //loop input
    do
    {
        n = get_int("Height: ");
    }
    //Make input from the user in range 1-8
    while (n < 1 || n > 8);

    //this will take care of the amount of rows
    for (int i = 0; i < n; i++)
    {
        //this will make the image backwards
        for (int k = n - 1; k > i; k--)
        {
            printf(" ");
        }
        //this will take care of adding a new "#" every new line
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }

}


