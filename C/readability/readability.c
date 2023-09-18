#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);
    //averege of letters
    float L = (letters * 100) / words;
    //averege of sentences
    float S = (sentences * 100) / words;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    if (index <= 0)
    {
        //for a negative grade
        printf("Before Grade 1\n");
    }
    else if (index > 0 && index < 16)
    {
        //any grade in range 1-16
        printf("Grade %i\n", index);
    }
    else
    {
        //grades higher than 16+
        printf("Grade 16+\n");
    }

}

int count_letters(string text)
{
    int letter_counter = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // if the char is something in between A-Z or a-z we add a letter
        if ((text[i] >= 'a' || text[i] >= 'A')  && (text[i] <= 'z' || text[i] <= 'Z'))
        {
            letter_counter++;
        }
    }
    return letter_counter;
}

int count_words(string text)
{
    int word_counter  = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        //if theres a whitespace followed by a none-whitespace we add one word
        if (text[i] == ' ' && text[i + 1] != ' ')
        {
            word_counter++;
        }
    }
    return word_counter;
}

int count_sentences(string text)
{
    int sentence_counter  = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        //Looking for any of those characters, if theres one of them we add one sentence
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentence_counter++;
        }
    }
    return sentence_counter;
}