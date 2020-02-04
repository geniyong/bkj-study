nums = input().split()
N = int(nums[0])
M = int(nums[1])
if N < M:
    t = N
    N = M
    M = t
print(abs(N - M))