#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_BET 80

int main()
{
	srand(time(NULL));

	int bet_amount = 0;
	int outcome;
	int quarters = 80;
	float balance = 20.00;

	printf("Welcome to the Betting Game!\n");
	printf("You have $%.2f worth of quarters.\n\n", balance);

	while (quarters > 0)
	{
		printf("You have %d quarters ($%.2f).\n", quarters, balance);

		printf("Enter the number of quarters to bet (or 0 to cash out): ");
		scanf("%d", &bet_amount); // & added to scanf

		if (bet_amount == 0)
		{
			printf("Cashing out. You ended with $%.2f.\n", balance);
			break;
		}
		else if (bet_amount > quarters || bet_amount <= 0)
		{ // Adjusted condition
			printf("Invalid bet. You have %d quarters. Please try again.\n", quarters);
			continue;
		}

		outcome = rand() % 100 + 1;
		printf("Reel stopped on the number %d\n", outcome);

		if (outcome < 50)
		{
			printf("You lose!\n\n");
			quarters -= bet_amount;
		}
		else if (outcome <= 74)
		{
			printf("You get your money back!\n\n");
		}
		else if (outcome <= 94)
		{
			printf("You double your money!\n\n");
			quarters += bet_amount;
		}
		else
		{
			printf("Jackpot! You triple your money!\n\n");
			quarters += 2 * bet_amount;
		}

		balance = quarters * 0.25; // Update balance using CREDIT_VALUE

		if (quarters == 0)
		{
			printf("Game Over! You have no more quarters.\n");
			break;
		}
	}

	return 0;
}
