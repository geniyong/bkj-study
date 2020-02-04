def to_zeros(s):
    if int(s) < 10:
        return '0{}'.format(s)
    else:
        return s

S = to_zeros(input())
cycle = 1
num = S[1] + to_zeros(str(int(S[0]) + int(S[1])))[1]
# print("시작 : {}".format(S))
# print("Cycle {} : {}".format(cycle, num))
while num != S:
    cycle += 1
    num = num[1] + to_zeros(str(int(num[0]) + int(num[1])))[1]
#     print("Cycle {} : {}".format(cycle, num))
# print('{} 의 사이클 길이 : {}'.format(S, cycle))
print(cycle)