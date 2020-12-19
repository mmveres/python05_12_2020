def task5():
    # task5
    #  1/30 +...+30/1   chisl/znam
    #
    chisl = 1
    znam = 30
    sum_drob = 0
    for i in range(0, 30, 1):
        sum_drob += chisl / znam
        print(i, " : ", chisl, "/", znam, " : ", sum_drob)
        chisl += 1
        znam -= 1

def print_fill_square(mrow = 10, ncol = 10):
    for i in range(mrow + 1):
        for j in range(ncol + 1):
                print("*", end=" ")
        print()

def print_square(mrow = 10, ncol = 10):
    for i in range(mrow + 1):
        for j in range(ncol + 1):
            if i == mrow or j == 0 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def print_triangle(mrow = 10, ncol = 10):
    for i in range(mrow + 1):
        for j in range(ncol + 1 - i):
            if i == mrow or j == 0 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def menu_main():
    print("1. print fill square")
    print("2. print empty square")
    print("3. print fill triangle")
    print("0. exit")
    answer = input("Enter choice")
    return answer


if __name__ == '__main__':
    while True:
        answer = int(menu_main())
        if answer == 1:
            print_fill_square()
        elif answer == 2:
            print_square()
        elif answer == 3:
            print_triangle()
        elif answer == 0:
            break;