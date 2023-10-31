#!/usr/bin/env python
# coding: utf-8

# # **Importing Libraries**

# In[64]:


import pandas as pd 
import matplotlib.pyplot as plt 
import warnings 
warnings.filterwarnings('ignore') 
import seaborn as sns


# # **Loading the Dataset**

# In[30]:


df=pd.read_csv(r"C:\Users\DELL\Desktop\CloudyML\Data Analyst Project-Python\Hotel_booking.csv")


# # Exploratory Data Analysis and Data Cleaning 

# In[31]:


df.head()


# In[32]:


df.tail()


# In[33]:


df.shape


# In[34]:


df.columns


# In[16]:


df.info()


# In[35]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], format='%d-%m-%Y')


# In[36]:


df.info()


# In[37]:


df.describe(include='object')


# In[41]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique()) 
    print('-'*50)


# In[42]:


df.isnull().sum()


# In[43]:


df.drop(['company','agent'],axis=1,inplace=True)
df.dropna(inplace=True)


# In[45]:


df.isnull().sum()


# In[46]:


df.describe()


# In[47]:


df['adr'].plot(kind='box')


# In[48]:


df=df[df['adr']<5000]


# In[49]:


df.describe()


# # **Data Analysis and visualizations**

# In[58]:


cancelled_perc =df['is_canceled'].value_counts()
cancelled_perc 


# In[54]:


plt.figure(figsize=(5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.7) 
plt.show()


# In[60]:


# percentage wise 
cancelled_perc =df['is_canceled'].value_counts(normalize=True)*100
cancelled_perc 


# In[62]:


plt.figure(figsize=(5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(normalize=True)*100,edgecolor='k',width=0.7) 
plt.show()


# In[67]:


plt.figure(figsize=(8,4))
ax1=sns.countplot(x='hotel',hue='is_canceled',data=df,palette='Blues')
legend_labels,_=ax1.get_legend_handles_labels()
plt.title('Reservation status in different hotels',size=20)
plt.xlabel('hotel')
plt.ylabel('number of reservations') 
plt.show()


# In[70]:


resort_hotel= df[df['hotel']=='Resort Hotel'] 
resort_hotel['is_canceled'].value_counts(normalize=True)*100


# In[73]:


city_hotel= df[df['hotel']=='City Hotel'] 
city_hotel['is_canceled'].value_counts(normalize=True)*100


# In[74]:


resort_hotel= resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel= city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[76]:


plt.figure(figsize=(20,8))
plt.title('Average Daily Rate in city and Resort hotel',fontsize=30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label='Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label='City Hotel') 
plt.legend(fontsize=20)
plt.show()


# In[81]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
ax1=sns.countplot(x='month',hue='is_canceled',data=df,palette='bright')
legend_labels,_=ax1.get_legend_handles_labels() 
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservtion status per month',size=20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['Not canceled','Canceled'])
plt.show()


# In[86]:


plt.figure(figsize=(15,8))
plt.title('AdR per month',fontsize=30)
data = df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index()
sns.barplot(x='month',y='adr',data=data)
plt.show()


# In[87]:


cancelled_data=df[df['is_canceled']==1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country,autopct='%.2f',labels= top_10_country.index)
plt.show()


# In[88]:


df['market_segment'].value_counts()


# In[90]:


df['market_segment'].value_counts(normalize=True)*100


# In[91]:


cancelled_df_adr= cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values('reservation_status_date',inplace=True)

not_cancelled_data=df[df['is_canceled']==0]
not_cancelled_df_adr=not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace=True)
not_cancelled_df_adr.sort_values('reservation_status_date',inplace=True)

plt.figure(figsize=(20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label='not_cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label='cancelled')
plt.legend()


# In[92]:


cancelled_df_adr= cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016')&(cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr= not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016')&(not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[94]:


plt.figure(figsize=(20,6))
plt.title('Average Daily Rate',fontsize=30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label='not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label='cancelled')
plt.legend(fontsize=20)


# In[ ]:




