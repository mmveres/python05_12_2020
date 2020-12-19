from ua.univer.lesson03.exception.data_verify import input_int_value, input_mark

if __name__ == '__main__':
    x = input_int_value()
    y = input_int_value()

    sum = x+y
    print("sum =", sum)

    mark = input_mark()
    print("mark =", mark)