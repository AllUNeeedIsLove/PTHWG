print("ПРАКТИЧЕСКАЯ РАБОТА №2")
a = int(input("Год: "))

def DaysSum(Days):
    temp = 0
    for i in range(Days + 1):
        if i<10:
            temp = temp + i
        else:
            ff = str(i)
            f = list(ff)
            temp = temp + int(f[0]) + int(f[1])
    return temp

try:
    if(a%4==0):
        print("Это високосный год")
        SumCounter = DaysSum(31) * 7 + DaysSum(30) * 4 + DaysSum(29)
        print("Сумма: ", SumCounter)
    else:
        print("Это невисокосный год")
        SumCounter = DaysSum(31) * 7 + DaysSum(30) * 4 + DaysSum(28)
        print("Сумма: ", SumCounter)
except:
    print("Данные введены неверно")


