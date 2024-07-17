import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('/home/clein/Desktop/Projects/Data Analytics Practice/real_estate/properties.csv')

manhattanData=data[(data['city']=='Manhattan')&(data['price']>=90000)&(data['price']<=120000)]

prices=manhattanData['price'].value_counts()
plt.figure(figsize=(8,6))
plt.bar(prices.index,prices.values, color='skyblue')
plt.xlabel('Price Range')
plt.ylabel('Number Of Properties')
plt.title('Distribution Of Property Prices In Manhattan')
plt.xticks(rotation=50)
plt.tight_layout()
plt.show()
