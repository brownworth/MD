
# coding: utf-8

# Slices and FOR loops (with a little IF in there too!)
# -------
# First, slices:
# --

# For this part, we'll be experimenting with slices. First, let's define a variable and assign some numbers to it.

# In[1]:

some_numbers = range(10)
print some_numbers


# This is a _list_ of numbers. Sometimes we'll say *array* instead of list. But it is technically a **list**. See below when we request its type:

# In[2]:

type(some_numbers)


# This is a 'slice'. Like a slice of cake, we are taking a smaller piece of the whole. Also, like a slice of cake, we can change the size depending on how large of a piece we want. In this case, we are taking a slice with a single element.

# In[3]:

print some_numbers[3]


# We know that the item `some_numbers` is a list, but the things in it are integers. We can use a single element slice to verify this:

# In[4]:

type(some_numbers[3])


# Because Python uses _zero-indexing_ when we ask for the element in position number 3, we are actually asking for the _fourth_ number. Thankfully for this example, the `range` function with a single argument starts with zero. It also shows why we stop at 9, rather than going on to 10.
# 
# For example, we get an error if we try to get the element in position number 10:

# In[5]:

some_numbers[10]


# We can also take slices that are larger than one element by specifying the beginning and end.

# In[67]:

print some_numbers[::-1]
print some_numbers[::-1]
print some_numbers[2:6]


# We can also assign the position numbers to variables and use those in the slices.

# In[7]:

start_position = 2
end_position = 6
print some_numbers[start_position:end_position]


# Note: this starts at the position indicated by the first number and stops _before the position of the second number_. There is a ':' (colon) to separate the two. (This will be really important later)

# Speaking of variable names, we need to be careful when we assign things to variables. Sometimes, we get a copy, and sometimes we just point at the original. Watch this:

# In[9]:

original_numbers = range(6)
print original_numbers
point_at_numbers = original_numbers
copy_the_numbers = original_numbers[:] # we are copying the original_numbers list elements, instead of just pointing at it.
print 'original_numbers =', original_numbers
print 'point_at_numbers =', point_at_numbers
print 'copy_the_numbers =', copy_the_numbers
print '\n'
print 'changing original_numbers . . .'
original_numbers[3] = 7
print 'original_numbers =', original_numbers
print 'point_at_numbers =', point_at_numbers
print 'copy_the_numbers =', copy_the_numbers


# In[12]:

print type(point_at_numbers[3])
print type(copy_the_numbers[3])


# This can be confusing, so it's always good to check the values of your variables when possible, and if you can, know the difference between copying and pointing (it's not always obvious.)

# Up until now, we have used positive numbers to indicate position. This indicates that we are starting from the front (or left) side of the list. If we want, we can start from the back (or right) side of the list using negative numbers. This is **especially useful** when we don't know how many elements are in our list.

# In[13]:

print some_numbers[-2]
print some_numbers[-5:-2]


# Note, in the above example, we started at a point indicated by its position relative to the end. But, if we wanted to travel backwards, it doesn't always work that way.

# In[14]:

print some_numbers[-2:-5]


# In this case, Python assumes that we want to start at the second-to-last element, and get all of the elements leading up to the fifth-to-last element. But you can't travel from left to right and get anything.
# 
# Or, can you?

# In[15]:

print some_numbers[-2:-5:-1]


# here, we introduced the **stride**. We are saying: Let's start at the second-to-last element and stop before the fifth-to-last element, but _go in a negative direction_. (This will also be important later)

# Stride doesn't have to be '-1'. In fact, it can be any integer, positive or negative. If we wanted, we can start at element 2 (the third element), go to the element before 7, and do so with a stride of 3

# In[16]:

print some_numbers[2:7:3]


# We can also use stride by itself.

# In[17]:

print some_numbers[::-1]
print some_numbers[::2] #this is a comment.


# We can also optionally exclude the beginning and/or end numbers, provided we use the ':' to indicate we are skipping a value on one side of it. Look at the difference between the first two entries:

# In[18]:

print some_numbers[4]


# In[19]:

print some_numbers[4:]


# In[20]:

print some_numbers[2::4]


# In[21]:

print some_numbers[:7:2]


# We don't have to use slices with just lists of integers. We can also use it with text (called _strings_).

# In[22]:

some_text = "I am the very model of a modern major general"
print type(some_text)


# In[23]:

print some_text
print some_text[2:22]


# Stride works with strings as well. Want to quickly reverse the letters in a string? Check this out:

# In[24]:

print some_text[::-1]


# You can also use slices with stride on strings, should that be your thing. (it probably won't be; I'm just putting it in here because it's neat).

# In[25]:

print some_text[5:30:4]


# Being able to work with individual slices of characters in a string can be useful, but what if you wanted to work with words instead?

# By converting the string to a list of strings, we can treat each individual word (as separated by space - important later!) as a 
# separate element. The `.split()` method separates a string based upon the space character (by default). We can definitely split on other characters. As such, `.split()` is probably something you will use frequently.

# In[26]:

some_words = some_text.split()
print type(some_words)
print type(some_words[0])
print some_words


# Just like the strings or lists of numbers, we can slice the list of words too.

# In[27]:

print some_words[2:3]
print some_words[-2:-8:-2]


# For Loops!
# --

# It's good to be able to separate slices within other objects, but what if you want to perform an action on the elements of these slices? this is where we use a **for** loop. In this case you are looking to do something _for_ each element within a list, string, etc. Notice the colon ':' and the indent on the following line. 

# In[28]:

for i in some_numbers:
    print i


# Maybe you would like to square each of these numbers.

# In[29]:

for i in some_numbers:
    print i**2


# In[35]:

some_floats = [1.2,6.89,3.58]
type(some_floats[0])
for i in some_floats:
    print i**2.5


# In[39]:

print type(3/2)
print type(3.0/2)
print type(3/2.0)


# Maybe you would like to count backwards with a message (and maybe save your sanity on a car ride).

# In[ ]:

for i in some_numbers[10:0:-1]:
    print i,'bottles of beer on the wall.'
    print i,"bottles of beer!"
    print "Take one down, pass it around."
    print i-1,"bottles of beer on the wall."


# Slices can be used in lots of locations. Here we're going through the words incrementally, (also known as _iterating_) and printing the first two characters of each word. Also note, we don't have to use 'i' as the variable. In this example, since I'm looking for 'a word' in a list of 'some words', it seemed to make sense to go ahead and name my variables in such a way that might help me (or someone else) understand what I was thinking here.

# In[43]:

for a_word in some_words:
    print a_word[0:2]


# Why not include a condition for whether or not we print a word. In this case, we want to see **if** the word contains the letter 'n'. Also notice the second level of indention.

# In[46]:

for a_word in some_words:
    if 'a' in a_word:
        print a_word


# We can also do some for loops, and if statements using list comprehension. It's similar to what we saw above, but returns the result as a list.

# In[45]:

[a_word[0:2] for a_word in some_words]


# In[47]:

[a_word for a_word in some_words if 'a' in a_word]


# We can measure other criteria for the if statement. For example:

# In[48]:

[a_word for a_word in some_words if len(a_word) > 4]


# And, if we want to get really confusing, we can create a list within the list comprehension. For this, we're doing the following:
# for each word (a_word) in the list of words (some_words),
# - display the word in UPPERCASE letters
# - reverse the letters using a slice, and then write it in UPPERCASE letters
# - use the `len()` function to say how many letters are in each word (a_word)
# 
# and, combine all of that into a list of lists!

# In[50]:

craziness = [[a_word.upper(), a_word[::-1].upper(), len(a_word)] for a_word in some_words]


# In[52]:

craziness[3][2]

