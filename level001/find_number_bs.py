def bs(arr, left, right, x):
    mid = int((left + right) / 2)
    if left < right-1:
        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            return bs(arr, left, mid, x)
        else:
            return bs(arr, mid, right, x)
    else:
        if arr[left] == x:
            return 1
        else:
            return 0


N = int(input())
A = input().split()
M = int(input())
B = input().split()
for idx, i in enumerate(A):
    A[idx] = int(i)
A.sort()

for i in B:
    print(bs(A, 0, N, int(i)))