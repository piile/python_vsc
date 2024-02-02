import pandas

dati = {
    "auto":["BMW", "Audi", "Mercedes"],
    "sēdvietas":[2,5,8]
}
rezult = pandas.DataFrame(dati)
print(rezult)

import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

import pandas as pd
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# load data into a DataFrame object:
df = pd.DataFrame(data, index = ["day1", "day2", "'day3"])
print(df)

import pandas as pd
df = pd.read_csv('Klases.csv')
print(df.head(10))