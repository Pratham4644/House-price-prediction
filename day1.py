import pandas as pd

file=r"C:\Users\bs529\OneDrive\Desktop\ML(Kaggle)\data\melb_data.csv"
df =pd.read_csv(file)
print(df.head())
print(df.columns)
print(df.dtypes)
print(df.shape)
df['Car'].fillna(df['Car'].median(), inplace=True)
df['BuildingArea'].fillna(df['BuildingArea'].median(), inplace=True)
df['YearBuilt'].fillna(df['YearBuilt'].median(), inplace=True)
df['CouncilArea'].fillna('Unknown', inplace=True)

print(df.isnull().sum())


