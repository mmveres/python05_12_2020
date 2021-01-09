import pandas as pd
if __name__ == '__main__':

    data = pd.read_csv('https://gist.githubusercontent.com/iosiuk/68a86c01922c10f66d35c7feaa66d997/raw/d5aea0c1b1ead288aa85235742149ac0743c7a22/orders.csv')
    print(data.head())

    kmda = pd.read_excel('https://data.gov.ua/dataset/770cc750-4333-424f-b6e9-6e6c5c76aec9/resource/78e76074-4bc5-4e3a-9c20-b4685f458ecc/download/rozrakhunkovo-platizhna-12-20.xls',sheet_name='Sheet1' )
    pd.set_option('display.max_columns', None)
    print(kmda.sample(3))
    print(kmda.columns)