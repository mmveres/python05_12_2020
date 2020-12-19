def input_int_value():
    while True:
        try:
            value = int(input("Enter int value"))
            break
        except:
            print("Not int, try again")
    return value

def input_mark():
    while True:
        print("enter mark (2<mark<=12)")
        mark = input_int_value()
        if 2 < mark <= 12:
            return mark
        else:
            print("Value not mark, try again")