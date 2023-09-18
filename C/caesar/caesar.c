#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//show to computer only_digits
bool only_digits(string s);

int main(int argc, string argv[])
{
    string t = argv[1];

    // argc represents the arg count, if not equal 2 break
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else if (!only_digits(t))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        //make the key an in, cause it was an string
        int key = atoi(argv[1]);
        //ask user for plaintext
        string r = get_string("Plaintext: ");
        //print the result
        printf("Ciphertext: ");
        for (int i = 0, len = strlen(r); i < len; i++)
        {
            //if is a uppercase letter ("A" = 65 in ascii), we subtract 65, put in 0 add the key so we get the cipher and then we need %26 to "loop" over A-Z and finally we add the "A" again
            if (isupper(r[i]))
            {
                printf("%c", (r[i] - 65 + key) % 26 + 65);
            }
            //same thing here but "a" is equal to 97
            else if (islower(r[i]))
            {
                printf("%c", (r[i] - 97 + key) % 26 + 97);
            }
            // for any other character that is not a letter
            else
            {
                printf("%c", r[i]);
            }
        }
        printf("\n");
    }

}

bool only_digits(string s)
{

    for (int i = 0, len = strlen(s); i < len; i++)
    {
        //loop trough every single character with for and then check if is a digit (0-9)
        if (isdigit(s[i]))
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    return 1;
}
