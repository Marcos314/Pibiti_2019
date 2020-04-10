import sh
import os
import csv
novaLinha = '"MES_REFERENCIA";"MES_COMPETENCIA";"UF";"CODIGO_MUNICIPIO_SIAFI";"NOME_MUNICIPIO";"NIS_FAVORECIDO";"NOME_FAVORECIDO";"VALOR_PARCELA"'

directory = os.fsencode("/home/marcos/Desktop/dados_teste/to_replaceLine/")

for file in os.listdir(directory):
     filename = os.fsdecode(file)



     if filename.endswith(".csv"): 

        directory = str(directory)
        path = str(directory[2:-1] + filename)
        #sh.sed("-i", "s/\"//g", path)
        sh.sed("-i", "1s/ /_/g" , path)