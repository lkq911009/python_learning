from random import choice,randint
word_list = ['python', 'java', 'javascript', 'hangman', 'challenge', 'programming', 'developer', 'function', 'variable', 'loop', 'condition', 'algorithm']
max_tries = 10

def get_random_word():
    return choice(word_list)

def has_won(secret_word, current_word, trie):
    return secret_word == current_word and trie <= max_tries

def display_init_word(secret_word):
        hints = (secret_word[randint(0, len(secret_word)-1)], secret_word[randint(0, len(secret_word)-1)])
        return [letter if letter in hints else '_' for letter in secret_word]

def replace_match_letters(current_word, guess_letter, secret_word):
   for index, letter in enumerate(secret_word):
       if letter == guess_letter:
           current_word[index] = guess_letter

def display_word(list_of_letters):
    return ''.join(list_of_letters)

def input_a_guess_letter():
    while True:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single letter.")

def hangman_game():
    secret_word = list(get_random_word())
    guessed_letters = set()
    tries = 0
    current_word = display_init_word(secret_word)

    print("Welcome to the Hangman Game!")
    print(f"The secret word has {len(secret_word)} letters.")
    print("Current word:", display_word(current_word))

    while tries < max_tries:
        guess = input_a_guess_letter()
        print(f"\nTries left: {max_tries - tries}")
        print(f"Guessed letters: {guessed_letters}")
        if guess in guessed_letters:
            print(f"You have already guessed the letter '{guess}'. Try again.")
            continue
        guessed_letters.add(guess)
        tries += 1

        if guess in secret_word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            #replace current word with the guessed letter
            replace_match_letters(current_word, guess, secret_word)
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
        if has_won(secret_word, current_word, tries):
            print(f"Congratulations! You've guessed the word: {display_word(current_word)}")
            return
        print(f"Current word: {display_word(current_word)}")

    print(f"Game over! The secret word was: {display_word(secret_word)}")

hangman_game()
