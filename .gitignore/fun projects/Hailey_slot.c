#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main()
{
	srand(time(NULL)); /* Seed the random number generator */

	int bet_amount = 0;
	int outcome;
	int quarters = 80;	   /* $20 balance (80 quarters) */
	float balance = 20.00; /* Track balance in dollars */

	while (quarters > 0)
	{
		printf("Welcome to the Betting Game!\n");
		printf("You have $%.2f worth of quarters.\n", balance); // Redundant Per the next line.

		printf("You have %d quarters ($%.2f).\n", quarters, balance);

		printf("Enter the number of quarters to bet (or 0 to cash out): ");
		scanf("%d", bet_amount); // & added to scanf, as it needs to be able to store the value. 

		if (bet_amount == 0)
		{
			printf("Cashing out. You ended with $%.2f.\n", balance);
			break;
		}
		
		
		else if (bet_amount > quarters || bet_amount > MAX_BET) 
		//else if (bet_amount > quarters || bet_amount <= 0) { // Adjusted condition
		//This ensures that the bet amount is not only less than or equal to the available quarters
		//but also greater than 0 (to prevent betting 0 quarters).
            printf("Invalid bet. You have %d quarters. Please try again.\n", quarters);
            continue;
		{
			printf("Insufficient balance OR max bet exceeded. Try Again!\n"); /* Fixed the newline */
			continue;
		}

		/* Generate the outcome of the spin */
		outcome = rand() % 100 + 1; /* Random number between 1 and 100 */
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
			quarters += bet_amount; /* Double means getting bet_amount * 2 (adding original back) */
		}
		else
		{
			printf("Jackpot! You triple your money!\n");
			quarters += bet_amount * 2; /* Tripling gives back bet_amount * 3, so add 2 * bet_amount */
		}

		balance = quarters / 4.0; // balance = quarters * 0.25; // Update balance using CREDIT_VALUE
	}

	if (quarters == 0)
	{
		printf("Game Over! You have no more quarters.\n");
	}

	return 0;
}