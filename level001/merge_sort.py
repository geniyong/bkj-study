def merge(L, left, mid, right):
    print("결합 - left: {}, right: {}, L: {}".format(L[left:mid], L[mid:right], L))
    leftArr = L[left:mid]
    rightArr = L[mid:right]
    M = [0 for i in range(0, right-left)]
    i = 0
    ptrL = 0
    ptrR = 0

    while True:
        if ptrL == len(leftArr) or ptrR == len(rightArr):
            if ptrL == len(leftArr):
                while ptrR < len(rightArr):
                    M[i] = rightArr[ptrR]
                    i += 1
                    ptrR += 1
                break

            else:
                while ptrL < len(leftArr):
                    M[i] = leftArr[ptrL]
                    i += 1
                    ptrL += 1
                break

        if leftArr[ptrL] < rightArr[ptrR]:
            M[i] = leftArr[ptrL]
            i += 1
            ptrL += 1
        else:
            M[i] = rightArr[ptrR]
            i += 1
            ptrR += 1

    c = 0
    print("M : {}".format(M))
    for i in M:
        L[left + c] = i
        c += 1
    print("결합 후 L : {}".format(L))


def merge_remember_index(L, IL, left, mid, right):
    print("결합 - left: {}, right: {}, L: {}, IL:{}".format(L[left:mid], L[mid:right], L, IL))
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
    print("M : {}".format(M))
    print("IM : {}".format(IM))
    for i in M:
        L[left + c] = i
        c += 1

    c = 0
    for i in IM:
        IL[left + c] = i
        c += 1
    print("결합 후 L : {}".format(L))
    print("결합 후 IL : {}".format(IL))


def merge_sort(L, left, right):
    print("left: {}, right: {}, L: {}".format(left, right, L[left:right]))
    mid = int((right + left) / 2)
    if left < right-1:
        merge_sort(L, left, mid)
        merge_sort(L, mid, right)
        merge(L, left, mid, right)


def merge_sort_remember_index(L, IL, left, right):
    print("left: {}, right: {}, L: {}".format(left, right, L[left:right]))
    mid = int((right + left) / 2)
    if left < right-1:
        merge_sort_remember_index(L, IL, left, mid)
        merge_sort_remember_index(L, IL, mid, right)
        merge_remember_index(L, IL, left, mid, right)

L = [7,4,15,2,33,9,6,14,1,6]
IL = [0,1,2,3,4,5,6,7,8,9]
# merge_sort(L, 0, len(L))
merge_sort_remember_index(L, IL, 0, len(L))

print("최종 - L: {}, IL: {}".format(L, IL))