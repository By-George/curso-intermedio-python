#manejo de archivos csv


with open('console_games.csv','r') as csv_file:
    #print(csv_file.readlines())
    #print(len(csv_file.readlines()))

    for line in csv_file.readlines():
        print(line)