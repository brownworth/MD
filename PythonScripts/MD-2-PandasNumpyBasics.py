
# coding: utf-8

# First deal with the imports. Import Pandas and NumPy. We primarily use the shortcut/alias names to make typing them easier. That, and these aliases are fairly universal - most documentation you read is likely to have them written this way.

# In[ ]:

import pandas as pd
import numpy as np


# Below, we are importing a list of integers. In this case, it might be grades for a test. Here we use the Pandas library (pd) to create a Pandas object called a _Series_.

# In[ ]:

series_a = pd.Series([90,85,88,86,91,79,82,65,88,87,96])


# If you are familiar with tabular data (CSV, Excel, Google Sheets, etc.) a series is similar to a single column. Similar in that it has a single column of values, but automatically assigns an index to the values as well. This is SUPER important - Pandas LOVES a good index.

# In[ ]:

series_a


# Pandas provides some methods to series. Here we can easily calculate the mean and median.

# In[ ]:

print series_a.mean()
print series_a.median()


# You can even drop duplicate values. If you are curious about what is available to you within a certain context, press `tab` after the series name and you can see the methods. You can even select from the dropdown list with the arrow keys and `enter` to confirm. Below is the `.drop_duplicates()` method. It will drop any entries whose values have already been represented above it in the Series. Notice that the second 88 (position 8) is dropped?

# In[ ]:

series_a.drop_duplicates()


# For the most part, unless you say specifically, the functions are not destructive. Even though we dropped the duplicates, they're still in there when we call the Series.

# In[ ]:

series_a


# Let's assign some usernames. First establish a list. Then, like before, we pass that list to Pandas and create a Series:

# In[ ]:

student_names = pd.Series(['WHARTNE','PTROUGH','JPERTWE','TBAKER','PDAVISO','CBAKER',
                 'SMCCOY','PMCGANN','CECCLES','DTENNAN','MSMITH','PCAPALD'])


# Also, like before, Pandas has assigned an index to our list.

# In[ ]:

student_names


# By using dictionaries (another python object) we can concatenate two series together on a specific axis, and name the columns at the same time. Below, we are creating an object called a DataFrame from two Series. Simply put, a DataFrame is a Series of one or more Series. In this case, we are aligning them as columns next to each other, so we are saying `axis=1`.

# In[ ]:

grades = pd.concat({'Names':student_names,'Midterm':series_a},axis=1)
grades
# grades.transpose().sort_index(ascending=False)


# If you are confused about **axis=0** vs. **axis=1**, watch what happens when we `.concat()` on **axis=0**:

# In[ ]:

axisTest = pd.concat([series_a,student_names],axis=0)
axisTest


# I like to think of `axis=0` as being vertical - you are adding rows to a Series or Dataframe at the bottom of the current object. By contrast, `axis=1` is horizontal. You are adding columns to the right of the current object. *I hope that didn't confuse matters further.*

# When concatenating Series into a DataFrame, Pandas will do its best to align them by the index. In this case, however, we have more names than grades. Pandas and NumPy know this, and added a `NaN` where data was missing. `NaN` is NumPy's way of saying there is **N**ot **a** **N**umber here, and should be recognized as being invalid.
# 
# To correct this cell, it should be a simple matter of providing the coordinates of the cell, and assigning the value.
# 
# ..._well, it should be easy..._

# In[ ]:

grades[1,11] = 85
grades


# Since we did not format the cell coordinates correctly, Pandas assumed that we were creating a new column and setting its values to the grade specified. That obviously didn't work, so let's delete it using the `.drop()` method. Be sure to specify the axis, in case you have a row named the same as one of your columns (hey, it's possible). Also, let's reassign the edited DataFrame back to itself. Otherwise, the `.drop()` function just returns a **view** of the grades DataFrame with the column dropped, without actually dropping it.

# In[ ]:

grades = grades.drop((1,11),axis=1)


# In[ ]:

grades


# Now, let's look at ways to index into a Series and DataFrame. There are three indexing methods:
# - `.ix[]`
# - `.loc[]`
# - `.iloc[]`
# 
# The first, `.ix[]` is the most friendly. It will first attempt to look up what you provide as a string, and if it can't find the string, look up based upon integer. 

# In[ ]:

grades.ix[7,'Midterm']


# We have used the .ix[] and supplied the row with the index 7, and the column 'Midterm'. For now, something like this is as simple as we need to be. We will DEFINITELY be coming back to this...
# 
# In the meantime, let's fill that space with a grade using '=', the assignment operator.

# In[ ]:

grades.ix[11,'Midterm'] = 85


# Checking the DataFrame, we can see that the grade is in the right place.

# In[ ]:

grades


# We can also check the datatypes of the variables thus far:

# In[ ]:

type(series_a)


# In[ ]:

type(grades)


# The `.info()` method provides a little more detail about the object. In this case, we'll look at the grades DataFrame.

# In[ ]:

grades.info()


# We can see information about the column heads.

# In[ ]:

grades.columns


# Here is some statistical information about the numerical column(s).

# In[ ]:

grades.describe()


# Masking
# --
# Masking is a way of hiding (or showing) cells based upon a Series/DataFrame of boolean (True/False) values. It is a very powerful way to do queries, provided you are willing to do a little work on the front end.

# Perhaps, we want to see every row where the 'Midterm' is greater than 85.

# In[ ]:

grade_threshold = 85
grades['Midterm'] > grade_threshold


# We can also assign this list of boolean values to a variable, and use it as a mask.

# In[ ]:

b_threshold = grades['Midterm'] > grade_threshold
grades[b_threshold]


# Let's add some more grades into this class. We'll use the NumPy random integer method...

# In[ ]:

np.random.randint(69,high=100,size=12)


# ...and assign it to the final variable. Don't worry if your numbers look different. Each time this page is re-run, the random number generator will create a new list. In fact, this second execution is different from the first. See?

# In[ ]:

final = pd.Series(np.random.randint(69,high=100,size=12))


# In[ ]:

final


# Now, let's use the `.concat()` method to concatenate the grades DataFrame with the final Series on axis 1. We'll go ahead and explicitly name the columns as well.

# In[ ]:

grades_final = pd.concat([grades,final],axis=1)
grades_final.columns = ['Midterm','Names','Final']


# In[ ]:

grades_final


# The index on the left doesn't make much sense in the context of the grades, so let's make the index equal to the names, and reassign to the `grades_final` DataFrame.

# In[ ]:

grades_final = grades_final.set_index('Names')


# In[ ]:

grades_final


# Now, let's add another column to the DataFrame, averaging the values in each row.

# In[ ]:

grades_final['Avg.'] = grades_final.mean(axis=1)
grades_final


# Now, let's make a mask **in place**, getting every average greater than some grade.

# In[ ]:

grades_final[grades_final['Avg.']>85]


# We're not limited to built-in functions for extra cells, we can even make a weighted average for the two grades:

# In[ ]:

grades_final['W.Avg.'] = (grades_final['Midterm'] *.4 + grades_final['Final'] *.6)
grades_final


# Using a boolean AND `&` or a boolean OR `|` we can combine masks to have compound results.

# In[ ]:

grades_final[(grades_final['Avg.'] > 85) & (grades_final['Midterm'] > 80)]

