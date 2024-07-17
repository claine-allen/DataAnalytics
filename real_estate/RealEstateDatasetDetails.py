import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/home/clein/Desktop/Projects/Data Analytics Practice/real_estate/properties.csv')

print(data.head())

print(data.info())

print(data.describe())

