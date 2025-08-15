def decorate_function(func):
    def wrapper(text):
        print("hello")
        func(text)
        print("goodbye")
    return wrapper

def uppercase(text):
    print(text.upper())

@decorate_function
def lowercase(text):
    print(text.lower())

lowercase('Hello World')

another_function = decorate_function(uppercase)
another_function('Hello World')

