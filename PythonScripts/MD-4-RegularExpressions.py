
# coding: utf-8

# Regular Expressions!
# --
# 
# Like before, we'll begin by importing the libraries we need. In this case, we'll import the Regular Expressions library, 're'.

# In[ ]:

import re


# Let's create some text with a **conspicuous** pattern and assign it to a variable.

# In[ ]:

birdText = "There are 35 Robins, 62 Doves, 18 Thrushes, and 5 Owls over here. Oh, and I forgot that there are 10 Woodpeckers."


# Using the `.findall()` method, we can apply a regular expression to some text, and return the matches as a list. In this first case, we're going to separate out the numbers by themselves. By using `\d+` we are looking for one or more (\d)igits.

# In[ ]:

numbers = re.findall(r'\d+',birdText)

print "numbers =",numbers


# this **numbers** variable is just like any other list, and can be sliced just like before.

# In[ ]:

print type(numbers)
print numbers[2:5]


# if we need the numbers to be `integers` we can use list comprehension to convert them. _(Or later, we'll convert them a different way.)_

# In[ ]:

[int(i) for i in numbers]


# This text also includes a bunch of words that are capitalized. We can do a regular expression to get those into a list of strings as well:
# 
# *(Remember the following from the powerpoint? It's ok if you don't. That business was like fixing a vacuum cleaner after cleaning up a Scrabble board.)*
# 
# `[A-Z]` is a range of characters from uppercase A to uppercase Z, but is only looking for one of them. 
# 
# `[a-z]*` is a range of characters from lowercase a to lowercase z, but this time the asterisk modifier `'*'` indicates that the previous pattern should be included if there are **zero or more** of them.

# In[ ]:

capitals = re.findall(r'[A-Z][a-z]*', birdText)

print "capitals =",capitals


# This found all of the words that were capitalized, including 'I' which had no lowercase letters. Unfortunately, this includes words that are not bird names, so we have to come up with a different pattern to separate them out. We can't just change the modifier from `'*'` to `'+'`, as it would include 'Oh' in the results.
# 
# In the text, each of the bird names is capitalized, but is immediately preceded by a number. So in this case, we will indicate that we are looking for capitalized words that immediately follow one or more digits, `'\d+'` and a single whitespace character, `'\s'`.

# In[ ]:

birds = re.findall(r'\d+\s([A-Z][a-z]*)',birdText)

print "birds =",birds


# notice above, that the expression looks like `\d+\s([A-Z][a-z]*)`. The part surrounded by parenthesis is being **captured**. This allows only the bird names to be added to the list.
# 
# But, we probably would like to include the numbers. To do so, we need to create a second capturing group.

# In[ ]:

birdNums = re.findall(r'(\d+)\s([A-Z][a-z]*)',birdText)

print "birdNums =",birdNums


# Now, the numbers and birds are paired in a list of tuples. But it may not be convenient for us to have the number first. Perhaps, we would like to create a dictionary where we search by a bird name, and it returns the number. With the entries ordered this way, a dictionary would be backwards. It would be like saying "What do I have 10 of? Oh, Woodpeckers!"
# 
# Let's reverse it, using...
# 
# list comprehension and slices!

# In[ ]:

ordered = [birdPair[::-1] for birdPair in birdNums]

print "ordered =",ordered


# Just because it is good to check every once in a while, lets see what types we're dealing with:

# In[ ]:

print type(ordered)
print type(ordered[0])


# Now that we have a list of correctly-ordered tuples, what if we want to make this something searchable? We can use the dict() function on our tuple list and it will convert our tuples into key-value pairs, searchable on the key.

# In[ ]:

birdDict = dict(ordered)
print birdDict


# This looks good, but notice that there are single quotes around the numbers? Even though these appear to be numbers, Python still sees them as strings:

# In[ ]:

print type(birdDict.get('Owls'))


# So, we're going to use dictionary comprehension (similar to list comprehension) and the int() function to convert the pairs into a string and integer.

# In[ ]:

birdInt = {birdName: int(birdCount) for birdName, birdCount in birdDict.iteritems()}


# Let's break this down so that it (hopefully) isn't too intimidating:
# - `birdInt =` 
# 
# -- this is just the part of the assignment, where we are creating a new variable and assigning what comes next.
# - `birdName: int(birdCount)`
# 
# -- We're starting with the open-curly-bracket to indicate that this is a dictionary. We're then using two arbitrarily defined variables to break apart the key and value pairs, separated by a colon ':'. In documentation, you will often see 'k' and 'v' for simplicity, but I'm deliberately choosing to name them something meaningful. I'm also putting the variable birdCount as the argument of the int() function. Even though we are using these variables here, Python doesn't know what they are yet.
# - `for`
# 
# -- here's our longtime buddy, `for`, iterating through the items we supply to it.
# - `birdName, birdCount`
# 
# -- our variables again, but we're defining them as a key-value pair for what comes next.
# - `in`
# 
# -- another of our longtime buddies, hanging out with his friend `for`
# - `birdDict.iteritems()`
# 
# -- ok, this is the new stuff. Basically, to iterate through a dictionary, the syntax is just a little different. Since we are returning the key-value as a pair, we need to **iter**ate through the **items**. It's very similar to the way that lists do it, but the method is just slightly different.
# 
# As we can see, the variable `birdInt` is now a dictionary with string:integer pairs.

# In[ ]:

birdInt


# In[ ]:

birdInt.get('Robins')


# In[ ]:

type(birdInt.get('Robins'))


# We can add to our dictionary, should we need get more information:

# In[ ]:

birdInt['Finches'] = 45


# In[ ]:

birdInt


# What if we want to get something in our dictionary that doesn't exist? For example, our diligent, narratively exquisite ornithologists didn't see any hawks.

# In[ ]:

birdInt.get('Hawks')


# Unfortunately, we didn't see them, and the dictionary doesn't supply any information to us to indicate that. So, when using the .get() method, you can optionally supply an argument that returns a specific value if the key is not found:

# In[ ]:

birdInt.get('Hawks',-999)


# Now, let's combine it with the things we've been doing in Pandas by making this dictionary a DataFrame. Import the libraries:

# In[ ]:

import pandas as pd
import numpy as np


# We're going to use a new method, `.from_dict()`. This allows you to create a DataFrame from a dictionary. If you're curious about how it works, remember to try `pd.DataFrame.from_dict?`
# 
# Basically, we are going to use two arguments: the dictionary (which in this case is called `birdInt`), and telling Pandas how to orient the dataframe. We want to continue using the key as our index, so we'll orient it as such:

# In[ ]:

birdData = pd.DataFrame.from_dict(birdInt,orient='index')


# Rename the index...

# In[ ]:

birdData.index.name = 'BirdType'


# Remember in lesson 3 when we used the `.rename()` method to rename the columns? If we're willing to rename all of them at once (in this case we have only one) we can pass a list of names to the columns property.
# 
# So, let's rename the column(s)...

# In[ ]:

birdData.columns = ['BirdCount']


# Sort the index, but instead of reassigning it to the variable again, `.sort_index()` is a method that allows the argument `inplace='True'` so the index is sorted and written back *in place*.

# In[ ]:

birdData.sort_index(inplace='True')


# Now we are left with something that should look very familiar:

# In[ ]:

birdData

