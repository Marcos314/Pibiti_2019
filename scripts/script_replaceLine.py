
import os
import sh
import csv

#SCRIPT PARAR REMOVER ASPAS DUPLAS

novaLinha = '"MES_REFERENCIA";"MES_COMPETENCIA";"UF";"CODIGO_MUNICIPIO_SIAFI";"NOME_MUNICIPIO";"NIS_FAVORECIDO";"NOME_FAVORECIDO";"VALOR_PARCELA"'
directory = os.fsencode("/home/marcos/Desktop/dados/clean_data/")

for file in os.listdir(directory):
       
     filename = os.fsdecode(file)
     if filename.endswith("201308.csv"):
        directory = str(directory)
        
        path = str(directory[2:-1] + filename)
        
        print(path)
        sh.sed("-i", "1s/.*/" + novaLinha + "/", filename)
        reader = csv.reader(filename, delimiter=';')
        #head = next(reader)
        #reader = csv.reader(filename)
        
        sh.sed("-i", "s/\"//g", path)        #Remover aspas duplas
        sh.sed("-i", "1s/ /_/g" , path)      #Alterar primeira linha do arquivo
        sh.sed("-i", "s/,00//g", path)      #Remover casas decimais com zeros no final
        sh.sed("-i", "s/;/,/g", path)       #Trocar ; por ,

       

        #sh.sed("-i", "s/,00//g", path)      #Remover casas decimais com zeros no final
        #sh.sed("-i", "1s/.*/" + "var" + "/", filename)