# -*- coding: utf-8 -*-
"""DAY 4 ASSIGNMENT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18tDKYGt5rRS8yLIt6sy2fWbAxwAx-558
"""



"""Day 4 Assignmenet:
1.Find all occurence of substring in the given string.

print the index values "we"

what we think we become;we are python programmer.
"""

string = 'what we think we become;we are python programmer'
substring = 'we'

index = string.find(substring)
print(index)

string = 'what we think we become;we are python programmer'
substring = 'we'
start=8

index = string.find(substring,start)
print(index)

string = 'what we think we become;we are python programmer'
substring = 'we'
start=15

index = string.find(substring,start)
print(index)

"""2.explain using islower() isupper() with different kind of strings.
1.isupper()
"""

string = 'LETSUPGRADE PYTHON'
print(string.isupper()) 
  
string = 'letsupgrade python'
print(string.isupper())

"""2.islower()"""

string = 'letsupgrade python'
print(string.islower()) 
  
string = 'LETSUPGRADE PYTHON'
print(string.islower())