#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int population;
    do
    {
        population  = get_int("Population size? ");
    }
    while (population < 9);
    // TODO: Prompt for end size
    int population0;
    do
    {
        population0  = get_int("Ending population size? ");
    }
    while (population0 < population);
    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    while (population < population0)
    {
        population  = population + (population / 3) - (population / 4);
        years++;
    }
    // TODO: Print number of years
    printf("Years: %i\n", years);
}
