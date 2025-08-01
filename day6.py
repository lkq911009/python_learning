from random import shuffle
dic = {'key1': 100, 'key2': 200, 'key3': 300}

item = dic.popitem()

print(item)

print(dic)

s = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

print(s.lstrip(',:%_#'))

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3, 'orange')

print(fruits)

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolated_sets = phone_brands.isdisjoint(tv_brands)
print(isolated_sets)

def test_function(name):
    print(f'Hello, {name}!')

test_function("Alice")

word = 'Python'

def reverse_word(word):
    return word[::-1].upper()
reversed_word = reverse_word(word)
print(reversed_word)

def check_3_digit(list_of_numbers):
    for n in list_of_numbers:
        if n not in range(100, 1000):
            continue
        else:
            return True

    return False

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

result = check_3_digit(list_of_numbers)
print(f"Does the list contain a 3-digit number? {result}")

def find_3_digit_numbers(list_of_numbers):
    three_digit_numbers = []
    for n in list_of_numbers:
        if n in range(100, 1000):
            three_digit_numbers.append(n)
    return three_digit_numbers

sticks_holder = ['-','--','---','----']

def mix_sticks(sticks):
    shuffled_sticks = sticks.copy()
    shuffle(shuffled_sticks)
    return shuffled_sticks

def pick_a_stick():
    while True:
        try:
            usr_input = int(input("Please pick a stick (1-4): "))
            if usr_input not in range(1, 5):
                continue
            return usr_input - 1  # Adjust for zero-based index
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def stick_game(mix_sticks):
    print("Welcome to the Stick Game!")
    user_guess = pick_a_stick()

    if mix_sticks[user_guess] == '-':
        print('You loss, take the bet')
    else:
        print(f'You win, you picked {mix_sticks[user_guess]}')
    print("Game Over!")

stick_game(mix_sticks(sticks_holder))


