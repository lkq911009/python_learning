from random import randint
user_name = input("What is your name? ")
print(f'Hello {user_name}, welcome to the number guessing game! please guess a number between 1 and 100')

random_number = randint(1, 100)
def get_valid_guess(prompt):
    while True:
        try:
            guess = int(input(prompt))
            return guess
        except ValueError:
            print("请输入一个有效的整数！")

input_guess = get_valid_guess("Guess a number between 1 and 100: ")
max_tries = 8

while max_tries > 0:
    if input_guess > 100 or input_guess < 1:
        print("Your guess is out of range. Please guess a number between 1 and 100.")
        input_guess = get_valid_guess("Guess again: ")
        continue
    elif input_guess == random_number:
        print(f"Congrats {user_name}, you guessed the number in {random_number}")
        break
    elif input_guess < random_number:
        print(f"Your guess {input_guess} is too low. You have {max_tries - 1} tries left.")
        max_tries -= 1
        input_guess = get_valid_guess("Guess again: ")
    else:
        print(f"Your guess {input_guess} is too high. You have {max_tries - 1} tries left.")
        max_tries -= 1
        input_guess = get_valid_guess("Guess again: ")
else:
    print(f"Sorry {user_name}, you have used all your tries. The number was {random_number}. Better luck next time!")

print("Thank you for playing the number guessing game!")