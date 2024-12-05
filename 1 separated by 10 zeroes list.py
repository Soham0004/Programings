ones_list = [1] * 2
num_zeros = 1
while num_zeros <= 10:
 ones_list.extend([0] * num_zeros + [1])
 num_zeros += 1
print(ones_list)
