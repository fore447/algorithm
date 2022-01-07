data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 別解
# for i in range(len(data)-1, 0, -1):
#     for j in range(i):

# 配列の要素が交換されたかどうかを示すフラグ
is_changed = True
for i in range(len(data)-1):
    # 配列の要素の交換が起こらなければ終了する
    if not is_changed:
        break
    is_changed = False
    for j in range(len(data)-1-i):
        # 配列の隣同士を比較する
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            is_changed = True
print(data)