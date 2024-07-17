import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/home/clein/Desktop/Projects/Data Analytics Practice/real_estate/properties.csv')

cities=['Manhattan','Brooklyn','Queens','Long Island','Bronx']
data1=data[data['city'].isin(cities)].groupby('city')['price'].mean()

plt.figure(figsize=(10,6))
plt.scatter(data1.index,data1.values)
plt.xlabel('City')
plt.ylabel('Average Price')
plt.title('Average Property Price By City In NYC')
plt.tight_layout()
plt.show()
