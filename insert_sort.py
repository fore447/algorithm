data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(1, len(data)):
    # 現在の要素を一時的に記録する
    tmp = data[i]
    # 直前の位置を記録する
    j = i - 1
    while (j >= 0) and (data[j] > tmp):
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = tmp
            
print(data)