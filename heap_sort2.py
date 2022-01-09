def heapify(data, i):
    left = 2*i+1
    right = 2*i+2
    size = len(data)-1
    min = i
    """
    親ノードが子ノードよりも大きいかどうかを確認する。
    親ノードの方が大きければ、親ノードと子ノードの値を交換し、
    その子ノードの子ノードの大小関係を再起的に並び替える
    """
    if left <= size and data[min] > data[left]:
        min = left
    if right <= size and data[min] > data[right]:
        min = right
    if min != i:
        data[i], data[min] = data[min], data[i]
        heapify(data, min)

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
# ヒープを構成
for i in reversed(range(len(data) // 2)):
    heapify(data, i)

# ソートを実行
sorted_data = []
for _ in range(len(data)):
    data[0], data[-1] = data[-1], data[0]
    sorted_data.append(data.pop())
    heapify(data, 0)

# 別解
# for _ in range(len(data)-1):
#     data[0], data[-1] = data[-1], data[0]
#     sorted_data.append(data.pop())
#     heapify(data, 0)
#     if len(data) == 1:
#         sorted_data.append(data.pop())

print(sorted_data)