from sklearn import datasets
import pandas as pd
wine = datasets.load_wine()
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
print(df_wine.head())
print(df_wine.alcohol.describe())
