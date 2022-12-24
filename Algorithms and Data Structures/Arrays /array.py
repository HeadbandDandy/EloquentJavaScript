#  To test this copy and paste new_list & loop into console


from unittest import result


new_list = [1, 2, 3, 7, 11, 98, 77, 45, 111, 1234, 6571]
result = new_list[0]


if 1 in new_list: print(True)


for n in new_list:
    if n == 1:
        print(True)
        
        break