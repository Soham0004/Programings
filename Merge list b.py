def merge_without_sort(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list
list1 = list(map(int, input("Enter the first sorted list: ").split()))
list2 = list(map(int, input("Enter the second sorted list: ").split()))
result = merge_without_sort(list1, list2)
print("Merged list (without using sort method):", result)
