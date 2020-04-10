import pandas as pd
import csv

'''Constantes'''
limInsercao = 10**4
ten = 10
count = 10**2


with open('/home/marcos/Desktop/dados_teste/testeW2.csv', "w") as file_w:
#with open('/home/marcos/neo4j/neo4j-pibiti/teste_escrita_1.csv', "w") as file_w:
    with open('/home/marcos/Desktop/TCC_2020/dados/201501.csv', "r") as file:
        
        reader = csv.reader(file, delimiter=';')
        head = next(reader)
        reader = csv.reader(file)


        writer = csv.writer(file_w)
        writer.writerow(head)
        data = []   
        bigCount = 0
        
        aux = 1
        print('INICIO DA IMPORTAÇÃO\n')
        for row  in reader:
            data = row

            if(bigCount < limInsercao):
                writer = csv.writer(file_w)
                writer.writerow(data)
                bigCount+=1
                if((bigCount//count) > ten * aux):
                    aux+=1
                    print(f"INSERIDO {bigCount} REGISTROS")        
       
            else:
                print(f"INSERIDO NO TOTAL: {bigCount} REGISTROS")
                
                break


        







