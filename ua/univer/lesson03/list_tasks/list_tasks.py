def print1(companies):
    for company in companies:
        print(company)


def print2(companies):
    for i in range(len(companies)):
        print(companies[i])


def print3(companies):
    i = 0
    while i < len(companies):
        print(companies[i])
        i += 1

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    print3(arr)