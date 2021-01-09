import csv
def csv_dict_example():
    FILENAME = "users.csv"

    users = [
        {"name": "Tom", "age": 28},
        {"name": "Alice", "age": 23},
        {"name": "Bob", "age": 34}
    ]

    with open(FILENAME, "w", newline="") as file:
        columns = ["name", "age"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        # запись нескольких строк
        writer.writerows(users)

        user = {"name" : "Sam", "age": 41}
        # запись одной строки
        writer.writerow(user)

    with open(FILENAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["name"], "-", row["age"])
if __name__ == '__main__':
    with open("rozrakhunkovo-platizhna-za-gruden-2018.csv", "r", encoding="UTF", newline="") as file:
        reader = csv.DictReader(file,delimiter=';')
        for row in reader:
            print(row["Прізвище, ім'я, по батькові"], "-", row["Оплата по окладу"])