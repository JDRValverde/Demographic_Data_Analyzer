import pandas as pd

df = pd.read_csv("adult.data.csv")
df.head()
df.race.unique()
df.race.value_counts().unique()

#print(round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100))
