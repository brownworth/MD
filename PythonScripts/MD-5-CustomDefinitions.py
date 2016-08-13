
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# Here we are going to use a combination of Pandas DataFrame functionality and a NumPy method to quickly create a 6x6 DataFrame populated with the numbers 0 - 35, with specified column heads. If you're looking to practice with DataFrames, the `np.arange().reshape()` methods are an easy way to create one quickly.

# In[2]:

test_data = pd.DataFrame(np.arange(36).reshape(6,6),columns=('alpha','bravo','charlie','delta','echo','foxtrot'))


# In[3]:

test_data


# Here we are defining a function with a single argument. In this case, it takes a single value `cellNum` and applies the inner workings of the function to it. We're also using an `else:` statement to determine an action when our initial `if:` proves to be false. _Remember your indentation!_

# In[4]:

def num_mod(cellNum):
    if cellNum % 2 == 0:
        return cellNum, "is even"
    else:
        return cellNum, "is odd"


# Remember `.apply()` with `pd.to_datetime` earlier? The `.applymap()` method is a way to _apply_ a function to elements individually. We can index out specific cells and then apply a function. It can even be one we defined ourselves.

# In[5]:

test_data.ix[0:2,0:3].applymap(num_mod)


# Where `.applymap()` can apply to individual cells, `.apply()` works with rows, columns, or the entire DataFrame. For this function, we are adding specifically named columns within the DataFrame. We are passing a row as an argument, and the function knows to work with certain columns and ignore the rest.

# In[6]:

def row_add(row):
    return row.loc['bravo'] + row.loc['delta'] + row.loc['foxtrot']


# In[7]:

test_data.apply(row_add,axis=1)

