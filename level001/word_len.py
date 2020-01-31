s = input()
sl = s.split(' ')
for i in sl:
    if not i:
        sl.remove(i)
if not sl[0]:
    print(0)
else:
    print(len(sl))