import sh
import os

novaLinha = '"MES REFERENCIA";"MES COMPETENCIA";"UF";"CODIGO MUNICIPIO SIAFI";"NOME MUNICIPIO";"NIS FAVORECIDO";"NOME FAVORECIDO";"VALOR PARCELA"'
directory = os.fsencode("/home/mendes/Downloads")

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".csv"): 
         sh.sed("-i", "1s/.*/" + novaLinha + "/", filename)