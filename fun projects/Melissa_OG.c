#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main () 
{
int balance = 20;
float quarter_amount = 80.0;
int bet_amount = 0;                //These are a mess. No idea why you have some of them. 
int = random_number;
int x = 1;


    while (x==1) {
    printf ("Welcome to the Betting Game");
    printf ("You have $%.2d in quarters./n", balance);
    printf ("/n");

    printf ("Enter the number of quarters to bet (or '0' to cash out):  ");
    scanf("%d, &bet_amount"); // Ya need some error handling and the actual format could be fixed.  
	//if (scanf("%d", &bet_amount) != 1)
	//printf("Invalid input. Please enter a number.\n");
//            while (getchar() != '\n'); // Clear input buffer
  //          continue;          //Go back to the start of the loop and try again

if (bet_amount==0) {
    printf ("Cashing out.You ended with $%.2d.\n", balance);
    break;
}

if (bet_amount > balance) {
    printf("Insufficient balance. Please try again.\n");
    continue;
}
//This leaves room for error just based on what if it's exactly the balance? And you dont manually put 0
//if (bet_amount == 0) {
//            printf("Cashing out. You ended with $%.2f.\n", balance);
//            break;
//        } else if (bet_amount > quarters || bet_amount <= 0) { // Adjusted condition for bet validation
//            printf("Invalid bet. You have %d quarters. Please try again.\n", quarters);
//            continue; // Go back to the start
//        }


random_number = rand() % 100 + 1;
printf("Reel Stopped on the number: %d\n", random_number); //kinda nitpicky but I'd name this variable, Winning_num 
// or outcome for readibility

    if (random_number <50) {
        printf("You lose!\n");
        balance -= bet_amount;
    } else if (random_number >=50 && random_number <= 74) {
      printf("(You get your money back!");
    } else if (random_number >= 75 && random_number <= 94) {
        printf("You double your money!\n");
        balance += bet_amount;
    } else { 
        printf("Jackpot! You tripled your money!\n");
        balance += bet_amount * 3;
    }

    printf ("You have $%.2d remaining."); 
	//balance = quarters * 0.25; // Convert quarters back to dollars using CREDIT_VALUE
	//   printf("Your new balance is: $%.2f (%d quarters)\n\n", balance, quarters); // Added to show updated balance

    if (balance <= 0) {
      printf("Game Over\n"); //This would need to be in the loop cause you need a break after it right? 
}
return 0;

}