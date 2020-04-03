import csv

with open('/home/marcos/Desktop/dados_teste/teste_1.csv', "r") as file:

    reader = csv.reader(file)

    head = next(reader)
    
    
    print(f"First Line {head}")

    print(len(head))




    for row in reader:
        print(row)