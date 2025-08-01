# Day 4 Challenge: Text Analysis

input_text = input("please input your text: ")
random_letter = input("please input your random 3 letters: ")

letter_list = list(random_letter.replace(" ", ""))
input_text = input_text.lower()

for letter in letter_list:
    print(f"the letter {letter} appears {input_text.count(letter)} times in the text")

input_text_list = list(input_text.split())

print(f"there are {len(input_text_list)} words in the input text")
print(f'the first letter of the text is {input_text[0]}')
print(f'the last letter of the text is {input_text[-1]}')

input_text_list.reverse()
#print the reversed text
print("the reversed text is: ", " ".join(input_text_list))

is_python_word = 'python' in input_text
my_dict = {True: "was", False: "was not"}
print(f'The word "Python" {my_dict[is_python_word]} found in the input text')




