# -*- coding: utf-8 -*-
"""Unit2_Dictionary_Assignment_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LfRjYb2a7Wzpm8XFX6qzrvO67PKHByR_

<a href="https://colab.research.google.com/github/niteen11/lagcc_data_analytics_micro_credential/blob/master/Unit%202%20-%20Python%20Fundamentals/Assignments/Unit2_Dictionary_Assignment_5.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Intrdouction to Python - Dictionary - Assignment #5

## 1.	Create a simple dictionary that stores 2 variables, for example: first and last name.
"""

#create a dictionary 
#store 2 variables, first and last name

full_name = {'first_name': 'Jade', 'last_name': 'Wang'}

"""## 2.	Print out those variables stored in your previous dictionary. """

#print the variables

print(full_name['first_name'])
print(full_name['last_name'])

"""## 3.	Add a message to those variables on printing: for example: “Hello, firstname lastname!”"""

#add message to the variables

full_name_1 = full_name['first_name'] + " " + full_name['last_name']
print("Hello, " + full_name_1 + "!")

"""## 4.	Create a dictionary that holds 2 key: value pairs:

a.	Look through your dictionary and print each pair,

"""

#create a dictionary with value pairs

full_name['Age'] = '30'
full_name['Annual Salary'] = '$100000' 
print(full_name)









