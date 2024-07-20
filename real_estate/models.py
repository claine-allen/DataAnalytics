import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/home/clein/Desktop/Projects/Data Analytics Practice/real_estate/properties.csv')

plt.figure(figsize=(8,6))
plt.hist(data['price'],bins=20, edgecolor='black')
plt.xlabel('Price')
plt.ylabel('Number of Properties')
plt.title('Distribution of Property Prices')
plt.grid(True)
plt.show()

property_types=data['property_type'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(property_types,labels=property_types.index,autopct='%1.1f%%')
plt.title('Proportion Of Properties By Type')
plt.show()

avg_price_city=data.groupby('city')['price'].mean()
plt.figure(figsize=(10,6))
plt.bar(avg_price_city.index, avg_price_city.values)
plt.xlabel('City')
plt.ylabel('Average Price')
plt.title('Average price per city')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

avg_listing_age_year=data.groupby('year_build')['listing_age'].mean()
plt.figure(figsize=(8,6))
plt.plot(avg_listing_age_year.index,avg_listing_age_year.values)
plt.xlabel('Year Built')
plt.ylabel('Average listing age')
plt.title('Average listing age by year built')
plt.grid(True)
plt.show()
