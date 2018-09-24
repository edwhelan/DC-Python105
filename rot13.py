#create of codebreaker for ROT13 cipher
#decipher the following

code_speak = "lbh zhfg hayrnea jung lbh unir yrnearq"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#shift the alphabet -13 
plus_13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

counter = 0
while counter < len(code_speak):
    translate_this = code_speak[counter]
    if translate_this == ' ':
        print(' ', end='')  
    else:
        found_index_value = alphabet.index(translate_this)
        print(plus_13[found_index_value], end='')
    counter += 1


#list[::-13] option to loop around

# while counter < len(code_speak):
    