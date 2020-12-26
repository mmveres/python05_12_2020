def save_to_file_in_new_row(arr, filename = "mytext.txt"):
    with open(filename, "w") as file_write:
        for x in arr:
            file_write.write(str(x) + "\n")


def get_list_from_file_in_new_row(filename = "mytext.txt"):
    arr1 = []
    with open(filename, "r") as myfile:
        for line in myfile:
            arr1.append(int(line))
    return arr1

def save_to_file_in_one_row(arr, filename = "mytext.txt"):
    with open(filename, "w") as file_write:
        for x in arr:
            file_write.write(str(x) + " ")

def get_list_from_file_in_one_row(filename = "mytext.txt"):
    arr1 = []
    with open(filename, "r") as myfile:
        for line in myfile:
            arr = line.rstrip().split(" ")
            arr1.append([int(x) for x in arr])
    return arr1


def save_to_file_in_one_row_CSV(arr, filename = "mytext.csv"):
    with open(filename, "w") as file_write:
        for x in arr:
            file_write.write(str(x) + ";")

def get_list_from_file_in_one_row_CSV(filename = "mytext.csv"):
    arr1 = []
    with open(filename, "r") as myfile:
        for line in myfile:
            arr = line.rstrip().split(";")
            arr1.append([int(x) for x in arr])
    return arr1

if __name__ == '__main__':
    arr = [1,2,3,4,5]
   # save_to_file_in_one_row_CSV(arr,"1.csv")
    arr1 = get_list_from_file_in_one_row_CSV("1.csv")
    print(arr1)