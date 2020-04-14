# sudo apt-get install python3-pip
# sudo python3 -m pip install pip --upgrade
# sudo pip install pandas
# sudo python3 -m pip install py2neo
# wget https://www.dropbox.com/s/z53qgw23lw042ij/BF201808.csv
import pandas as pd
from py2neo import *
import sys
import os
import time
import csv


class BolsaFamilia:
    GRAPH = Graph("bolt://localhost:7687")

    def cleanDatabase(self):
        self.GRAPH.run("MATCH (n) DETACH DELETE n;")


    def loadDatabase(self):
        start_time = time.time()
        now = datetime.now()

        #directory = '/home/marcos/Desktop/Pibiti_2019/scripts/'
        files = [f for f in os.listdir('/home/marcos/Desktop/Pibiti_2019/scripts/') if f.startswith('20') and f.endswith('.csv')]
        #print(files)
        for filename in files:
            #filename = 'clean_data/' + filename
            print('ARQUIVO:',filename)
            for dataframe in pd.read_csv( filename,chunksize=10 ** 6):
                print('OK')
                dataframe = pd.read_csv(filename)
                print(dataframe.info())
                for index, linha in dataframe.iterrows():
                    sys.stdout.write('.')
                    tx = self.GRAPH.begin()
                    p = Node("Pagamento", 
                        mesReferencia=linha['MES_REFERENCIA'],
                        mesCompetencia=linha['MES_COMPETENCIA'], 
                        nomeMunicipio=linha['NOME_MUNICIPIO'], 
                        valorParcela=linha['VALOR_PARCELA'],
                        codigoMunicipio=linha['CODIGO_MUNICIPIO_SIAFI'],
                        uf=linha['UF']
                        )
                    b = Node("Beneficiario", 
                        nome=linha['NOME_FAVORECIDO'], 
                        nis=linha['NIS_FAVORECIDO']
                    )
                    tx.create(p)
                    tx.merge(b, "Beneficiario", "nis")
                    b_p = Relationship(b, "RECEBEU", p)
                    tx.create(b_p)
                    tx.commit() #ver batch do IPEA/RAIS
        
        spend = time.time() - start_time
        hour = spend//3600
        spend %= 3600
        minutes = spend//60
        spend %= 60
        second = spend
        print(f"Tempo gasto para importação -> Time: {int(minutes)}min, {round(second,2)}s")


    
print('inicio')
bf = BolsaFamilia()
bf.cleanDatabase()
bf.loadDatabase()

