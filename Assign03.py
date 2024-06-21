from random import randint

# Generate values for randint
random1, random2, random3 = (randint(0, 3) for _ in range(3))

# Welcome message of the game
print("\nWelcome to the Lottery Game!\n")

# Get the user input
user_bets = [int(input(f"{bet} Number: ")) for bet in ["First", "Second", "Third"]]

# Print bets and results
print("Your Bets: ", user_bets)
print("Result: ", random1, random2, random3)

# Outcome of the game
if user_bets == [random1, random2, random3]:
    print("\nYou Win!")
elif set(user_bets) == set([random1, random2, random3]):
    print("\nYou Partially Win!")
else:
    print("\nYou Lose!")
