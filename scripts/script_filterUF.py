
'''FILTRAR CSV POR CÓDIGO SIAFI'''
import pandas as pd
import os


path = input("Informe o diretório: ")
print(path)
directory = os.fsencode(path)

files = [f for f in os.listdir(path) if f.startswith('2013') and f.endswith('03.csv')] 

for filename in files:

    #filename = os.fsdecode(file)
    file = filename
    print("ARQUIVO:", filename, "\n")  
  

    filename = f'{path}/{filename}'
    df = pd.read_csv(filename)
    
    df2 = pd.read_csv(filename)
    

    print('DF\n')
    df.query('UF == "DF"').to_csv(f'/home/marcos/Desktop/dados_teste/clean_data/{file}', index=False)
    #df2.query('UF == "GO"').to_csv('/home/marcos/Desktop/dados_teste/201301_ok.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    print('RIDE\n')
    df2.query('CODIGO_MUNICIPIO_SIAFI in ["9645","9645","9771","1052","9205","9211","9215","9263","9279","5407","0578","4185","4089","1068","0067","1066","9305","9755","9597","9677","9595","9509","1058","9931","9445","9361","9371","9445","0077","0055","9317","9359","9325","9543","9489" ]').to_csv(f"/home/marcos/Desktop/dados_teste/clean_data/{file}", mode='a', index=False) #mode 'a' não exclui os dados existentes





