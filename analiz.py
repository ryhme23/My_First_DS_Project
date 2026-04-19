from unittest.mock import inplace

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dt = pd.read_csv('Data/imdb_movie_data.csv')

#print(dt.head())
#print(dt.info())
#print(dt.describe())
#print(dt.columns)
#print(dt.shape)

#print(dt['Runtime (Minutes)'].info())

dt_clean = dt.copy()


#print(dt_clean.dtypes)

#print(dt_clean.isnull().sum())


dt_clean['Metascore'] = dt_clean['Metascore'].fillna(dt_clean['Metascore'].mean())

#print(dt_clean.isnull().sum())

#print(dt_clean.info())

dt_clean['Revenue (Millions)'] = dt_clean['Revenue (Millions)'].fillna(dt_clean['Revenue (Millions)'].mean())

#print(dt_clean.isnull().sum())

top10 = dt_clean.sort_values('Rating', ascending=False).head(10)

#print(top10[['Title','Rating']])

sum_director = dt_clean['Director'].value_counts()
#print(sum_director.head(10))

run_time = dt_clean['Runtime (Minutes)'].sort_values(ascending=False)

#print(f"En uzun film: {run_time.head(1)} en kısa film: {run_time.tail(1)}")

plt.figure(figsize = (10,8))

plt.scatter(dt_clean['Year'], dt_clean['Rating'])
plt.xlabel('Rating')
plt.ylabel('Year')
#plt.show()


#print(dt_clean['Genre'].value_counts())

#print(dt_clean.groupby('Genre')['Revenue (Millions)'].value_counts())

plt.plot(dt_clean['Revenue (Millions)'].value_counts())
plt.title('Top 10')
plt.show()