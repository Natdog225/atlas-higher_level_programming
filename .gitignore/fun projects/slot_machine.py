import random

# ASCII art for the slot machine
slot_machine = [
    "   .-----------.",
    "  /  O  O  O  \\",
    " |     O     |",
    " |  [       ]  |",
    "  \\  O  O  O  /",
    "   '-----------'"
]

def display_reels(spin_result):
    """
    Displays the slot machine with a spinning animation, then shows the final result.
    """
    for _ in range(5):  # Simulate spinning for a few iterations
        slot_machine[3] = f"|  [ {random.randint(1, 100):3d} ]  |"
        print("\033c", end="")  # Clear the screen (ANSI escape code)
        for line in slot_machine:
            print(line)
        time.sleep(0.3)  # Pause for a brief moment

    # Display the actual spin result
    slot_machine[3] = f"|  [ {spin_result:3d} ]  |"
    print("\033c", end="") 
    for line in slot_machine:
        print(line)


def main():
    """
    The main game loop.
    """

    balance = 20.00  # Starting balance
    credit_value = 0.25

    while True:
        print(f"Your balance: ${balance:.2f} ({balance / credit_value:.0f} credits)")
        bet_input = input("Enter the number of credits to bet (0 to cash out): ")

        try:
            bet_credits = int(bet_input)
            if bet_credits < 0:
                raise ValueError
        except ValueError:
            print("We don't accept trash or pennies. Please enter a positive number of credits or 0 to cash out.")
            continue

        bet_amount = bet_credits * credit_value

        if bet_credits == 0:
            print(f"Cashing out. Your final balance is: ${balance:.2f}")
            break
        elif bet_amount > balance:
            print(f"Insufficient balance. You have {balance / credit_value:.0f} credits.")
            continue

        balance -= bet_amount

        spin_result = random.randint(1, 100)
        display_reels(spin_result)

        if spin_result < 50:
            winnings = 0
            print(f"You lose! Spin result: {spin_result}")
        elif spin_result <= 74:
            winnings = bet_amount
            print(f"You get your bet back! Spin result: {spin_result}")
        elif spin_result < 95:
            winnings = 2 * bet_amount
            print(f"You win double your bet! Spin result: {spin_result}")
        else:
            winnings = 3 * bet_amount
            print(f"You win triple your bet! Spin result: {spin_result}")

        balance += winnings
        print(f"Winnings: ${winnings:.2f}")
        print(f"New balance: ${balance:.2f} ({balance / credit_value:.0f} credits)\n")

if __name__ == "__main__":
    main()