#!/bin/bash

# This line decides what the symbols are. I dont actually know if a plum is
# actually used in slots. It just sounded right at the time. 
reel1=("Cherry" "Lemon" "Orange" "Plum" "Bell" "Bar")
reel2=("Cherry" "Lemon" "Orange" "Plum" "Bell" "Bar")
reel3=("Cherry" "Lemon" "Orange" "Plum" "Bell" "Bar")

# Function to spin a single reel
spin_reel() {
    local num_symbols=${#reel1[@]} 
    local index=$((RANDOM % num_symbols))
    echo "${reel1[$index]}" 
}

slot_machine=(
"   .-----------."
"  /  O  O  O  \\"
" |     O     |"
" |  [       ]  |"
"  \\  O  O  O  /"
"   '-----------'"
)

display_reels() {
    local i
    for i in {1..5}; do 
        slot_machine[3]="|  [ $((RANDOM % 10)) ]  |" 
        clear 
        printf "%s\n" "${slot_machine[@]}" 
        sleep 0.3
    done

    result1=$(spin_reel)
    result2=$(spin_reel)
    result3=$(spin_reel)
    slot_machine[3]="|  $result1 $result2 $result3  |"
    clear
    printf "%s\n" "${slot_machine[@]}"
}

# Ze money
declare pay_table
three_of_a_kind_payouts=(0.75 1.50 2.25 3.00)
two_of_a_kind_payouts=(0.25 0.50 0.75 1.00)
cherry_jackpot_payouts=(5.00 10.00 15.00 20.00)

# Money shark loan
balance=10

# Main game
while true; do
    read -p "Choose your bet ($0.25, $0.50, $0.75, $1.00): " bet

    # Deduct bet
    case $bet in
        0.25|0.50|0.75|1.00) 
            balance=$(echo "$balance - $bet" | bc) 
            ;;
        *) 
            echo "Invalid bet amount. Please choose from: $0.25, $0.50, $0.75, or $1.00" 
            continue 
            ;;
    esac

    display_reels

    # Da winning combinations
    if [ "$result1" == "$result2" ] && [ "$result2" == "$result3" ]; then
        if [ "$result1" == "Cherry" ]; then
            winnings=${pay_table[$bet,cherry_jackpot]}
            echo "JACKPOT! You win big! HOLY FUCK Your balance is now: $(echo "$balance + $winnings" | bc)"
        else
            winnings=${pay_table[$bet,three_of_a_kind]}
            echo "Three of a kind! Woo! Your balance is now: $(echo "$balance + $winnings" | bc)"
        fi
    elif [ "$result1" == "$result2" ] || [ "$result1" == "$result3" ] || [ "$result2" == "$result3" ]; then
        winnings=${pay_table[$bet,two_of_a_kind]}
        echo "Two of a kind! Hell yeah! Your balance is now: $(echo "$balance + $winnings" | bc)"
    else
        echo "LOSER! Your balance is now: $balance"
    fi

    balance=$(echo "$balance + $winnings" | bc)

    # Check if you are hella broke or kinda broke
    if (( $(echo "$balance <= 0" | bc -l) )); then
        echo "You're fucking broke! Get a job, Game over."
        break
    fi
done