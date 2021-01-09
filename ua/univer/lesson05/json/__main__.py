import json


def get_dict_from_file(filename):
    with open(filename, "r", encoding="UTF") as myfile:
        user_str = myfile.read()
    print(user_str)
    user_dict = json.loads(user_str)
    return user_dict
if __name__ == '__main__':
    user_dict = get_dict_from_file("user.json")
    print(user_dict["children"])
    dictData = { "ID"       : 210450,
                 "login"    : "admin",
                 "name"     : "John Smith",
                 "password" : "root",
                 "phone"    : 5550505,
                 "email"    : "smith@mail.com",
                 "online"   : True }

    strData = json.dumps(dictData)
    with open("data.json", "w") as file:
        file.write(strData)