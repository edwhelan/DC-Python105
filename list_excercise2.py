list_of_numbers = [1, 2, 3, 4, 55, -2, 6, 7, 8, 9, 10]
index_counter = 0
#print largest in list
is_largest = 0
while index_counter < len(list_of_numbers):
    if list_of_numbers[index_counter] > is_largest:
        is_largest = list_of_numbers[index_counter]
    index_counter += 1
print('This is the largest number in the list = ' + str(is_largest))

#print the smallest in list
index_counter = 0

is_smallest = 100000000000000000
while index_counter < len(list_of_numbers):
    if list_of_numbers[index_counter] < is_smallest:
        is_smallest = list_of_numbers[index_counter]
    index_counter += 1
print('This is the smallest number in the list = ' + str(is_smallest))


# print number if its even
index_counter = 0
is_even_num = ''
while index_counter < len(list_of_numbers):
    if list_of_numbers[index_counter] % 2 == 0:
        is_even_num = is_even_num + ' ' + str(list_of_numbers[index_counter])
    index_counter += 1    
print('These numbers are even = ' + str(is_even_num))

# print positive numbers print
index_counter = 0
is_pos_num = ''
while index_counter < len(list_of_numbers):
    if list_of_numbers[index_counter] > 0:
        is_pos_num = is_pos_num + ' ' + str(list_of_numbers[index_counter])
    index_counter += 1    
print('These numbers are positive = ' + str(is_pos_num))

#given a list of numbers create new list of numbers containing positive numbers
index_counter = 0
is_pos_num_list = []
while index_counter < len(list_of_numbers):
    if list_of_numbers[index_counter] > 0:
        is_pos_num_list.append(list_of_numbers[index_counter])
    index_counter += 1    
print(is_pos_num_list)

# given a list of numbers and a single factor, 
# create a new list consisting of each of numbers multiplied by the given. 

index_counter = 0
the_factor = 5
list_times_factor = []
while index_counter < len(list_of_numbers):
    #current list[x] * our factor
    big_num = list_of_numbers[index_counter] * the_factor
    list_times_factor.append(big_num)
    index_counter += 1    
print(list_times_factor)

multiply_list1 = [2, 3, 5]
multiply_list2 = [3, 5, 10]
list_times_list = []
index_counter = 0
while index_counter < len(multiply_list1):
#   current number for list1[x] * list2[x]
    current_num = multiply_list1[index_counter] * multiply_list2[index_counter]
    list_times_list.append(current_num)
    index_counter += 1
print(list_times_list)

#add 2 lists in 1 list with the same index
matroska_list = [[1, 3, 2, 4], [5, 2, 1, 0]]
new_list = []
index_counter = 0
second_index_counter = 0
while second_index_counter < len(matroska_list[1]):
    current_num = matroska_list[0][second_index_counter] + matroska_list[1][second_index_counter]
    new_list.append(current_num)
    second_index_counter += 1
print(new_list)

#de-dup a list of any duplicate values

# index_counter = 0
# while index_counter < len(dup_list):
#     if dup_list[index_counter] in dup_list:
#        dup_list.pop(current_val)
#     index_counter += 1
# print(dup_list)

dup_list = [2, 5, 6, 8, 2, 'cheese', 'bread', 'milk', 'bread']
dup_free_list = []
#improved 
index_counter = 0

while index_counter < len(dup_list):
    #   second_index_counter = 0
    if dup_list[index_counter] not in dup_free_list:
        dup_free_list.append(dup_list[index_counter])
    index_counter += 1
print(dup_free_list)