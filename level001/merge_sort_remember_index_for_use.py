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