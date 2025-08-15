# numbers.py
def ticket_message_decorator(func):
    def wrapper():
        ticket_number = func()
        print('\n' + '*' * 23)
        print('Your number is:')
        print(ticket_number)
        print('Please wait for your turn')
        print('*' * 23 + '\n')
        return ticket_number
    return wrapper

def perfume_tickets():
    for n in range(1, 10000):
        yield f'P - {n}'

def medicine_tickets():
    for n in range(1, 10000):
        yield f'M - {n}'

def cosmetic_tickets():
    for n in range(1, 10000):
        yield f'C - {n}'