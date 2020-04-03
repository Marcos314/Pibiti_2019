import pandas as pd
import csv

#df = pd.read_csv('/home/marcos/Desktop/teste_1.csv')

with open('/home/marcos/Desktop/dados_teste/teste_1.csv', "r") as file:

    reader = csv.reader(file, delimiter = ";")

    head = next(reader)

    print(head)

    for row in reader:

        print(row)


with open('/home/marcos/Desktop/dados_teste/teste_escrita_1.csv', "w") as file_w:

    writer = csv.writer(file_w)
    writer.writerow(head)






