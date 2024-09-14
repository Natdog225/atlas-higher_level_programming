#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

// Function prototypes
void display_reels(const char **result1, const char **result2, const char **result3);
const char *spin_reel(int reel_index);
int main(void); 

#define NUM_REELS 3
#define NUM_SYMBOLS 6
#define MAX_SYMBOL_LENGTH 15

const char *reels[NUM_REELS][NUM_SYMBOLS] = {
    {"Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"},
    {"Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"},
    {"Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar"}};

char *slot_machine[6];

// Pay tables
float three_of_a_kind_payouts[] = {0.75, 1.50, 2.25, 3.00};
float two_of_a_kind_payouts[] = {0.25, 0.50, 0.75, 1.00};
float cherry_jackpot_payouts[] = {5.00, 10.00, 15.00, 20.00};

// Function to spin a single reel
const char *spin_reel(int reel_index)
{
    int index = rand() % NUM_SYMBOLS;
    return reels[reel_index][index];
}

// Function to display the slot machine with spinning animation
void display_reels(const char **result1, const char **result2, const char **result3)
{
    int i;
    for (i = 0; i < 5; i++)
    {
        sprintf(slot_machine[3], "|  [ %d ]  |", rand() % 10);
        system("clear");
        for (int j = 0; j < 6; j++)
        {
            printf("%s\n", slot_machine[j]);
        }
        usleep(300000);
    }

    char *temp_result1 = (char *)spin_reel(0); // Explicit cast
    char *temp_result2 = (char *)spin_reel(1);
    char *temp_result3 = (char *)spin_reel(2);

    *result1 = temp_result1;
    *result2 = temp_result2;
    *result3 = temp_result3;

    sprintf(slot_machine[3], "|  %s %s %s  |", *result1, *result2, *result3);
    system("clear");
    for (int j = 0; j < 6; j++)
    {
        printf("%s\n", slot_machine[j]);
    }
}

int main(void)
{
    srand((unsigned int)time(NULL));

    // Allocate memory
    for (int i = 0; i < 6; i++)
    {
        slot_machine[i] = malloc((3 + 3 * MAX_SYMBOL_LENGTH + 2) * sizeof(char));
        strcpy(slot_machine[i], "");
    }
    strcpy(slot_machine[0], "   .-----------.");
    strcpy(slot_machine[1], "  /  O  O  O  \\");
    strcpy(slot_machine[2], " |     O     |");
    strcpy(slot_machine[3], " |  [       ]  |");
    strcpy(slot_machine[4], "  \\  O  O  O  /");
    strcpy(slot_machine[5], "   '-----------'");

    float balance = 20.0;
    float bet, winnings;
    const char *result1, *result2, *result3;

    while (1)
    {
        printf("Choose your bet ($0.25, $0.50, $0.75, $1.00): ");
        scanf("%f", &bet);

        if (bet != 0.25 && bet != 0.50 && bet != 0.75 && bet != 1.00)
        {
            printf("We don't accept pennies or trash. Please choose from: $0.25, $0.50, $0.75, or $1.00\n");
            continue;
        }

        balance -= bet;

        display_reels(&result1, &result2, &result3);

        if (strcmp(result1, result2) == 0 && strcmp(result2, result3) == 0)
        {
            if (strcmp(result1, "Cherry") == 0)
            {
                winnings = cherry_jackpot_payouts[(int)(bet / 0.25)];
                printf("JACKPOT! You won A LOT OF MONEY HOLY FUCK! Your balance is now: %.2f\n", balance + winnings);
            }
            else
            {
                winnings = three_of_a_kind_payouts[(int)(bet / 0.25)];
                printf("Three of a kind! You win! Neato job! Your balance is now: %.2f\n", balance + winnings);
            }
        }
        else if (strcmp(result1, result2) == 0 || strcmp(result1, result3) == 0 || strcmp(result2, result3) == 0)
        {
            winnings = two_of_a_kind_payouts[(int)(bet / 0.25)];
            printf("Two of a kind! Hell yeah! Your balance is now: %.2f\n", balance + winnings);
        }
        else
        {
            winnings = 0;
            printf("Try again! Your balance is now: %.2f\n", balance);
        }

        balance += winnings;

        if (balance <= 0)
        {
            printf("You're fucking broke! Get a job, Game over.\n");
            break;
        }
    }

    // Free allocated memory
    for (int i = 0; i < 6; i++)
    {
        free(slot_machine[i]);
    }

    return 0;
}
