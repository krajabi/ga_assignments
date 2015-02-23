
# coding: utf-8

# In[50]:

# Data source: https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam
get_ipython().magic(u'pylab inline')


# In[170]:

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)


# In[171]:

df = pd.read_csv('data/nycdeath.csv')


# In[176]:

#Key exploration objectives:
#1)How death type differs by race in 2011
#2)How does gender affect leading death type in 2011 
#3)How has leading death type changed from 2007 to 2011


# In[177]:

df.describe()


# In[178]:

#Group by year to assess 
gryear = df.groupby('Year').aggregate(sum)  
gryear.describe()


# In[179]:

gryear.plot(kind='bar')


# In[181]:

#only want to examine 2011 data/subset
year_2011 = df[df.Year==2011]
#Subsetting the data by year to focus on 2011 data for some parts of my analysis


# In[182]:

#Create new DataFrame from 2011 data; sort by count to uncover top causes of death
#QUESTION 1: How death type differs by race in 2011
ct_2011 = year_2011[['Count', 'Ethnicity', 'Sex', 'CauseofDeath']]
sort_ct_2011=ct_2011.sort(columns='Count', axis=0, ascending=False)


# In[183]:

api_data = sort_ct_2011[sort_ct_2011.Ethnicity == 'ASIAN & PACIFIC ISLANDER']
api_data.head(6)
#Asian subset: we can see cancer is the leading cause of death for Asians, but heart disease is the leading cause of death for all the other races that were sampled


# In[184]:

his_data = sort_ct_2011[sort_ct_2011.Ethnicity == 'HISPANIC']
his_data.head(6)
#Hispanic subset


# In[185]:

nhb_data = sort_ct_2011[sort_ct_2011.Ethnicity == 'NON-HISPANIC BLACK']
nhb_data.head(6)
#Black subset: Diabetes was the third leading cause of death in non-hispanic blacks, but not as high for other ethnicities 


# In[186]:

nhw_data = sort_ct_2011[sort_ct_2011.Ethnicity == 'NON-HISPANIC WHITE']
nhw_data.head(6)
#White subset


# In[187]:

#Now, let's see how
HIV_data = sort_ct_2011[sort_ct_2011.CauseofDeath == 'HUMAN IMMUNODEFICIENCY VIRUS DISEASE']
HIV_data
#Wow! If you are non-hispanic black male, you have more than triple the chance of dying from HIV than non-hispanic white males.
#Additionally, if you are a hispanic  male, you have more than double the chance of dying from HIV than non-hispanic white males.


# pct_2011 — want to narrow down my DataFrame to only my columns of interest

# Now, using a pivot table to analyze aggregate changes to causes of death over the years

# In[188]:

#QUESTION 2)How does gender affect leading death type in 2011 

sex_male = year_2011[year_2011.Sex=='MALE']
#sex_male_all=sex_male.sort(columns='Count', axis=0, ascending=False)

pivoted_sex = year_2011.pivot_table(values='Count',
                 columns='Sex',
                 index='CauseofDeath',
                 aggfunc='sum')
pivoted_sex


# In[189]:

pivoted_sex.plot(figsize=(30, 6))
#Chronic Lower Respiratory disease 4th leading cause males, 5th in females
#Cerebrovascular disease 4th leading in women, 6th leading in men
#Assault/homicide 10th leading cause in men, 18th in women
#Alzheimer’s 8th leading cause in females, 16th in men


# In[208]:

#QUESTION 3)How has leading death type changed from 2007 to 2011
pivoted_df = df.pivot_table(values='Count',
                 columns='Year',
                 index='CauseofDeath',
                 aggfunc='sum')
pivoted_df
#Snapshot/overview of how death type has changed over the years


# In[217]:

#Heart disease gradually declined (went from 21195 in 2007 to 16722 in 2011)
pivoted_df.plot(figsize(20,5))
pivoted_df.plot(kind='bar')

