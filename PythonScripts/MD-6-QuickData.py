
# coding: utf-8

# Quick Data!
# ---

# Now, as a "fun" exercise, we're just going to go quickly through some of the stuff we covered earlier to demonstrate how Python, Pandas, NumPy and MatPlotLib can work together. I don't know how you spend your evenings, but me? I like to check out datasets on data.gov!

# Standard library imports...

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# Here's a simple CSV file showing some power usage for zip codes over time. I've added the URL in case the file gets corrupted. Please feel free to download your own, though the column and row names (not to mention Series and DataFrame sizes may be different).

# In[ ]:

# http://catalog.data.gov/dataset/average-monthly-residential-energy-usage-by-zip-code-0487d
power_data = pd.read_csv(r'Average_monthly_residential_energy_usage_By_zip_code.csv',header=0)
power_data.columns.values


# This is here to remind us to look at the inline documentation for `pd.read_csv`.

# In[ ]:

# pd.read_csv?


# Looking at the data in the column 'Location 1'. It's weirdly formatted, where it appears that there is a zip code, followed by some coordinates. 

# In[ ]:

power_data.ix[0,'Location 1']


# We're not really interested in the coordinates (today), so let's grab what is presumably a zip code. We could use regular expressions, but since we're only ever looking at the first five characters, a simple slice will do.

# In[ ]:

power_data['Location 1'] = power_data['Location 1'].str[:5]


# In[ ]:

power_data = power_data.set_index('Location 1')


# In[ ]:

power_data = power_data.sort_index()


# We'll change the index name to something more informative than 'Location 1'

# In[ ]:

power_data.index.name = 'Zip Code'


# Now, let's talk about `pd.date_range()`. This is a very powerful function within Pandas for creating ranges of dates.

# In[ ]:

# pd.date_range?


# By default, `pd.date_range()` assumes a daily frequency:

# In[ ]:

pd.date_range(start='01-01-2005',end='01-10-2005')


# in the information output, there's a *freq='D'*. This means that the frequency is 'Daily'. We could use other codes, such as 'A' for __A__nnually, 'M' for __M__onthly, or even 'H' for __H__ourly.

# In[ ]:

pd.date_range(start='01-01-2005',end='08-10-2005',freq='M')


# We can even specify when we want the repetition to occur. Below, we're using 'AS-JAN'. This means the frequency is __A__nnual,  __S__tarting on __JAN__uary 1st.

# In[ ]:

pd.date_range(start='01-01-2005',end='01-01-2012',freq='AS-JAN')


# In[ ]:

dateColumnNames = pd.date_range(start='01-01-2005',end='01-01-2012',freq='AS-JAN')


# It may seem a little repetitive to then bring it back to a string for processing, but this is largely an exercise, so we're just going to convert to a string, and just use the year for simplicity.
# 
# _NOTE: this functionality may cause an error unless you are using a current version of Pandas/NumPy._

# In[ ]:

# strftime.org
dateColumnNames.strftime('%Y')


# In[ ]:

power_data.columns = dateColumnNames.strftime('%Y')


# In[ ]:

power_data['Average'] = power_data.mean(axis=1)


# In[ ]:

power_data


# In[ ]:

power_data.ix[:,7].name


# In[ ]:

power_data.index[0:10].values


# In[ ]:

barWidth = .75
plt.figure(figsize=(12,8))
plt.barh(np.arange(10),power_data['Average'][0:10],barWidth)

plt.title('Power Consumption by Zip Code in Los Angeles')
plt.xlabel('Usage in kWh')
plt.ylabel('Zip Code')
plt.yticks(np.arange(10)+ (barWidth / 2),power_data.index[0:10],rotation=90);


# In[ ]:

startZip = 0
samples = 10
endZip = startZip + samples

dataYear = '2012'

index = np.arange(samples)
powerZip = power_data.ix[startZip:endZip].index.values
barWidth = .4
powerAvg = power_data.ix[startZip:endZip,'Average'].values
powerYear = power_data.ix[startZip:endZip,dataYear].values

power_chart = plt.figure(figsize=(16,8))
power1 = plt.bar(index, powerAvg, barWidth, color='#f1c40f', label='Average')
power2 = plt.bar(index + barWidth, powerYear, barWidth, color='#dc7633', label=dataYear)
plt.xticks(index + barWidth, powerZip)
plt.title('Power Consumption by Zip Code in Los Angeles')

# don't forget to switch these, now that the bars are vertical:
plt.ylabel('Usage in kWh')
plt.xlabel('Zip Code')
plt.legend(loc=0);

