import pandas as pd
import csv

#df = pd.read_csv('/home/marcos/Desktop/teste_1.csv')

with open('/home/marcos/Desktop/dados_teste/teste_escrita_1.csv', "w") as file_w:
    
    with open('/home/marcos/Desktop/TCC_2020/dados/201501.csv', "r") as file:
        
        reader = csv.reader(file)
        head = next(reader)
        reader = csv.reader(file, delimiter= ";")
        writer = csv.writer(file_w)
        writer.writerow(head)
        data = []   
        Bcount = 0
        count = 10**4
        aux = 1
        print('INICIO DA IMPORTAÇÃO\n')
        for row in reader:
            data = row
            
            if(Bcount < 10**6):
                writer = csv.writer(file_w)
                writer.writerow(data)
                Bcount+=1

                if((Bcount//count) > 10*aux):
                    aux+=1
                    print(f"INSERIDO {Bcount} REGISTROS")        
       
            else:
                print(f"INSERIDO NO TOTAL: {Bcount} REGISTROS")
                break

        







