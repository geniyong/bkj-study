def switch_hex_to_decimal(_hex):
    try:
        if _hex.upper() == 'A':
            return 10
        elif _hex.upper() == 'B':
            return 11
        elif _hex.upper() == 'C':
            return 12
        elif _hex.upper() == 'D':
            return 13
        elif _hex.upper() == 'E':
            return 14
        elif _hex.upper() == 'F':
            return 15
    except:
        pass
    return None

hl = []
h = input()
for i in h:
    hl.append(i)
hl.reverse()
val = 0
for idx, i in enumerate(hl):
    try:
        each_val = int(i)
    except:
        each_val = switch_hex_to_decimal(i)
    val += pow(16, idx) * each_val
print(val)