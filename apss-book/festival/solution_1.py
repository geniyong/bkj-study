n = int(input())
min_val_list = []
for X in range(0, n):
    n_m_inputs = list(map(int, str(input()).split()))
    N = n_m_inputs[0] # 공연장 대여 비용 배열 개수 N
    L = n_m_inputs[1] # 먼저 섭외된 L 개의 팀
    cost_list = list(map(int, str(input()).split()))
    min_val = 9999
    for i in range(L, N+1):
        for j in range(0, (N-i)+1):
            sum = 0
            for k in range(j, j+i):
                sum += cost_list[k]

            if sum/i < min_val:
                min_val = sum/i
    min_val_list.append(min_val)
for v in min_val_list:
    print(v)