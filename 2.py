num_array = [1, 2]
i = 0
while num_array[-1] <= 4000000:
    num_array.append(num_array[i] + num_array[i + 1])
    i += 1
evens = list(filter(lambda x: x % 2 == 0, num_array))
print(sum(evens))
