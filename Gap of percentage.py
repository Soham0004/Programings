L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
gaps = [b - a for a, b in zip(L[:-1], L[1:])]
max_gap = max(gaps)
num_gaps_size_2 = gaps.count(2)
percentage_gaps_size_2 = (num_gaps_size_2 / len(gaps)) * 100
print("Maximum gap size:", max_gap)
print("Percentage of gaps with size 2:", percentage_gaps_size_2, "%")
