# -*- coding: utf-8 -*-
"""Day 7 Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yin0DHw812a1APYB1apHg1ZRm_qKCoNl
"""



"""1.Make a new dictionary in which keys become values and values become keys."""

port1 = {21:"FTP",22:"SSH",23:"telnet",80:"http"} 
port2 ={value:key for key,value in port1.items()}
print("The output:",port2)

"""2.Make a new list which conains the sum of number of tuples."""

list1=[(1,2),(3,4),(5,6),(4,5)]
res=[]
for each in range(0,len(list1)):
    a,b=list1[each]
    res.append(a+b)
print(res)

"""3.Make the elements of inner list and tuples to outer lists."""

list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
list2=[i for each in list1 for i in each]
print (list2)