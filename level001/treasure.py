def get_max(arr):
    ptr = 1
    max = arr[0]
    while ptr < len(arr):
        if arr[ptr] > max:
            max = arr[ptr]
        ptr += 1
    return max


n = int(input())
A = input().split()
B = input().split()
T = [-1 for i in range(0, n)]
R = [-1 for i in range(0, n)]
for idx, i in enumerate(A):
    A[idx] = int(i)
for idx, i in enumerate(B):
    T[idx] = int(i)
    B[idx] = int(i)
A.sort()
if n == 1:
    print(A[0] * B[0])
else:
    ptr = 0
    while ptr < n:
        max_val = get_max(T)
        mi = T.index(max_val)
        R[mi] = A[ptr]
        T[mi] = -1
        ptr += 1

    sum = 0
    for i in range(0, n):
        sum += R[i] * B[i]
    print(sum)