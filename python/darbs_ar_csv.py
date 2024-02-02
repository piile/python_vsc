import csv
# atver failu
dati = open("example.csv",encoding="utf-8")

# nolasa failu
csv_dati = csv.reader(dati)

# pārformatē par Python objektu - list of lists
rindas = list(csv_dati)

# izdrukā datus
print(rindas[0])
print(len(rindas))

# izdrukā vairākas konkrētas rindas
for i in rindas[:5]:
    print(i)

# e-pasts no konkrētas rindas
print(rindas[9][3])

# visus e-pastus
epasti = []

for i in rindas[1:16]:
    epasti.append(i[3])

print(epasti)

# izdrukā vārdus un uzvārdus
personas = []

for i in rindas[1:16]:
    personas.append(i[1]+" "+i[2])

print(personas)

# ieraksta failā
jauns_fails = open("jauns_fails.csv",mode="w",newline="")
ierakstitajs = csv.writer(jauns_fails,delimiter=',')
ierakstitajs.writenow(["a","b","c"])
ierakstitajs.writerows(["1","2","3"],["1","2","3"])
jauns_fails.close()