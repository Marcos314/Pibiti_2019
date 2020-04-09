import csv
import pandas as pd

with open('/home/marcos/Desktop/dados_teste/testeW2.csv', "w") as file_w:

    with open('/home/marcos/Desktop/TCC_2020/dados/201501.csv', "r") as file:
        
        reader = csv.reader(file)
        head = next(reader)

        reader = csv.reader(file)

        writer = csv.writer(file_w)
        writer.writerow(head)  

        df = pd.read_csv('/home/marcos/Desktop/TCC_2020/dados/201501.csv', low_memory=False)       

        bigCount = 0
        limInsercao = 10**3
        ten = 10
        count = 10
        lista = []
        for row  in reader:

            if df.columns[2] == 'UF':
                lista = row                
                writer = csv.writer(file_w)
                writer.writerow(lista)

        print(lista)