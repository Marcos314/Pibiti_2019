import pandas as pd
import csv

#df = pd.read_csv('/home/marcos/Desktop/teste_1.csv')

with open('/home/marcos/Desktop/dados_teste/teste_escrita_1.csv', "r+") as file_w:
    
    with open('/home/marcos/Desktop/dados_teste/teste_1.csv', "r") as file:
        
        reader = csv.reader(file)
        head = next(reader)  
        data = []
        writer = csv.writer(file_w)
        writer.writerow(head)
        for row in reader:
            data = row
            print(row)
        
            writer = csv.writer(file_w)
            writer.writerow(data)

        







