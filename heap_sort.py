data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# (親ノード >= 子ノード）のヒープを構成
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2]
        j = (j - 1) // 2

# data = [15, 13, 11, 8, 9, 4, 5, 2, 7, 6]
# ソートを実行する
for i in range(len(data)-1, 0, -1):
    # ヒープの先頭と交換
    data[i], data[0] = data[0], data[i]
    print(data)
    j = 0
    # 子ノードの方が大きい場合
    while ((2*j+1 < i) and (data[j] < data[2*j+1]))\
      or ((2*j+2 < i) and (data[j] < data[2*j+2])):
        # 左側の子ノードがソート済み、存在しない場合。または、左側の子ノードの方が大きい場合。
        if (2*j+2 == i) or (data[2*j+1] > data[2*j+2]):
            # 左側の子ノードと交換
            data[j], data[2*j+1] = data[2*j+1], data[j]
            # 左下に移動
            j = 2*j+1
        else:
            # 右側の子ノードと交換
            data[j], data[2*j+2] = data[2*j+2], data[j]
            # 右下に移動
            j = 2*j+2
        
print(data)