#! Программа Обменный пункт


def currency_office():
    while True:
        print("Для выхода нажмите Y")
        data = input("Введите сумму для обмена: ")
        if data.lower() == "y":
            break  # выход из цикла
        money = float(data)
        if money < 0:
            print("error, enter positive value")
            continue

        cache = round(money / 28.5, 2)
        print("К выдаче", cache, "долларов")

    print("Работа обменного пункта завершена")