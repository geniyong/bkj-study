def print_result(rs):
    for i in rs:
        for index_j, j in enumerate(i):
            print(j, end=" ")
            if index_j % len(i) == len(i) - 1:
                print("")

def find_val(arr, val):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n):
            if arr[i][j] == val:
                return i+1, j+1


n = int(input())
p = int(input())
k = [[-1]* n for i in range(n)]
snail_value = (n * n) + 1
if n % 2 == 0:
    ci = cj = n-1
    while snail_value > 1:
        # 위로
        while True:
            if k[ci][cj] == -1:
                snail_value -= 1
                k[ci][cj] = snail_value
            if ci-1 < 0 or k[ci-1][cj] != -1:
                cj -= 1
                break
            ci -= 1

        # 왼쪽으로
        while True:
            if k[ci][cj] == -1:
                snail_value -= 1
                k[ci][cj] = snail_value
            if cj-1 < 0 or k[ci][cj-1] != -1:
                ci += 1
                break
            cj -= 1

        # 아래로
        while True:
            if k[ci][cj] == -1:
                snail_value -= 1
                k[ci][cj] = snail_value
            if ci >= n-1 or k[ci+1][cj] != -1:
                cj += 1
                break
            ci += 1

        # 오른쪽으로
        while True:
            if k[ci][cj] == -1:
                snail_value -= 1
                k[ci][cj] = snail_value
            if cj >= n - 1 or k[ci][cj + 1] != -1:
                ci -= 1
                break
            cj += 1
else:
    ci = cj = 0
    while snail_value > 1:
        # 아래로
        while True:
            if k[ci][cj] == -1:
                snail_value -= 1
                k[ci][cj] = snail_value
            if ci >= n - 1 or k[ci + 1][cj] != -1:
                cj += 1
                break
            ci += 1

        # 오른쪽으로
        while True:
            if k[ci][cj] == -1:
                snail_value -= 1
                k[ci][cj] = snail_value
            if cj >= n - 1 or k[ci][cj + 1] != -1:
                ci -= 1
                break
            cj += 1

        # 위로
        while True:
            if k[ci][cj] == -1:
                snail_value -= 1
                k[ci][cj] = snail_value
            if ci-1 < 0 or k[ci-1][cj] != -1:
                cj -= 1
                break
            ci -= 1

        # 왼쪽으로
        while True:
            if k[ci][cj] == -1:
                snail_value -= 1
                k[ci][cj] = snail_value
            if cj-1 < 0 or k[ci][cj-1] != -1:
                ci += 1
                break
            cj -= 1
print_result(k)
x, y = find_val(k, p)
print("{} {}".format(x, y))