given_string = input('Please input for translation ')
#uppercase
print(given_string.upper())

#capitalize
print(given_string.capitalize())

#reverse
print(given_string[::-1])
# reversed_string = []
# length_of_given_string = len(given_string)
# while len(reversed_string) < len(given_string):
#     reversed_string.append(length_of_given_string)
#     length_of_given_string

#print l33t h4xor
leet_speak = given_string.replace('a', '4')
leet_speak = leet_speak.replace('e', '3')
leet_speak = leet_speak.replace('g', '6')
leet_speak = leet_speak.replace('l', '1')
leet_speak = leet_speak.replace('o', '0')
leet_speak = leet_speak.replace('s', '5')
leet_speak = leet_speak.replace('t', '7')
print(leet_speak.upper())

# intab =['a', 'e', 'g', 'l', 'o', 's', 't']
# outtab= ['4', '3', '6', '1','0', '5', '7']
# trans_counter = 0
# counter = 0
# while counter < len(given_string):
#     if given_string in intab:
#         given_stri

#print loooong vowels
long_vowels = ''
#if 2 vowels in a row add 4 more
counter = 0
while counter < len(given_string):
    previous_letter = given_string[counter - 1]
    if given_string[counter] == previous_letter:
       given_string = given_string.replace(previous_letter, str(previous_letter * 4))
    counter+=1
print(given_string)

