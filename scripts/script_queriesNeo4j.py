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

	gh = Graph("bolt://localhost:7687")

	#Função para percorrer BD
	#def loadDatabase(self):
		#tx = self.gh.begin()
		#a = Node("Person", name="Ana")


		#tx.create(a)
		#tx.commit()
	gh.run("MATCH (n:Person) DELETE n")
	#print(gh.run("MATCH (a:Beneficiario) RETURN a.nome LIMIT 4").stats())
	#print(len(gh.nodes))


bf = BolsaFamilia()
#bf.loadDatabase()
