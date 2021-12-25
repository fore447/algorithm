N = 8

# 斜めのチェック
def check(y, col):
    # 配置済みの行を逆順に調べる
    for i, row in enumerate(reversed(col)):
        if (y + i + 1 == row) or (y - i - 1 == row):
            return False
    return True

def search(col):
    if len(col) == N: # 全て配置できれば出力
        print(col)
        return

    for y in range(N):
        if y not in col: # 同じ行は使わない
            if check(y, col):
                col.append(y)
                search(col)
                col.pop()

search([])