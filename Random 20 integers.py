import random
random_list = [random.randint(1, 100) for _ in range(20)]
print("Random list:", random_list)
average = sum(random_list) / len(random_list)
print("Average:", average)
largest = max(random_list)
smallest = min(random_list)
print(f"Largest: {largest}, Smallest: {smallest}")
sorted_list = sorted(random_list)
second_largest = sorted_list[-2]
second_smallest = sorted_list[1]
print(f"Second largest: {second_largest}, Second smallest: {second_smallest}")
even_count = sum(1 for num in random_list if num % 2 == 0)
print("Number of even numbers:", even_count)
