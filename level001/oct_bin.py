def get_binary_string(n):
    binary_val = ""
    while True:
        binary_val = str(n % 2) + binary_val
        n = int(n / 2)
        if n < 1:
            return binary_val


def to_zeros(s):
    s = "00" + s
    return s[-3:]


num = input()
for idx, oct_val in enumerate(num):
    if idx == 0:
        print(get_binary_string(int(oct_val)), end="")
    else:
        print(to_zeros(get_binary_string(int(oct_val))), end="")

