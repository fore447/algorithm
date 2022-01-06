data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data) - 1):
    min_idx = i
    for j in range(i + 1, len(data)):
        if data[min_idx] > data[j]:
            min_idx = j
        
    data[i], data[min_idx] = data[min_idx], data[i]

print(data)

# target = 0
# while target < len(data)-1:
#     min_idx = target
#     for i in range(target+1, len(data)):
#         if data[min_idx] > data[i]:
#             min_idx = i
#     tmp = data[min_idx]
#     data[min_idx] = data[target]
#     data[target] = tmp
#     target += 1