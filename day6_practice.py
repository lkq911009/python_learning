from random import randint,choice

def roll_two_dice():
    return (randint(1, 6), randint(1, 6))

def roll_result(dice1, dice2):
    sum_dice = dice1 + dice2
    if sum_dice <= 6:
        return f"The sum of your dice is {sum_dice}. Unfortunate"
    elif sum_dice < 10:
        return f"The sum of your dice is {sum_dice}. You have a good chance"
    else:
        return f"The sum of your dice is {sum_dice}. It looks like a winning roll"

dice1, dice2 = roll_two_dice()
result = roll_result(dice1, dice2)
print(result)

def reduce_list(list_of_numbers):
    reduced_list = []
    max_value = max(list_of_numbers)
    for n in list_of_numbers:
        if n not in reduced_list and n != max_value:
            reduced_list.append(n)
        else:
            pass
    return reduced_list

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
reduced_list = reduce_list(list_of_numbers)
print(f"Original list: {list_of_numbers}")
print(f"Reduced list: {reduced_list}")

def average(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers) if list_of_numbers else 0

secret_codes =['Heads','Tails']

def toss_coin():
    return choice(secret_codes)

print(toss_coin())

def luck(toss_result, secret_code):
    if toss_result == secret_code:
        return "You are lucky today!"
    else:
        return "Better luck next time!"

def number_attributes(**kwargs):
    return len(kwargs.keys())

def describe_person(name,**kwargs):
    print(f'Characteristics of {name}:')
    for key,value in kwargs.items():
        print(f'{key}: {value}')

describe_person("Ash", eye_color="brown", hair_color="black")