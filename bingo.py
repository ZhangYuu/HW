# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 02:11:30 2016

@author: 宇
"""

number=[0]
a=0
check=0
while a!="stop":
    a=0
    a=input("input the number:")
    number.append(int(a))

table = [[1 for i in range(5)] for j in range(5)]

for i in range(5):
    for j in range(5):
        print('the',i+1,'line',j+1,'list:')
        table[i][j]= int(input())
print (table)        
i=0
if table[0][0] in number and table[0][4] in number and table[4][0] in number and table[4][4] in number:
    print("win with four point")

for j in range(5):
    if table[i][j] in number:
        check+=1
if check == 6:
    print ("")
    
    