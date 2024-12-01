from collections import Counter

data = open('./input.txt', 'r')
all_numbers = tuple(map(int, data.read().split()))
column1, column2 = all_numbers[::2], all_numbers[1::2]
res = sum(n * Counter(column2)[n] for n in column1)
print(res)