import pandas as pd
from py2neo import *
import sys
import os

class BolsaFamilia:
        
    GRAPH = Graph("bolt://localhost:7687")

    def cleanDatabase(self):
        self.GRAPH.run("MATCH (n) DETACH DELETE n;")

    def queries(self):
            
        self.GRAPH.run("MATCH (n:Person) DELETE n")
        print(self.GRAPH.run("MATCH (a:Beneficiario) RETURN a.nome LIMIT 4").stats())

    def carregarDados(self):

        query = "LOAD CSV WITH HEADERS FROM 'file:///teste3.csv' as line CREATE  (p:Pagamento {mesReferencia: line.MES_REFERENCIA, mesCompetencia: line.MES_COMPETENCIA, nomeMunicipio: line.NOME_MUNICIPIO, valorParcela: line.VALOR_PARCELA,codigoMunicipio: line.CODIGO_MUNICIPIO_SIAFI, uf: line.UF})"

        query2 = "LOAD CSV WITH HEADERS FROM 'file:///teste3.csv' as line CREATE (b:Beneficiario {nome: line.NOME_FAVORECIDO, nis: line.NIS_FAVORECIDO})"

        query3 = "LOAD CSV WITH HEADERS FROM 'file:///teste3.csv' as line MERGE (b:Beneficiario {nis: line.NIS_FAVORECIDO})"

        relation = "LOAD CSV WITH HEADERS FROM 'file:///teste3.csv' as line MATCH (b:Beneficiario) MERGE (p:Pagamento {nomeMunicipio: line.NOME_MUNICIPIO,  uf: line.UF}) MERGE (b)-[:RECEBEU]->(p)"    


        self.GRAPH.run(query)
        self.GRAPH.run(query2)
        self.GRAPH.run(query3)
        self.GRAPH.run(relation)


bf = BolsaFamilia()
bf.cleanDatabase()
#bf.queries()
bf.carregarDados()