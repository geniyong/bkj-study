num = int(input())
dl = input().split()
for idx, i in enumerate(dl):
    dl[idx] = int(i)
dl.sort()
if num % 2 == 0:
    N = int(dl[0]) * int(dl[num-1])
else:
    N = int(dl[int(num/2)]) * int(dl[int(num/2)])
print(N)