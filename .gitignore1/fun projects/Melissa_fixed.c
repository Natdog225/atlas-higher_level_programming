#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CREDIT_VALUE 0.25
int main(void);

int main()
{
	printf("Welcome to the Betting Game!\n");

	srand(time(NULL));

	int bet_amount = 0;
	int outcome;
	int quarters = 80;
	float balance = 20.00;

	while (1)
	{
		printf("You have $%.2f worth of quarters.\n\n", balance);
		printf("You have %d quarters ($%.2f).\n", quarters, balance);

		printf("Enter the number of credits to bet (or 0 to cash out): ");
		if (scanf("%d", &bet_amount) != 1)
		{
			printf("Invalid input. Please enter a number.\n");
			while (getchar() != '\n')
				;
			continue;
		}

		if (bet_amount == 0)
		{
			printf("Cashing out. You ended with $%.2f.\n", balance);
			break;
		}
		else if (bet_amount > quarters || bet_amount <= 0)
		{
			printf("Invalid bet. You have %d quarters. Please try again.\n", quarters);
			continue;
		}

		outcome = rand() % 100 + 1;
		printf("Reel stopped on the number %d\n", outcome);

		if (outcome < 50)
		{
			printf("You lose!\n");
			quarters -= bet_amount;
		}
		else if (outcome <= 74)
		{
			printf("You get your money back!\n");
		}
		else if (outcome <= 94)
		{
			printf("You double your money!\n");
			quarters += bet_amount;
		}
		else
		{
			printf("Jackpot! You tripled your money!\n");
			quarters += 2 * bet_amount;
		}

		balance = quarters * CREDIT_VALUE;
		printf("Your new balance is: $%.2f (%d quarters)\n\n", balance, quarters);

		if (quarters == 0)
		{
			printf("Game Over! You have no more quarters.\n");
			break;
		}
	}

	return 0;
}