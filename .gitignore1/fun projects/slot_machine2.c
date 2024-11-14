#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define MAX_SYMBOL_LENGTH 10
#define CREDIT_VALUE 0.25

char *slot_machine[6];

// Function to display the slot machine
void display_reels(int spin_result)
{
	int i;
	for (i = 0; i < 5; i++)
	{
		sprintf(slot_machine[3], "|  [ %3d ]  |", rand() % 100 + 1); // Random number 1-100
		system("clear");
		for (int j = 0; j < 6; j++)
		{
			printf("%s\n", slot_machine[j]);
		}
		usleep(300000);
	}

	// Display the actual spin result
	sprintf(slot_machine[3], "|  [ %3d ]  |", spin_result);
	system("clear");
	for (int j = 0; j < 6; j++)
	{
		printf("%s\n", slot_machine[j]);
	}
}

// Function prototype for main
int main(void);

int main()
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

	float balance = 60.0;
	int bet_credits, winnings_credits;
	float bet_amount;
	int spin_result;
	char bet_input[10];

	printf("Your balance is: $%.2f (%.0f credits)\n", balance, balance / CREDIT_VALUE);

	while (1)
	{
		printf("Enter the number of credits to bet (0 to cash out): ");

		fgets(bet_input, 10, stdin);
		bet_credits = atoi(bet_input);

		bet_amount = (float)(bet_credits * CREDIT_VALUE); // Explicit cast to float

		if (bet_credits == 0)
		{
			printf("Cashing out. Your final balance is: $%.2f\n", balance);
			break;
		}
		else if (bet_amount > balance)
		{
			printf("You're a bit short on cash. You have %.0f credits.\n", balance / CREDIT_VALUE);
			continue;
		}
		else if (bet_credits < 0)
		{
			printf("We don't accept IOUs or funny money. Please enter a positive number of credits or 0 to cash out.\n");
			continue;
		}

		balance -= bet_amount;

		spin_result = rand() % 100 + 1;
		display_reels(spin_result);

		if (spin_result < 50)
		{
			winnings_credits = 0;
			printf("You lose! YOU WIN NOTHING! GOOD DAY SIR/MA'AM Spin result: %d\n Your balance is now: $%.2f (%.0f credits)\n\n", spin_result, balance, balance / CREDIT_VALUE);
		}
		else if (spin_result <= 74)
		{
			winnings_credits = bet_credits;
			balance += (float)(winnings_credits * CREDIT_VALUE); // Fix the balance update. Explicit cast to float
			printf("You get your bet back! Spin result: %d\nYour balance is now: $%.2f (%.0f credits)\n\n",
				   spin_result, balance, balance / CREDIT_VALUE);
		}
		else if (spin_result < 95)
		{
			winnings_credits = 2 * bet_credits;
			balance += (float)(winnings_credits * CREDIT_VALUE);
			printf("You win double your bet! Spin result: %d\nYour balance is now: $%.2f (%.0f credits)\n\n",
				   spin_result, balance, balance / CREDIT_VALUE);
		}
		else
		{
			winnings_credits = 3 * bet_credits;
			balance += (float)(winnings_credits * CREDIT_VALUE);
			printf("You win triple your bet! Spin result: %d\nYour balance is now: $%.2f (%.0f credits)\n\n",
				   spin_result, balance, balance / CREDIT_VALUE);
		}
		if (balance == 0)
		{
		printf("Game over, Thanks for playing loser.\n");
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
