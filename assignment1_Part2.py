#!/usr/bin/env python
# coding: utf-8

# In[60]:


#IS211 Week1 Part 2  - Simple Class

# Create a class called Book -- This class should have the following properties:
# A.) Two attributes, author and title, both of which should be initialized to the blank string
# B.) An __init__ function that takes in an author and a title, and sets them to the object variables
# C.) A function called display, which when called, simply prints out a string representing the book

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
       print (self.title,"written by",self.author)


# In[61]:


# Instantiate two objects from this class. 
# The first object represents the book ‘Of Mice and Men’,written by John Steinbeck 
# the other is ‘To Kill a Mockingbird’ by Harper Lee.

book1 = Book("Of Mice and Men", "John Steinbeck")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Print both of these objects to the screen by calling their display() functions

book1.display()
book2.display()


# In[ ]:





# In[ ]:




