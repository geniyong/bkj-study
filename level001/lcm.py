def get_gcd(x, y):
    if x < y:
        t = x
        x = y
        y = t
    while y > 0:
        t = x % y
        x = y
        y = t
    return x


def get_gcd_i(x, y):
    cd_list = []
    cnt = 1
    gcd = 1
    if x < y:
        t = x
        x = y
        y = t
    while True:
        if y < cnt:
            break
        if y % cnt == 0:
            cd_list.append(cnt)
        cnt += 1
    cd_list.reverse()
    for cd in cd_list:
        if x % cd == 0:
            gcd = cd
            break
    return gcd


c = 0
n = int(input())
while True:
    if c == n:
        break
    s = input().split(' ')
    x = int(s[0])
    y = int(s[1])
    gcd = get_gcd_i(x, y)
    lcm = int(x * y / gcd)
    print(lcm)
    c += 1
    # print('최대공약수 : {}'.format(gcd))
    # print('최소공배수 : {}'.format(lcm))
