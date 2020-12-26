def get_list_kmda_from_file(filename):
    arr_kmda_oklad = []
    with open(filename, "r", encoding="UTF") as myfile:
        title = myfile.readline()
        for line in myfile:
            cells = line.split(";")
            if cells[0] != '':
                row = [cells[1], float(cells[2].replace(',', '.'))]
                arr_kmda_oklad.append(row)
    return arr_kmda_oklad

if __name__ == '__main__':
    filename = "rozrakhunkovo-platizhna-za-gruden-2018.csv"
    arr_kmda_oklad = get_list_kmda_from_file(filename)
    pour_kmda = arr_kmda_oklad[0]
    for worker in arr_kmda_oklad:
        if worker[1] < pour_kmda[1]:
            pour_kmda = worker
    print(worker)