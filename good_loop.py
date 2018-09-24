intab = ['A','E','G','I','O','S','T']
outtab = [4,3,6,1,0,5,7]
# leet_translator = ''
original = "Darth Plageuis"
original = original.upper()
counter = 0

while counter < len(original):
   currentletter = original[counter]
   if original[counter] in intab:
#       original = original.replace(str(intab[counter]),str(outtab[counter]))
       # print('*', end="")
       counter2 = 0
       while counter2 < len(intab):
           lead = intab[counter2]
           if currentletter == lead:
               print(outtab[counter2], end="")
           counter2 += 1
       # print(outtab)

   else:
       print(original[counter], end="")
   counter += 1