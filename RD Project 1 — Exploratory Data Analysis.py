
# coding: utf-8

# In[1]:

# Data source: https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam
get_ipython().magic(u'pylab inline')


# In[90]:

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (15, 5)


### df = pd.read_csv('data/nycdeath.csv') df.describe()

# In[ ]:

#Group by year to assess 
gryear = df.groupby('Year').aggregate(sum)  
gryear.describe()
gryear.plot(kind='bar')


# In[14]:

year_2011 = df[df.Year==2011]
year_2011.head()
#Subsetting the data by year to focus on 2011 data for some parts of my analysis


# In[111]:

#Create new DataFrame from 2011 data; sort by count to uncover top causes of death
ct_2011 = year_2011[['Count', 'Ethnicity', 'Sex', 'Cause of Death']]
sort_ct_2011=ct_2011.sort(columns='Count', axis=0, ascending=False)
sort_ct_2011.head()
#Great...but now we need to aggregate all deaths by ethnicity


# In[147]:

#grouping by ethnicity to narrow down how death type differs by race
eth_2011 = year_2011.groupby('Ethnicity', sort = True)
eth_2011.median()
#eth_2011.head()
#max min etc.
#cause of deaths per ethnicity
#total deaths per ethnicity
#Normalize data set by cause of death per ethnicity / total deaths per ethnicity


# pct_2011 — want to narrow down my DataFrame to only my columns of interest

# In[64]:

#eth_2011.sort(columns='Percent', axis=0, ascending=False)


# In[ ]:

gbd = df.groupby('Cause of Death')


# In[25]:

pivoted_df = df.pivot_table(values='Percent',
                 columns='Year',
                 index='Cause of Death',
                 aggfunc='sum')


# Now, using a pivot table to analyze aggregate changes to causes of death over the years

# In[26]:

pivoted_df


# In[73]:

df.hist()


# In[74]:

df.boxplot()
plt.figure(figsize=(8, 6), dpi=80)


# In[75]:

sns.set_style() # sets seaborn "white" to the default matplotlib style
plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)
plt.hist(df.g, bins=20)


# In[ ]:

ethnicity = df['Ethnicity']
year = df['Year']


# In[15]:

# using plot and the '.' notation.
plt.figure(figsize=(8, 6), dpi=80)
plt.plot(ethnicity, year, '.')


# In[ ]:




# In[ ]:




# In[ ]:



