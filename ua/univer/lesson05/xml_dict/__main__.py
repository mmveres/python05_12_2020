import xmltodict
import pprint
import json

with open('data.xml') as fd:
    doc = xmltodict.parse(fd.read())
    data_txt = json.dumps(doc)
    with open("data.json", "w") as file:
        file.write(data_txt)

   # data_dict = json.loads(data_txt)
    with open("data.json", "r", encoding="UTF") as myfile:
        data_str = myfile.read()
    data_dict = json.loads(data_str)
    for elem in data_dict['data']['items']['item']:
        print(elem['#text'])