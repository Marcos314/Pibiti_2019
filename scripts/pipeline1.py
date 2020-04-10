import pandas as pd
from py2neo import *
import sys
import os
import time
import os
import sh
import csv
import time 
#SCRIPT PARAR REMOVER ASPAS DUPLAS, ,00


def replaceLine():

    start_time = time.time()
    now = datetime.now()
    print('FUNÇÃO replaceLine()\n')
    print("----- ARQUIVO: 201301.CSV e 201706.csv -----\n ")
    directory = os.fsencode("/home/marcos/Desktop/dados_teste/to_replaceLine/")
    

    for file in os.listdir(directory):        
        filename = os.fsdecode(file)

        if filename.endswith(".csv"):

            directory = str(directory)
            
            path = str(directory[2:-1] + filename)
            
            print(path)

            reader = csv.reader(filename, delimiter=';')
            head = next(reader)
            reader = csv.reader(filename)
            
            sh.sed("-i", "s/\"//g", path)        #Remover aspas duplas
            sh.sed("-i", "1s/ /_/g" , path)      #Alterar primeira linha do arquivo
            sh.sed("-i", "s/,00//g", path)      #Remover casas decimais com zeros no final
            sh.sed("-i", "s/;/,/g", path)       #Trocar ; por ,

    spend = time.time() - start_time
    hour = spend//3600
    spend %= 3600
    minutes = spend//60
    spend %= 60
    second = spend

    print(f"Tempo gasto replaceLine() -> Time: {int(minutes)}min, {round(second,2)}s")

#FUNÇÃO PARA OBTER REGISTROS APENAS DE DOIS ESTADOS (GO E DF)
def filterUf():

    print('FUNÇÃO filterUF()\n')
    print("----- ARQUIVO: 201301.CSV -----\n ")

    start_time = time.time()
    now = datetime.now()

    filename = '/home/marcos/Desktop/dados_teste/to_replaceLine/201706.csv'

    df = pd.read_csv(filename, sep=',')
    df2 = pd.read_csv(filename, sep=',')


    df.query('UF == "DF"').to_csv('/home/marcos/Desktop/dados_teste/201301_ok.csv', index=False)
    #df2.query('UF == "GO"').to_csv('/home/marcos/Desktop/dados_teste/201301_ok.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9645"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9771"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "1052"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9205"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9211"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9215"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9263"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9279"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "5407"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "0578"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "4185"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "4089"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "1068"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "0067"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "1066"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9305"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9755"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9597"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9677"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9595"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9509"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "1058"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9931"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9445"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9361"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9371"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9445"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "0077"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "0055"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9317"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9359"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9325"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9543"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
    df2.query('CODIGO_MUNICIPIO_SIAFI == "9489"').to_csv('/home/marcos/Desktop/dados_teste/clean_data/201706.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes


    spend = time.time() - start_time
    hour = spend//3600
    spend %= 3600
    minutes = spend//60
    spend %= 60
    second = spend

    print(f"Tempo gasto filterUF() -> Time: {int(minutes)}min, {round(second,2)}s")

'''INÍCIO DA FUNÇÃO PRINCIPAL'''
# def main():

#     replaceLine()
#     filterUf()

#     #IMPORTAÇÃO PARA O NEO4J
#     inicio = time.time()
#     class BolsaFamilia:
#         GRAPH = Graph("bolt://localhost:7687")

#         def cleanDatabase(self):
#             self.GRAPH.run("MATCH (n) DETACH DELETE n;")

#         def loadDatabase(self):
#             files = [f for f in os.listdir("/home/marcos/Desktop/Pibiti_2019/scripts/") if f.startswith('20') and f.endswith('2.csv')]
#             #print(files)
#             for filename in files:
#                 #filename = 'dados/' + filename
#                 print(filename)
#                 #for dataframe in pd.read_csv( filename, sep=','):
#                 dataframe = pd.read_csv(filename)
#                 print(dataframe.info())
#                 for index, linha in dataframe.iterrows():
#                         sys.stdout.write('.')
#                         tx = self.GRAPH.begin()
#                         p = Node("Pagamento", 
#                             mesReferencia=linha['MES_REFERENCIA'],
#                             mesCompetencia=linha['MES_COMPETENCIA'], 
#                             nomeMunicipio=linha['NOME_MUNICIPIO'], 
#                             valorParcela=linha['VALOR_PARCELA'],
#                             codigoMunicipio=linha['CODIGO_MUNICIPIO_SIAFI'],
#                             uf=linha['UF']
#                             )
#                         b = Node("Beneficiario", 
#                             nome=linha['NOME_FAVORECIDO'], 
#                             nis=linha['NIS_FAVORECIDO']
#                         )
#                         tx.create(p)
#                         tx.merge(b, "Beneficiario", "nis")
#                         b_p = Relationship(b, "RECEBEU", p)
#                         tx.create(b_p)
#                         tx.commit() #ver batch do IPEA/RAIS    
        
#     print('inicio')
#     bf = BolsaFamilia()
#     bf.cleanDatabase()
#     bf.loadDatabase()

#     fim = time.time()
#     print(f'Tempo gasto: {fim} - {inicio}')

# '''FIM DA MAIN'''

# if __name__ == '__main__':
#    main()

#replaceLine()
filterUf()