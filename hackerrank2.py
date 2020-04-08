bird = int(input().strip())
vid = list(map(int, input().strip().split(' ')))


peremenaya = [0] * bird

for type in vid:
    peremenaya[type] += 1

max_value = -1
max_index = -1
for i in range(bird):
    if peremenaya[i] > max_value:
        max_value = peremenaya[i]
        max_index = i
print(max_index)