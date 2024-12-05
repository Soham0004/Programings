numbers = input("Enter a list of integers separated by spaces: ").split()
my_list = [int(num) for num in numbers]
print("Total items:", len(my_list))
print("Last item:", my_list[-1])
print("List in reverse:", my_list[::-1])
contains_five = 5 in my_list
print("Yes")
five_count = my_list.count(5)
print("Number of fives:", five_count)
del my_list[0]
del my_list[-1]
my_list.sort()
print("List after removing first/last and sorting:", my_list)
less_than_five_count = sum(i < 5 for i in my_list)
print("Number of integers less than 5:", less_than_five_count)
