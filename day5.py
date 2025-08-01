age = 16
has_license = False

"You can drive"

"You can't drive yet. You must be 18 years old and have a license"

"You can't drive. You need to have a license"

if age >= 18 and has_license:
    print("You can drive")
elif age >= 18 and not has_license:
    print("You can't drive. You need to have a license")
else:
    print("You can't drive yet. You must be 18 years old and have a license")


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_even = 0

sum_odd = 0

for number in list_numbers:
    if number % 2 == 0:
        sum_even = sum_even + number
    else:
        sum_odd = sum_odd + number

print(f'sum_even is {sum_even} and sum_odd is {sum_odd}')


number = 50

while number >= 0:
    if number % 5 == 0:
        print(number)
        number = number - 1
    else:
        number = number - 1
