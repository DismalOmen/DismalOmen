#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("Number of cents? ");
    }
    while (cents < 0);
    return cents;
}

int calculate_quarters(int cents)
{
    //creating a const equal to the value of the coin so the chances of making a mistake with that value kinda goes away
    const int QUARTER = 25;
    //to keep track of the coins needed
    int total_amount_quarters = 0;
    //condition for the loop to repeat if u can use this value of coin
    while (cents >= QUARTER)
    {
        //substract the amount in question
        cents = cents - QUARTER;
        //each time the loop repeats, increase by one the amount of coins
        total_amount_quarters++;
    }
    //so u can have in another place this said amount of coins
    return total_amount_quarters;

}

int calculate_dimes(int cents)
{
    const int DIMES = 10;
    int total_amount_dimes = 0;
    while (cents >= DIMES)
    {
        cents = cents - DIMES;
        total_amount_dimes++;
    }
    return total_amount_dimes;
}

int calculate_nickels(int cents)
{
    const int NICKLES = 5;
    int total_amount_nickles = 0;
    while (cents >= NICKLES)
    {
        cents = cents - NICKLES;
        total_amount_nickles++;
    }
    return total_amount_nickles;
}

int calculate_pennies(int cents)
{
    const int PENNIES = 1;
    int total_amount_pennies = 0;
    while (cents >= PENNIES)
    {
        cents = cents - PENNIES;
        total_amount_pennies++;
    }
    return total_amount_pennies;
}
