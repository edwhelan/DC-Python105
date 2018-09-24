list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#print sum of list
index_counter = 0
total_of_num = 0
while index_counter < len(list_of_numbers):
    total_of_num = total_of_num + list_of_numbers[index_counter]
    index_counter += 1
print('This is the total of your list = ' + str(total_of_num))

#print largest number
while index_counter < len(list_of_numbers):
    is_largest = 0
    if list_of_numbers[index_counter] > is_largest:
        is_largest = list_of_numbers[index_counter]
print('This is the largest number in the list = ' + str(is_largest))