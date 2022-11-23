#!/usr/bin/env python
# coding: utf-8

# Exploratory Data Analysis on Indian Premier League(IPL) 2017

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Importing the dataset
ipl=pd.read_csv('C:/Users/hp/Downloads/matches.csv')


# In[3]:


ipl.head()


# In[6]:


#Count of player of the match
ipl["player_of_match"].value_counts()


# In[9]:


# Top 10 counts of the player of the match
ipl["player_of_match"].value_counts()[0:10]


# In[6]:


#Fetching the names of player who won player of the match award
list(ipl["player_of_match"].value_counts()[0:7].keys())


# In[5]:


# Plotting bar chart for theb player of the match award
plt.figure(figsize=(15,5))
plt.bar(list(ipl["player_of_match"].value_counts()[0:10].keys()),(ipl["player_of_match"].value_counts()[0:10]),color="r")
plt.legend()
plt.title("bar graph of the highest MOM")
plt.show()


# In[4]:


#Fetching the count of the types of results
ipl["result"].value_counts()


# In[23]:


#Extracting the number of toss wins w.r.t each team
ipl["toss_winner"].value_counts()


# In[13]:


#fetching the records of the wins of teams batting first
batting_first=ipl[ipl["win_by_runs"]!=0]
batting_first[0:5]


# In[22]:


#making histogram of number of wins for batting first
plt.figure(figsize=(5,7))
plt.hist(batting_first["win_by_runs"],bins=10)
plt.title("no. of wins batting first")
plt.xlabel("runs")
plt.show()


# In[49]:


#No.of wins w.r.t each team after batting first
batting_first["winner"].value_counts()


# In[24]:


#PLotting the top 3 teams having maximum numbers of wins after batting first.
plt.figure(figsize=(10,5))
plt.bar(list(batting_first["winner"].value_counts().keys()[0:3]),list(batting_first["winner"].value_counts()[0:3]),color=["blue","yellow","Orange"])
plt.show()


# In[29]:


#Pie Chart for determining the win percentage of top 5 teams after batting first.
plt.figure(figsize=(10,5))
plt.pie(list(batting_first["winner"].value_counts()[0:5]),labels=batting_first["winner"].value_counts().keys()[0:5],colors=("blue","Yellow","Orange","purple","Red"),explode=(0.1,0,0,0,0),startangle=180,autopct="%0.1f%%")
plt.show()


# In[17]:


#fetching the records of the wins of teams batting second
batting_second=ipl[ipl["win_by_wickets"]!=0]


# In[18]:


batting_second.head()


# In[19]:


#making histogram of number of wins for batting second
plt.figure(figsize=(7,7))
plt.hist(batting_second["win_by_wickets"],bins=20)
plt.title("distribution of runs")
plt.show()


# In[36]:


#No.of wins w.r.t each team after batting first
batting_second["winner"].value_counts()


# In[43]:


#PLotting the bar chart for top 3 teams having maximum numbers of wins after batting second.
plt.figure(figsize=(10,5))
plt.bar((batting_second["winner"].value_counts().keys()[0:3]),(batting_second["winner"].value_counts()[0:3]),color=["#800080","b","r"])
plt.show()


# In[27]:


#Pie Chart for determining the win percentage of top 5 teams after batting second.
plt.figure(figsize=(10,5))
plt.pie(list(batting_second["winner"].value_counts()[0:5]),labels=batting_second["winner"].value_counts().keys()[0:5],explode=(0.1,0,0,0,0),startangle=180,colors=["#800080","blue","red","Yellow","Cyan"],autopct="%0.1f%%")
plt.show()


# In[31]:


#Number of matches played in each season
ipl['season'].value_counts()


# In[32]:


#Number of matches played in each city
ipl["city"].value_counts()


# In[38]:


#Finding out the number of matches win after winning the toss
np.sum(ipl["toss_winner"]==ipl["winner"])


# In[44]:


ipl.shape


# In[48]:


#Win percentage after winning toss 
(393/756)*100


# In[51]:


#Import the deliveries dataset
deliveries=pd.read_csv("C:/Users/hp/Downloads/deliveries.csv")


# In[52]:


deliveries.head()


# In[54]:


#finding unique match_id
deliveries['match_id'].unique()


# In[55]:


#Fetching the data of match 1
match_1=deliveries[deliveries['match_id']==1]


# In[80]:


match_1.head()


# In[85]:


match_1.shape


# In[58]:


#Analysing the 1st innings of the 1st match
srh=match_1[match_1['inning']==1]


# In[60]:


# Finding the ways of runs for srh
srh['batsman_runs'].value_counts()


# In[61]:


#Kinds of dismissal
srh['dismissal_kind'].value_counts()


# In[62]:


#Analysing the 2nd innings of the 1st match
rcb=match_1[match_1['inning']==2]


# In[63]:


# Finding the ways of runs for rcb
rcb['batsman_runs'].value_counts()


# In[64]:


#Kinds of dismissal
rcb['dismissal_kind'].value_counts()


# In[ ]:




