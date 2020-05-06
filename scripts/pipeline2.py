import pandas as pd
from py2neo import *
import sys
import os
import time
import os
import sh
import csv
import time
import gc
#SCRIPT PARAR REMOVER ASPAS DUPLAS, ,00


def replaceLine():

    start_time = time.time()
    now = datetime.now()
    print('\nFUNÇÃO: replaceLine\n')
    
    

    path = input("Informe o diretório: ")
    print(path)
    directory = os.fsencode(path)
    

    for file in os.listdir(directory):        
        filename = os.fsdecode(file)

        print(f"----- ARQUIVO: {filename} -----\n ")
        if filename.endswith(".csv"):

            directory = str(directory)
            
            path = str(directory[2:-1] + filename)
            
            print(path)

            reader = csv.reader(filename, delimiter=';')
            head = next(reader)
            reader = csv.reader(filename)
            path2 = '/home/marcos/Desktop/dados_teste/clean_data/'
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
    
    print("----- FUNÇÃO filterUf -----\n ")

    start_time = time.time()
    now = datetime.now()

    #path = input("Informe o diretório: ")
    path = '/media/marcos/DISPOSITIVO/pibiti/dados'
    print(path)
    directory = os.fsencode(path)

    files = [f for f in os.listdir(path) if f.startswith('2013') and f.endswith('08.csv')] 
    
    for filename in files:

        #filename = os.fsdecode(file)
        file = filename
        print("ARQUIVO:", filename, "\n")     

        #filename = '/home/marcos/Desktop/dados_teste/to_replaceLine/201706.csv' /media/marcos/DISPOSITIVO/pibiti/dados

        filename = f'{path}/{filename}'

        
        df = pd.read_csv(filename,low_memory=True)

        #df2 = pd.read_csv(filename)
        #print('DF\n')
        #df.query('UF == "DF"').to_csv(f'/home/marcos/Desktop/dados_teste/clean_data/{file}', index=False)
        #df2.query('UF == "GO"').to_csv('/home/marcos/Desktop/dados_teste/201301_ok.csv', mode='a', index=False) #mode 'a' não exclui os dados existentes
        print('RIDE\n')
        df.query('CODIGO_MUNICIPIO_SIAFI in ["9645","9645","9771","1052","9205","9211","9215","9263","9279","5407","0578","4185","4089","1068","0067","1066","9305","9755","9597","9677","9595","9509","1058","9931","9445","9361","9371","9445","0077","0055","9317","9359","9325","9543","9489","9701"]').to_csv(f"/home/marcos/Desktop/dados/clean_data/{file}", mode='a', index=False) #mode 'a' não exclui os dados existentes

    spend = time.time() - start_time
    hour = spend//3600
    spend %= 3600
    minutes = spend//60
    spend %= 60
    second = spend

    print(f"Tempo gasto filterUF() -> Time: {int(hour)}h, {int(minutes)}min, {round(second,2)}s")
    with open('/home/marcos/Desktop/dados/log.txt', "a+") as file_w:
        writer1 = file_w.write(f"Arquivo: {file}\n")
        writer = file_w.write(f"Tempo Total -> Time: {int(hour)}h, {int(minutes)}min, {round(second,2)}s\n")
    
    


#replaceLine()
filterUf()
# '''INÍCIO DA FUNÇÃO PRINCIPAL'''
# def main():

#     #replaceLine()
#     #filterUf()

#     #IMPORTAÇÃO PARA O NEO4J   
#     class BolsaFamilia:
#         GRAPH = Graph("bolt://localhost:7687")

#         def cleanDatabase(self):
#             self.GRAPH.run("MATCH (n) DETACH DELETE n;")

#         def loadDatabase(self):
#             print('Inicio LoadDatabase\n')
#             start_time = time.time()
#             files = [f for f in os.listdir("/home/marcos/Desktop/dados_teste/clean_data/") if f.startswith('2014') and f.endswith('01.csv')]
#             #print(files)
#             for filename in files:
                               
#                 files = str(files)
#                 filename = f'/home/marcos/Desktop/dados_teste/clean_data/{filename}'
               
#                 #for dataframe in pd.read_csv( filename, sep=','):                
#                 dataframe = pd.read_csv(filename) #MUDAR ESSA LEITURA P/OTMIZAÇÃO DA MEMÓRIA
                
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
                
#                 print(filename)
#                 print(dataframe.info())

#             '''TIME'''
#             spend = time.time() - start_time
#             hour = spend//3600
#             spend %= 3600
#             minutes = spend//60
#             spend %= 60
#             second = spend

#             print(f"\nTempo gasto filterUF() -> Time: {int(hour)}h, {int(minutes)}min, {round(second,2)}s")  
        
#     #print('inicio')
#     bf = BolsaFamilia()
#     #bf.cleanDatabase()
#     bf.loadDatabase()
# '''FIM DA MAIN'''

# if __name__ == '__main__':
#    main()

