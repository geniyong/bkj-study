def merge_remember_index(L, IL, left, mid, right):
    leftArr = L[left:mid]
    rightArr = L[mid:right]
    leftIndexArr = IL[left:mid]
    rightIndexArr = IL[mid:right]
    M = [0 for i in range(0, right-left)]
    IM = [0 for i in range(0, right-left)]
    i = 0
    ptrL = 0
    ptrR = 0

    while True:
        if ptrL == len(leftArr) or ptrR == len(rightArr):
            if ptrL == len(leftArr):
                while ptrR < len(rightArr):
                    M[i] = rightArr[ptrR]
                    IM[i] = rightIndexArr[ptrR]
                    i += 1
                    ptrR += 1
                break

            else:
                while ptrL < len(leftArr):
                    M[i] = leftArr[ptrL]
                    IM[i] = leftIndexArr[ptrL]
                    i += 1
                    ptrL += 1
                break

        if leftArr[ptrL] < rightArr[ptrR]:
            M[i] = leftArr[ptrL]
            IM[i] = leftIndexArr[ptrL]
            i += 1
            ptrL += 1
        else:
            M[i] = rightArr[ptrR]
            IM[i] = rightIndexArr[ptrR]
            i += 1
            ptrR += 1

    c = 0
    for i in M:
        L[left + c] = i
        c += 1

    c = 0
    for i in IM:
        IL[left + c] = i
        c += 1


def merge_sort_remember_index(L, IL, left, right):
    mid = int((right + left) / 2)
    if left < right-1:
        merge_sort_remember_index(L, IL, left, mid)
        merge_sort_remember_index(L, IL, mid, right)
        merge_remember_index(L, IL, left, mid, right)


N = int(input())
A = input().split()
M = int(input())
B = input().split()

# N = 10
# A = [7,4,15,2,33,9,6,14,1,6]
# B = [14, 14, 14, 14, 14, 14]
# M = len(B)

IndexArrA = [i for i in range(N)]
IndexArrB = [i for i in range(M)]

for idx, i in enumerate(A):
    A[idx] = int(i)

for idx, i in enumerate(B):
    B[idx] = int(i)

merge_sort_remember_index(A, IndexArrA, 0, N)
merge_sort_remember_index(B, IndexArrB, 0, M)

ptrA = ptrB = 0
ResultArr = [0 for i in range(M)]
while ptrA < len(A):
    if ptrB == len(B):
        break
    if A[ptrA] == B[ptrB]:
        ResultArr[IndexArrB[ptrB]] = 1
        ptrB += 1
    elif A[ptrA] < B[ptrB]:
        ptrA += 1
    else:
        ptrB += 1
# print("A: {}\nB: {}\nIB: {}\nRS: {}".format(A, B, IndexArrB, ResultArr))
for i in ResultArr:
    print(i)
