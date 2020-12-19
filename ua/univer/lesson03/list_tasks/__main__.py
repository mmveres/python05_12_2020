from ua.univer.lesson03.list_tasks.list_tasks import *

if __name__ == '__main__':
    arr1 = [1,-2,3,4]
    companies = ["Microsoft", "Google", "Oracle", "Apple"]

    print1(companies)

    print2(companies)

    print3(companies)

    sum = 0
    count = 0
    for x in arr1:
        if x > 2:
            sum+=x
            count+=1
    aver = sum/count
