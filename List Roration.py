def rotate_list(my_list):
 """Rotates the elements of a list so that the last element becomes the first."""
 last_element = my_list[-1]
 for i in range(len(my_list) - 1, 0, -1):
   my_list[i] = my_list[i - 1]
 my_list[0] = last_element
numbers_str = input("Enter a list of numbers separated by spaces: ")
my_list = [int(num) for num in numbers_str.split()]
rotate_list(my_list)
print(f"Rotated list: {my_list}")
