print("Практическая работа №1.\nCalculator")
InputFirst = int(input("INPUT 1: "))

while(True):
    try:
        InputSecond = int(input("INPUT 2: "))
        print("Choose an action")
        print("1. Addition \t\t\t'+'\n2. Subtraction \t\t\t'-'\n3. Multiplication  \t\t'*'\n4. Division \t\t\t'/'"
              "\n5. Expanding \t\t\t'**'\n6. Remainder of division '%'\n7. Reset\nEnter the sequence number of the action!")
        action = input()

        print("Output: ")
        match action:
            case '1':
                InputFirst = InputFirst + InputSecond
                print(InputFirst)
            case '2':
                InputFirst = InputFirst - InputSecond
                print(InputFirst)
            case '3':
                InputFirst = InputFirst * InputSecond
                print(InputFirst)
            case '4':
                if InputSecond == 0:
                    print("the operation cannot be performed!\nIt is not possible to divide by zero...")
                else:
                    InputFirst = InputFirst / InputSecond
                    print(InputFirst)
            case '5':
                InputFirst = InputFirst ** InputSecond
                print(InputFirst)
            case '6':
                InputFirst = InputFirst % InputSecond
                print(InputFirst)
            case '7':
                InputFirst = 0
                print("the value has been reset:", InputFirst)
                InputFirst = int(input("INPUT 1: "))
            case _:
                print("There is no such action")
    except:
        print("Value error")


