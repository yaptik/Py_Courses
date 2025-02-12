# # Home Work 3.3.
# list = []
#
# array_size = int(input("Enter the number of array elements: "))
#
# for i in range(array_size):  # Loop for array input.
#     user_input = int(input(f" Enter element # {i+1}-->"))
#     list.append(user_input)
#
# print("Array before sorting-->", list)
# swapped = True
#
# while swapped:  # Loop for sorting.
#     swapped = False
#     for i in range(len(list)-1):
#         if list[i] > list[i+1]:
#             swapped= True
#             list[i], list[i+1] = list[i+1], list[i]
#
# print("Array after sorting -->", list)
# list.reverse()
# print("Array after reverse -->", list)
#
# # Home Work 3.5.
# my_list = [int(value) for value in input("Enter values: ").split()]
# my_list = sum(my_list)  # Function, sum of sequence.
# print("Sum of list elements = ", my_list)
