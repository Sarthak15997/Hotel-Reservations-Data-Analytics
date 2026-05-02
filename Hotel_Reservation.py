#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[54]:


df = pd.read_csv('hotel_bookings 2.csv')


# # Exploratory Data Analysis And Data Cleaning

# In[55]:


df.head()


# In[56]:


df.tail()


# In[57]:


df.shape


# In[58]:


df.columns


# In[59]:


df.info()


# reservation_status_date column is in object form. We need to perform analysis on this column. So we can change it to Datetime column

# In[60]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[61]:


df.info()


# In[62]:


df.describe(include = 'object')


# In[63]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[64]:


df.isnull().sum()


# Dropping Country and company columns As the number of null rows in these columns is very high as compared to the other columns

# In[65]:


df.drop(['agent', 'company'], axis = 1, inplace = True)


# In[66]:


df.dropna(inplace = True)


# In[67]:


df.isnull().sum()


# In[68]:


df.describe()


# In[69]:


df['adr'].plot(kind = 'box')


# In[70]:


df = df[df['adr'] < 5000]


# In[71]:


df.describe()


# # Data Analysis and Visualizations

# In[72]:


canceled_perc = df['is_canceled'].value_counts(normalize = True)
canceled_perc


# In[73]:


print(canceled_perc)


# In[94]:


plt.figure(figsize = (5, 4))
plt.title('Reservation Status Count')
plt.bar(['Not canceled', 'Canceled'], df['is_canceled'].value_counts(), edgecolor = 'r', width = 0.9)
plt.show()


# As canceled data is more than half of the non canceled data so we can safely say that this is a valid problem that needs to be solved

# In[75]:


plt.figure(figsize = (8, 4))
axl = sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_ = axl. get_legend_handles_labels()
axl.legend(bbox_to_anchor=(1, 1))
plt.title('Reservation status in different hotels', size = 20)
plt.xlabel('hotel')
plt.ylabel('No of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# In[76]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[77]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[78]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[79]:


resort_hotel.head(10)


# In[80]:


city_hotel.tail()


# In[98]:


plt.figure(figsize = (20, 8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.xlabel('month', fontsize = 20)
plt.ylabel('Average Daily Rate', fontsize = 20)
plt.legend(fontsize = 20)
plt.show()


# In[99]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16, 8))
axl = sns.countplot(x = 'month', hue = 'is_canceled', data = df, palette = 'bright')
legend_labels,_ = axl. get_legend_handles_labels()
axl.legend(bbox_to_anchor=(1, 1))
plt.title('Reservation status per month', size = 20)
plt.xlabel('month')
plt.ylabel('reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


# From the above chart we can see that the reservations are the highest in the month of August and the cancelations are also minimum in this month. The cancelations are maximum in the month of January.

# In[83]:


plt.figure(figsize = (15, 8))
plt.title('ADR per month', size = 16)
sns.barplot('month', 'adr', data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# August has the lowest ADR so that might be a reason that the cancelations are minimum in August

# In[100]:


canceled_data = df[df['is_canceled'] == 1]
top_10_country = canceled_data['country'].value_counts()[:10]
plt.figure(figsize = (8, 8))
plt.title("Top 10 countries with reservation canceled")
plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)
plt.show()


# In[85]:


market_segment = df['market_segment']
print(market_segment)


# In[86]:


market_segment.head(20)


# In[87]:


df['market_segment'].value_counts()


# In[88]:


df['market_segment'].value_counts(normalize = True)


# Our Initial Hypothesis that the maximum amount of reservation comes from Offline mode is wrong.

# In[89]:


canceled_data['market_segment'].value_counts(normalize = True)


# In[90]:


canceled_df_adr = canceled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_df_adr.reset_index(inplace = True)
canceled_df_adr.sort_values('reservation_status_date', inplace = True)

not_canceled_data = df[df['is_canceled'] == 0]
not_canceled_df_adr = not_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace = True)
not_canceled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize = (20, 6))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr['reservation_status_date'], not_canceled_df_adr['adr'], label = 'not canceled')
plt.plot(canceled_df_adr['reservation_status_date'], canceled_df_adr['adr'], label = 'canceled')
plt.legend()


# Data from 2016 to September 2017 is consistent. Rest is not consistent. So we only consider the data in the consistent period
# 

# In[91]:


canceled_df_adr = canceled_df_adr[(canceled_df_adr['reservation_status_date']> '2016') & (canceled_df_adr['reservation_status_date'] < '2017-09')]
not_canceled_df_adr = not_canceled_df_adr[(not_canceled_df_adr['reservation_status_date']> '2016') & (not_canceled_df_adr['reservation_status_date'] < '2017-09')]


# In[92]:


not_canceled_df_adr.head()


# In[93]:


plt.figure(figsize = (20, 6))
plt.title('Average Daily Rate', fontsize = 30)
plt.plot(not_canceled_df_adr['reservation_status_date'], not_canceled_df_adr['adr'], label = 'not canceled')
plt.plot(canceled_df_adr['reservation_status_date'], canceled_df_adr['adr'], label = 'canceled')
plt.legend(fontsize = 20)
plt.show()


# In[ ]:




