import csv

# 1.uzdevums

# dati = open("weather_data.csv",encoding="utf-8")

# csv_dati = csv.reader(dati)
# rindas = list(csv_dati)

# print(dati.read())

# # 2.uzdevums

# temp = []

# for i in rindas[1:]:
#     temp.append(int(i[1]))

# print (temp)

# # 3.uzdevums

# temperatura1 = []
 
# for e in rindas[1:]:
#     temperatura1.append(e[1])
 
# rezultats = ' '.join(map(str, temperatura1))
# print(rezultats)

import pandas
dati = pandas.read_csv('weather_data.csv')
print(dati["temp"])

dati_vardnica = dati.to_dict()
print(dati_vardnica)

temp_list = dati["temp"].to_list()
print(temp_list)

# aprēķināt vidējo temperatūru

videjais = sum(temp_list)/len(temp_list)
print(videjais)

# vidējais ar Pandas
print(dati["temp"].mean())

# aprēķināt minimālo(min)
print(dati["temp"].min())
# aprēķināt maksimālo(max)
print(dati["temp"].max())