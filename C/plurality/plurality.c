#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>


// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    //loop through the candidates, compare both strings and if they are equal add one vote.
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name) == 0)
        {
            candidates[i].votes++;
            //if we added votes, return true
            return true;
        }
    }
    //else return false
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // set a win condition so we can pass the amount of votes and  identify the winner.
    int win_condition = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        //first we loop with the for into the condidates votes and then we pass the value to win_condition
        if (candidates[i].votes > win_condition)
        {
            win_condition = candidates[i].votes;
        }
    }
    // now that we have the value we just print the name of the candidate, in reality we are printing the array of names that have the biggest win_condition amount, so if theres more than one they will appear on screen.
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == win_condition)
        {
            printf("%s\n", candidates[i].name);
        }
    }
}