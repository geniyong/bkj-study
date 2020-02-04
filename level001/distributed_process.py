cases = int(input())
for case in range(0, cases):
    S = input().split()
    a = int(S[0])
    b = int(S[1])
    cycle = [int(S[0])]
    if a % 10 == 0:
        print(10)
    else:
        while True:
            a *= int(S[0])
            if cycle[0] % 10 != a % 10:
                cycle.append(a)
            else:
                break
        if b == 1:
            print(cycle[0] % 10)
        else:
            print(cycle[(b-1) % len(cycle)] % 10)