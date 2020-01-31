bl = []
temp_list = []
oct_val_list = []
b = input()
for i in b:
    bl.append(int(i))
bl.reverse()
for idx, i in enumerate(bl):
    temp_list.append(i)
    if idx % 3 == 2:
        oct_val_list.append(temp_list[0] + temp_list[1] * 2 + temp_list[2] *4)
        temp_list = []
if temp_list:
    temp_val = 0
    for idx, i in enumerate(temp_list):
        temp_val += pow(2, idx) * temp_list[idx]
    oct_val_list.append(temp_val)
oct_val_list.reverse()
result = ""
for i in oct_val_list:
    result += str(i)
print(result)