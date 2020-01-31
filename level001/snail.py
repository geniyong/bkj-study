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

k = [
    [9, 2, 3],
    [8, 1, 4],
    [7, 6, 5]
]

n = int(input())
p = int(input())

# print("입력된 N : {}".format(n))
for step in range(4, n+1):
    # print("현재 STEP : {}".format(step))
    t = [[0] * step for _temp_i in range(step)] # 한 단계 위의 2차원 배열 선언 (step X step)
    # print("임시 배열 : {}".format(t))
    snail_value = (step - 1) * (step - 1) # 달팽이가 지나갈때 남기는 흔적 값
    # print("현재 달팽이 값 : {}".format(snail_value))
    if step % 2 == 0 :
        # 1. 현재 스텝이 짝수 일 때는 [0][j..step]번 라인 0으로 초기화 및 [0..step][step]번 라인 0으로 초기화
        # for j in range(0, step+1):
            # t[0][j] = 0 이미 0으로 초기화된 상태라서 그대로 두면 됨
        # 1번 로직을 구현하는 방식이 아닌 1번 로직을 배제한채로 복사하는 방식으로 구현 함
        for i in range(1, step):
            for j in range(0, step - 1):
                t[i][j] = k[i-1][j] # t 배열에 k 배열을 복사함
        for j in range(0, step):
            snail_value += 1
            t[0][j] = snail_value
        for i in range(1, step):
            snail_value += 1
            t[i][step-1] = snail_value
        k = t
    else:
        for i in range(0, step-1):
            for j in range(1, step):
                t[i][j] = k[i][j-1]
        for j in range(step-1, -1, -1):
            snail_value += 1
            t[step-1][j] = snail_value
        for i in range(step-2, -1, -1):
            snail_value += 1
            t[i][0] = snail_value
        k = t
print_result(k)
x, y = find_val(k, p)
print("{} {}".format(x, y))
