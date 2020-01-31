long_month = [1, 3, 5, 7, 8, 10, 12]
short_month = [4, 6, 9, 11]
day_str = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
s = input().split(' ')
month = int(s[0])
day = int(s[1])
days = 0
for i in range(1, month):
    if i in long_month:
        days += 31
    elif i in short_month:
        days += 30
    elif i == 2:
        days += 28
days += day
print(day_str[days % 7])