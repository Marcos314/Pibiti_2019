# sudo apt-get install python3-pip
# sudo python3 -m pip install pip --upgrade
# sudo pip install pandas
# sudo python3 -m pip install py2neo
# wget https://www.dropbox.com/s/z53qgw23lw042ij/BF201808.csv
import pandas as pd
from py2neo import *
import sys
import os

class BolsaFamilia:
    GRAPH = Graph("bolt://localhost:7687")

    def cleanDatabase(self):
        self.GRAPH.run("MATCH (n) DETACH DELETE n;")

    def loadDatabase(self):
        files = [f for f in os.listdir("/home/marcos/Desktop/dados_teste/") if f.startswith('te') and f.endswith('3.csv')]
        #print(files)
        for filename in files:
            #filename = 'dados/' + filename
            print(filename)
            #for dataframe in pd.read_csv( filename, sep=','):
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
                    tx.commit()
print('inicio')
bf = BolsaFamilia()
bf.cleanDatabase()
bf.loadDatabase()
