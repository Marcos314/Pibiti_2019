
import os
import sh
import csv

#SCRIPT PARAR REMOVER ASPAS DUPLAS

directory = os.fsencode("/home/marcos/Desktop/TCC_2020/dados/")

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
        sh.sed("-i", "s/,00//g", path)      #Remover casas decimais com zeros no final
        sh.sed("-i", "s/;/,/g", path)       #Remover ;
        
        #sh.sed("-i", "1s/.*/" + "var" + "/", filename)