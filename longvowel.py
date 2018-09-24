vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#add 3 vowels to 2 reoccuring vowels
inputed_text = input('What would your like augmented? ')
# loop through word
counter = 0
while counter < len(inputed_text):
    current_letter = inputed_text[counter]
    next_letter = inputed_text[counter-1]
    if current_letter in vowels:
        if current_letter == next_letter:
            print(current_letter * 4, end='')
    else:
        print(current_letter, end='')
    counter += 1
