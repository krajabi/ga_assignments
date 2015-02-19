"""
1. What's the primary difference between the following two ipython magic (%)
commands? -- 

#Pylab inline allows you to put all your figures inside your notebook but is also inclusive of importing matplotlib
"""

%matplotlib inline
%pylab inline

"""
2.  We have a file called "ads_performance.csv" which includes the following
header rows, and one row and the end that sums the total of the dataset.

Google Adwords Perfomance
February 16 2015, February 22 2015
Brand
date, ad_id, strategy_group, description, spend, spend_wfees, impressions, clicks
02/16/2015, 1772, 'team_bananas', 'Did you know there are 100s of bananas? Click here to find out more!', 23.75, 24.33, 107771, 10

Write the pd.read_csv function that would ignore the additional headers, use the
correct header for the column names, and ignore the very last row.
"""
ads = pd.read_csv('../data/GoogleAdwordsPerfomance.csv'), header = 0, skiprows = 0, na_values='?')
header_row = ['date', 'ad_id', 'strategy_group', 'description', 'spend', 'spend_wfees', 'impressions', 'clicks']
ads.columns = header_row

"""
3. With the ads dataset stored in name `ads`, write code that'd create a subset
of just ad_id 200 where the spend was more than 30 dollars

subset = ads['ad_id'] == 200 &  ads['spent'] > 5.0
print subset

"""
4. We want to aggregate the sum of spend by day and ad. What code would return
back that dataset?
"""

ads.groupby('day').aggregate(sum)
ads.groupby('ad').aggregate(sum)

"""
5. Explain what the following code block is doing, line by line.
"""
import matplotlib.pyplot as plt
from __future__ import division
#importing library

ads['ctr'] = ads['clicks'] / ads['impressions']
#trying to get a proportion/subset of the original data set

fig = plt.figure()
plt.subplot(1, 2, 1)
plt.hist(ads.spend)
#plotting a histogram of the spending data

plt.subplot(1, 2, 2)
plt.plt(ads.spend, ads.ctr, 'g.')
plt.show()
#plotting a scatterplot of the spending data

"""
6-8. Imagine we're viewing the following coefficient table for the following
regression:

(ad_id1772 is either 1 or 0, meaning it was ad 1772, or it was not)
'spend ~ impressions + clicks + ad_id1772'

column          coefficient         pvalue
y_intercept     0.02                0.000
impressions     0.00057             0.038
clicks          0.976               0.78
ad_id1772      -0.5                 0.02


6. How much can we assume the ad cost to place online, based on it having
   no impressions?
   #since there are no impressions and the ad_id value is boolean, we can assume the majority of the spend will come from the clicks. Using that, we can assume a pretty strong linear relationship between # of clicks and amount spent

7. Which part of the model seems insignificant to solving for cost?
#clicks because of a high p value
8. What effect does ad 1772 have on the cost of the ad?
#ad 1772 appears to have a negative correlation between the cost of the ad and the presence of the ad
"""


"""
9. What does a Trellis plot allow you to do?
What python library does theTrellis plot come from?
"""
#Trellis plots are graphs that display a variable or the relationship between variables, conditioned on one or more other variables.
#They come from the rplot library

"""
10. What does the reset_index() function do on a DataFrame?
Describe an instance you might need to use it.
"""
#If you have a DataFrame and they have a particular index, reset_index restores this to default indexing starting from 0
#You would use this if you have a DataFrame with certain values that have been cleared. This helps eliminate this inevitable offset that would be created.
"""