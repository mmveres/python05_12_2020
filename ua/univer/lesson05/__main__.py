if __name__ == '__main__':
    with open("user.csv", "r", encoding="UTF") as myfile:
        user_str = myfile.readline()
        user1 = tuple(user_str.split(";"))
   # user1 = ["Tom", 20, 10000]
    print("name=", user1[0],"age=",user1[1],"salary=",user1[2])
    user1[1] = "privet"
    print("name=", user1[0],"age=",user1[1],"salary=",user1[2])