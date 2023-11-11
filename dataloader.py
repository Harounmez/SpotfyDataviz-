import pandas as pd 

df = pd.read_csv('dataset.csv')
df = df.drop('Unnamed: 0', axis = 1)
df = df.drop('track_id', axis = 1)


df = df.drop('artists', axis=1)
df = df.drop('album_name', axis=1)
df = df.drop('track_name', axis=1)

print(df.columns)