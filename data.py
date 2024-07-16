import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('/home/clein/Desktop/Projects/AmazonProductSales/Casual Shoes.csv')
print(data.head())
print(data.info())
print(data.describe())
sns.histplot(data['name'],bins=20)
plt.show()
