tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [], []]

# 行きがけ順
# def search(pos):
#     print(pos, end=' ')
#     for i in tree[pos]:
#         search(i)
# search(0)

# 帰りがけ順
# def search(pos):
#     for i in tree[pos]:
#         search(i)
#     print(pos, end=' ')
# search(0)

# 通りがけ順
def search(pos):
    if len(tree[pos]) == 2:
        search(tree[pos][0])
        print(pos, end=' ')
        search(tree[pos][1])
    elif len(tree[pos]) == 1:
        search(tree[pos][0])
        print(pos, end=' ')
    else:
        print(pos, end=' ')
search(0)