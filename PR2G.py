print("ПРАКТИЧЕСКАЯ РАБОТА №2\nВведите год:")
Year = int(input())

def DaysSum(Days):
    temp = 0
    for i in range(Days + 1):
        if i<10:
            temp = temp + i
        else:
            Daysstr = str(i)
            Dayssymb = list(Daysstr)
            temp = temp + int(Dayssymb[0]) + int(Dayssymb[1])
    return temp

if(Year%4==0 and Year%400==0 or Year%100!=0):
    print("Это високосный год")
    SumCounter = DaysSum(31) * 7 + DaysSum(30) * 4 + DaysSum(29)
    print("Сумма: ", SumCounter)
else:
    print("Это невисокосный год")
    SumCounter = DaysSum(31) * 7 + DaysSum(30) * 4 + DaysSum(28)
    print("Сумма: ", SumCounter)