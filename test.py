import pandas as pd

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_weather = pd.read_csv(link)

continent_list = [' US.', ' Japan.', ' Europe.']

toto= df_weather.columns.values

print((toto[0]))