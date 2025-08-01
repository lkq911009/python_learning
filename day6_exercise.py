def count_primes(n):
    count = 0
    if n < 2:
        return 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

print(count_primes(100))

def print_non_repeating_characters(s):
    seen = set()
    for char in s:
        if char not in seen and char != ' ':
            seen.add(char)
    return list(seen)

print(print_non_repeating_characters("hello world"))

def consicutive_zeros(*args):
    count = 0
    for num in args:
        if num == 0:
            count += 1
            if count > 1:
                return True
        else:
            count = 0
    return False
print(consicutive_zeros(0, 1, 0, 2, 0))  # True
print(consicutive_zeros(0, 0, 0, 2, 1))

def return_distincts(num1, num2, num3):
    sum_total = num1 + num2 + num3
    if sum_total > 15:
        return max(num1, num2, num3)
    elif sum_total < 10:
        return min(num1, num2, num3)
    else:
        return immediate(num1, num2, num3)

def immediate(num1, num2, num3):
    return num1 if num1 != num2 and num1 != num3 else (num2 if num2 != num1 and num2 != num3 else num3)