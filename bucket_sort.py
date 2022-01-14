data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]

def bucket_sort(data):
    # 回数を保存するリスト
    counter = [0] * 10
    for i in data:
        counter[i] += 1

    # ソート結果を保存するリスト
    result = []
    for i, num in enumerate(counter):
        if num > 0:
            result.extend([i] * num)
    
    return result

print(bucket_sort(data))