def merge_sort_method(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list
list1 = list(map(int, input("Enter the first sorted list: ").split()))
list2 = list(map(int, input("Enter the second sorted list: ").split()))
result = merge_sort_method(list1, list2)
print("Merged list (using sort method):", result)
