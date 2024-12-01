data = open('./input.txt', 'r')
all_numbers = tuple(map(int, data.read().split()))
column1, column2 = all_numbers[::2], all_numbers[1::2]
res = sum(max(c1, c2) - min(c1, c2) for c1, c2 in zip(sorted(column1), sorted(column2)))
print(res)
