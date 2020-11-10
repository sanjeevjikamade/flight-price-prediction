#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn  as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


train_df=pd.read_excel('Data_Train.xlsx')


# In[3]:


train_df.sample(10)


# In[4]:


train_df.shape


# In[5]:


train_df.info()


# In[6]:


train_df.isnull().sum()


# In[7]:


train_df.dropna(inplace=True)


# In[8]:


train_df.isnull().sum()


# In[9]:


train_df['Date_of_Journey'].value_counts()


# In[10]:


train_df['journey_day']=pd.to_datetime(train_df['Date_of_Journey'], format="%d/%m/%Y").dt.day


# In[11]:


train_df['journey_month']=pd.to_datetime(train_df['Date_of_Journey'], format='%d/%m/%Y').dt.month


# In[12]:


train_df.head()


# In[13]:


train_df.drop('Date_of_Journey', inplace=True, axis=1)


# In[14]:


train_df['departure_hour']=pd.to_datetime(train_df['Dep_Time']).dt.hour
train_df['departure_min']=pd.to_datetime(train_df['Dep_Time']).dt.minute


# In[15]:


train_df.head()


# In[16]:


train_df.drop('Dep_Time',axis=1, inplace=True)


# In[17]:


train_df['arrival_hour']=pd.to_datetime(train_df['Arrival_Time']).dt.hour
train_df['arrival_minute']=pd.to_datetime(train_df['Arrival_Time']).dt.minute


# In[18]:


train_df.drop('Arrival_Time',axis=1, inplace=True)


# In[19]:


train_df.head()


# In[20]:


"5h 25m".split()


# In[21]:


len("5h 25m".split())


# In[22]:


duration = list(train_df['Duration'])
for i in range(len(duration)) :
    if len(duration[i].split()) != 2:
        if 'h' in duration[i] :
            duration[i] = duration[i].strip() + ' 0m'
        elif 'm' in duration[i] :
            duration[i] = '0h {}'.format(duration[i].strip())
duration_hours = []
duration_minutes = []  
 
for i in range(len(duration)) :
    duration_hours.append(int(duration[i].split()[0][:-1]))
    duration_minutes.append(int(duration[i].split()[1][:-1]))


# In[23]:


train_df['duration_hrs']=duration_hours
train_df['duration_mins']=duration_minutes


# In[24]:


train_df.head()


# In[25]:


train_df.drop('Duration', axis=1, inplace=True)


# In[26]:


train_df['Airline'].value_counts()


# In[27]:


sns.countplot(x='Airline', data=train_df)
plt.xticks(rotation=-80)


# In[28]:


airline=train_df['Airline']
airline=pd.get_dummies(airline, drop_first=True)
airline.head()


# In[29]:


Source=train_df['Source']


# In[30]:


Source=pd.get_dummies(Source, drop_first=True)
Source.head()


# In[31]:


Destination=train_df['Destination']
Destination=pd.get_dummies(Destination,drop_first=True)
Destination.head()


# In[32]:


train_df['Route'].value_counts()


# In[33]:


train_df['Destination'].value_counts()


# In[34]:


train_df.drop(['Route','Additional_Info'],axis=1, inplace=True)


# In[35]:


train_df.head()


# In[36]:


train_df['Total_Stops'].value_counts()


# In[37]:


train_df.replace({'non-stop':0, '1 stop':1, '2 stops':2, '3 stops':3, '4 stops':4},inplace=True)


# In[38]:


train_df.head()


# In[39]:


train=pd.concat([train_df, airline, Source, Destination],axis=1)


# In[40]:


train.head()


# In[41]:


train.columns


# In[42]:


train.drop(['Airline','Source', 'Destination'],axis=1, inplace=True)


# In[43]:


train.head()


# In[44]:


train.shape


# In[45]:


test_df=pd.read_excel('Test_set.xlsx')


# In[46]:


test_df.head()


# In[47]:


test_df.dropna(inplace=True)
test_df['journey_day']=pd.to_datetime(test_df['Date_of_Journey'], format="%d/%m/%Y").dt.day
test_df['journey_month']=pd.to_datetime(test_df['Date_of_Journey'], format='%d/%m/%Y').dt.month
test_df['departure_hour']=pd.to_datetime(test_df['Dep_Time']).dt.hour
test_df['departure_min']=pd.to_datetime(test_df['Dep_Time']).dt.minute


# In[48]:


test_df.drop('Dep_Time',axis=1, inplace=True)
test_df['arrival_hour']=pd.to_datetime(test_df['Arrival_Time']).dt.hour
test_df['arrival_minute']=pd.to_datetime(test_df['Arrival_Time']).dt.minute
test_df.drop('Arrival_Time',axis=1, inplace=True)


# In[49]:


duration = list(test_df['Duration'])
for i in range(len(duration)) :
    if len(duration[i].split()) != 2:
        if 'h' in duration[i] :
            duration[i] = duration[i].strip() + ' 0m'
        elif 'm' in duration[i] :
            duration[i] = '0h {}'.format(duration[i].strip())
duration_hours = []
duration_minutes = []  
 
for i in range(len(duration)) :
    duration_hours.append(int(duration[i].split()[0][:-1]))
    duration_minutes.append(int(duration[i].split()[1][:-1]))


# In[50]:


test_df['duration_hrs']=duration_hours
test_df['duration_mins']=duration_minutes


# In[51]:


test_df.drop('Duration', axis=1, inplace=True)
airline=test_df['Airline']
airline=pd.get_dummies(airline, drop_first=True)


# In[52]:


Source=test_df['Source']
Source=pd.get_dummies(Source, drop_first=True)
Destination=test_df['Destination']
Destination=pd.get_dummies(Destination,drop_first=True)


# In[53]:


test_df.drop(['Route','Additional_Info'],axis=1, inplace=True)
test_df.replace({'non-stop':0, '1 stop':1, '2 stops':2, '3 stops':3, '4 stops':4},inplace=True)
test_data=pd.concat([train_df, airline, Source, Destination],axis=1)


# In[54]:


test_data.drop(['Airline','Source', 'Destination'],axis=1, inplace=True)


# In[55]:


test_data.head()


# In[56]:


test_data.shape


# In[57]:


X=train.drop('Price', axis=1)


# In[58]:


y=train.pop('Price')


# In[59]:


print(X.shape)
print(y.shape)


# In[60]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=.30, random_state=1)


# In[61]:


from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor()


# In[62]:


model.fit(X_train,y_train)


# In[63]:


model.score(X_train,y_train)


# In[64]:


predict=model.predict(X_test)


# In[65]:


model.score(X_test, y_test)


# In[66]:


sns.distplot(y_test-predict)


# In[67]:


plt.scatter(y_test,predict)
plt.xlabel('y_test')
plt.ylabel('predict')


# In[68]:


import pickle


# In[69]:


pickle.dump(model,open('flight_fare.pkl','wb'))


# In[70]:


model_r=pickle.load(open('flight_fare.pkl','rb'))


# In[71]:


result=model_r.predict(X_test)


# In[72]:


result


# In[73]:


from sklearn import metrics


# In[74]:


metrics.r2_score(y_test,result)


# In[ ]:





# In[ ]:




