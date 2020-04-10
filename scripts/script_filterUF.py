
'''FUNÇÃO PARA FILTRAR CSV POR UF'''

import pandas as pd


filename = '/home/marcos/Desktop/dados_teste/201501.csv'

df = pd.read_csv(filename, sep=',')
df2 = pd.read_csv(filename, sep=',')



df.query('UF == "DF"').to_csv('/home/marcos/Desktop/dados_teste/testeW3.csv', index=False)
df2.query('UF == "GO"').to_csv('/home/marcos/Desktop/dados_teste/testeW3.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes

print(df.query('UF == "DF"'))


    
   
       
    

    
