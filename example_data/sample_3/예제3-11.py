from sklearn import datasets
import pandas as pd
diabetes = datasets.load_diabetes()
df_diabetes = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(df_diabetes.head())
print(df_diabetes.age.describe())
