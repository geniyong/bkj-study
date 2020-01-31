al = nl = []


def get_max():
    max_val = 0
    for i in nl:
        if max_val < i:
            max_val = i
    max_len = 0
    for i in nl:
        if i == max_val:
            max_len += 1
    if max_len > 1:
        return "?"
    else:
        return al[nl.index(max_val)]


nl = [0] * 100
word = input()
for a in word:
    large_alphabet = a.upper()
    try:
        idx = al.index(large_alphabet)
    except:
        al.append(large_alphabet)
        idx = al.index(large_alphabet)
    nl[idx] += 1

print(get_max())
