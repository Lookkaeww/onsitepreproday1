"""เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
def main():
    """เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
    money1 = int(input())
    water = int(input())
    snk1 = int(input())
    snk2 = int(input())
    snk3 = int(input())
    some1 = money1-water
    some2 = some1%3
    if some1 >= 27:
        def snkk1(some22):
            if some2 == 0:
                cal1 = some1-snk1*10
                print("Snack number 1: %d baht"%cal1)
            elif some2 == 1:
               cal1 = some1-snk1*15
               print("Snack number 1: %d baht"%cal1)
            elif some2 == 2:
                cal1 = some1-snk1*20
                print("Snack number 1: %d baht"%cal1)
            else:
                print("You don't have enough money!")
        def snkk2(call1):
            if call1 >= 12:
                some3 = call1%3
                if some3 == 0:
                    cal2 = call1-snk2*12
                    print("Snack number 2: %d baht"%cal2)
                elif some3 == 1:
                    cal2 = call1-snk2*15
                    print("Snack number 2: %d baht"%cal2)
                elif some3 == 2:
                    cal2= call1-snk2*18
                    print("Snack number 2: %d baht"%cal2)
                else:
                    print("You don't have enough money!")
        def snkk3(call2):
            if call2 >=5:
                some4 = call2%3
                if some4 == 0:
                    cal3 = call2-snk3*5
                    print("Snack number 3: %d baht"%cal3)
                elif some4 == 1:
                    cal3 = call2-snk3*7
                    print("Snack number 3: %d baht"%cal3)
                elif some4 == 2:
                    cal3 = call2-snk3*9
                    print("Snack number 3: %d baht"%cal3)
                else:
                    print("You don't have enough money!")
    else:
        print("You don't have enough money!")
snkk1(some