
import os
import sh

#SCRIPT PARAR REMOVER ASPAS DUPLAS

directory = os.fsencode("/home/marcos/Desktop/dados_teste/to_replaceLine/")

for file in os.listdir(directory):
       
     filename = os.fsdecode(file)
     if filename.endswith(".csv"):
        directory = str(directory)
        
        path = str(directory[2:-1] + filename)
        
        print(path)
        
        sh.sed("-i", "s/\"//g", path)
        #sh.sed("-i", "s/0,/0./g", path)
    
        
        #sh.sed("-i", "1s/.*/" + "var" + "/", filename)