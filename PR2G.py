print("ПРАКТИЧЕСКАЯ РАБОТА №2")
a = int(input("Год: "))

def DaysSum(x):
    d = 0
    for i in range(x+1):
        if i<10:
            d = d + i
        else:
            hh = str(i)
            h = list(hh)
            d = d + int(h[0]) + int(h[1])
    return d

try:
    if(a%4==0):
        print("Это високосный год")
        b = DaysSum(31) * 7 + DaysSum(30) * 4 + DaysSum(29)
        print("Сумма: ", b)
    else:
        print("Это невисокосный год")
        b = DaysSum(31) * 7 + DaysSum(30) * 4  + DaysSum(28)
        print("Сумма: ", b)
except:
    print("Данные введены неверно")


