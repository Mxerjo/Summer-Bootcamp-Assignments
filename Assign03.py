from random import randint

print("\nWelcome to the Lottery Game!\n")

result_1 = randint(0, 9)
result_2 = randint(0, 9)
result_3 = randint(0, 9)

user_bet1 = int(input("First Bet Number: "))
user_bet2 = int(input("Second Bet Number: "))
user_bet3 = int(input("Third Bet Number: "))

print("Bet: ", user_bet1, user_bet2, user_bet3)
print("Result: ", result_1, result_2, result_3)

if user_bet1 == result_1 and user_bet2 == result_2 and user_bet3 == result_3:
    print("\nYou Win!")

elif(user_bet1 == result_1 and user_bet2 == result_3 and user_bet3 == result_2) or \
    (user_bet2 == result_3 and user_bet2 == result_1 and user_bet3 == result_2) or \
    (user_bet1 == result_2 and user_bet2 == result_1 and user_bet3 == result_3) or \
    (user_bet1 == result_3 and user_bet2 == result_1 and user_bet3 == result_2):
    print("\nYou Partially Win!")

else:
    print("\nYou Lose!")
