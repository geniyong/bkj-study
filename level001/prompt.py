n = int(input())
strArr = []
ptr = 0
for i in range(0, n):
    strArr.append(input())
pattern = [0 for i in range(0, len(strArr[0]))]
while ptr < len(strArr[0]):
    base = strArr[0]
    pattern[ptr] = strArr[0][ptr]
    for i in strArr[1:]:
        if base[ptr] != i[ptr]:
            pattern[ptr] = "?"
            break
    ptr += 1
for i in pattern:
    print(i, end="")