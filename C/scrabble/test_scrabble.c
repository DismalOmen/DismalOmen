#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    string word = get_string("word: ");
    int score = 0;
    int i;
    word += POINTS[word[i]];
    printf("%c\n", word);
    // for (int i = 0, n = strlen(word); i < n; i++)
    // {
    //     if (isupper(word[i]))
    //     {
    //         word[i] = tolower(word[i]);
    //         score += POINTS[word[i]];
    //     }
    //     else
    //     {
    //         score += POINTS[word[i]];
    //     }
    // }
    // return score;
    // printf("\n");
}