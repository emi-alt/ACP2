import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IMDB Dataset.csv")
print("HEAD - 3")
print(df.head(3))
print("TAIL - 3")
print(df.tail(3))
print("INFO")
print(df.info())
print("NULL VALUES")
print(df.isnull().sum())
print("ILLOC - 41 to 75")
print(df.iloc[41:76])
print('HIGHEST VOTES')
print(df.loc[df['No_of_Votes'] == df['No_of_Votes'].max()])
sns.boxplot(data=df, x='IMDB_Rating', y='Runtime')
plt.show()

plt.scatter(df['IMDB_Rating'], df['Runtime'])
plt.xlabel('IMDB_Rating')
plt.ylabel('Runtime')
plt.show()

sns.countplot(data=df, x='Certificate', order=df['Certificate'].value_counts().index)
plt.title('Distribution of Certificates')
plt.ylabel('Number of Movies')
plt.show()