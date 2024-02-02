# -*- coding: utf-8 -*-
"""
Created on Tue Aug  29 11:01:02 2023

@author: Ghafoor
"""

import numpy as np

#Deletion
# parameters
eps = 1e-7
C = 1e6
B = 1e4
# Input

d = 2
e =[3, 2, 4, 1]
n = len(e)

# First layer is input layer, Given as
x = [1, 3]
X = x  
print("Input:")
print("e:", e)
print("d:", d)
#print("m:", m)
print("x:", X)  

#To construct weight matrix for second layer/first hidden layer is L1=W1*X+B1
W1 = []

for l in range(n):
    for k in range(d):
        for m in range(2):
            temp_row = []
            for j in range(d):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)
for l in range(n):
    for k in range(d):
        for m in range(2):
            temp_row = []
            for j in range(d):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)

# for i in W1:
#     print(i)
    
#Bias matrix for second layer/first hidden layer 

B1 = []
# top(bias matrix for alphas)

for l in range(n):
    for k in range(d):
        for m in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if m==0:
                    b = (-(l+1) / eps)+1
                else:
                    b= -(l+1) / eps
                temp_row.append(b)
            B1.append(temp_row)

# bottom(bias matrix for beta)

for l in range(n):
    for k in range(d):
        for m in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if m==0:
                    b = ((l+1) / eps)+1
                else:
                    b=(l+1) / eps
                temp_row.append(b)
            B1.append(temp_row)

 
# for i in B1:
#     print(i)    
    

L1 = [] # alpha and beta nodes
for i in range(len(W1)):
    temp_row = []
    L1_i_entry =np.maximum( (np.dot(W1[i], X)+B1[i]),0)    
    L1.append(L1_i_entry)
    # print('this is index i:', i)
    # print('this is the value L1[i]:', L1_i_entry)
    
    
# print('Printing alpha and beta nodes of second layer/first hidden layer')
# for i in L1:
#     print(i)    

#To construct weight matrix for third layer/second hidden layer is L2=W2*L1+B2
W2 = []
# left-for eta and alphas

A1 = []
for i in range(n):
    for m in range(2):
        temp_row = []
        for l in range(n):
            for k in range(d):
                for q in range(2):
                   w = 0
                   if i == l:
                       if q == 0:
                          w = -1 / eps
                       else: # q = 1
                           w = 1 / eps
                   temp_row.append(w)
        A1.append(temp_row)
         
#right-for betas
A2 = []         
for i in range(n):
    for m in range(2):
        temp_row = []
        for l in range(n):
            for k in range(d):
                for q in range(2):
                   w = 0
                   if i == l:
                       if q == 0:
                          w = -1 / eps
                       else: # q = 1
                           w = 1 / eps
                   temp_row.append(w)
        A2.append(temp_row)

# Concatenating both matrices A and B horizontally

for i in range(len(A1)):
    concatenated_row = A1[i] + A2[i]
    W2.append(concatenated_row)
# print("weight matrix for third layer/second hidden layer")
# print(W2)

#Bias matrix for third layer/second hidden layer 
B2 = []

for i in range(n):
    for m in range(2):
        temp_row = []
        for j in range(1):
            b = 0
            if m==0:
               b = (d/ eps)+1
            else:
               b = d / eps
            temp_row.append(b)
        B2.append(temp_row)

# for i in B2:
#     print(i)

L2 = [] # Eita nodes
for i in range(len(W2)):
    #temp_row = []
    L2_i_entry =np.maximum( (np.dot(W2[i], L1)+B2[i]),0)    
    L2.append(L2_i_entry)
#    print('this is index i:', i)
#    print('this is the value L2[i]:', L2_i_entry)
       
# print('Printing Eita nodes of third layer/second hidden layer')
# for i in L2:
#     print(i) 
  

#To construct weight matrix for fourth layer/third hidden layer L3=W3*L2+B3
W3 = []
    
for i in range(n):
    for m in range(2):
        temp_row = []
        for l in range(n):
            for q in range(2):
              w = 0
              if i == l:
                 if q==0:
                    w= 1 / eps
                 else:      
                    w = -1 / eps
              temp_row.append(w)
        W3.append(temp_row)
##
for i in range(n):
    for m in range(2):
        temp_row = []
        for l in range(n):
            for q in range(2):
              w = 0
              if i == l:
                 if q==0:
                    w= -1 / eps
                 else:      
                    w = 1 / eps
              temp_row.append(w)
        W3.append(temp_row)        
##
for i in range(n):
    temp_row = []
    for l in range(n):
        for q in range(2):
            w = 0
            if l <= i:
               if q==0:
                  w= 1
               else:      
                  w = -1 
            temp_row.append(w)
    W3.append(temp_row)  
    
#print('Printing weight matrix for fourth layer/third hidden layer, W3')
# for i in W3:
#     print(i)

#Bias matrix for fourth layer/third hidden layer
B3 = []

for i in range(n):
    for m in range(2):
        temp_row = []
        for l in range(1):
            b = 0
            if m == 0:
               b = 1
            temp_row.append(b)
        B3.append(temp_row)
##
for i in range(n):
    for m in range(2):
        temp_row = []
        for l in range(1):
            b = 0
            if m == 0:
               b = 1
            temp_row.append(b)
        B3.append(temp_row)
##
for i in range(n):
    temp_row = []
    for l in range(1):
        b = 0
        temp_row.append(b)
    B3.append(temp_row)        
# for i in B3:
#     print(i)

L3 = [] # Mu,lamda and Gamma nodes
for i in range(len(W3)):
#    temp_row = []
    L3_i_entry =np.maximum( (np.dot(W3[i], L2)+B3[i]),0)    
    L3.append(L3_i_entry)
#    print('this is index i:', i)
#    print('this is the value L3[i]:', L3_i_entry)
    
    
# print('Printing Mu, lambda and gamma nodes of fourth layer/third hidden layer')
# for i in L3:
#     print(i) 

#To construct weight matrix for fifth layer/fourth hidden layer L4=W4*L3+B4
W4 = []

# Left
C1 = []
for i in range(n):
    temp_row = []
    for l in range(n):
        for m in range(2):
          w = 0
          if i == l:
             if m==0:
              w=-C
             else:    
              w = C       
          temp_row.append(w)
    C1.append(temp_row)

# middle
C2 = []
for i in range(n):
    temp_row = []
    for l in range(n):
        for m in range(2):
          w = 0
          if i == l:
             if m==0:
                 w = -C
             else:    
                 w = C        
          temp_row.append(w)
    C2.append(temp_row)
#
# right
C3 = []
for i in range(n):
    temp_row = []
    for l in range(n):
        w = 0
        if i == l:
          w=B
        temp_row.append(w)
    C3.append(temp_row)  
##
for i in range(len(C1)):
    concatenated_row = C1[i] + C2[i]+ C3[i]
    W4.append(concatenated_row)   
    
# print("Printing weight matrix for fifth layer/fourth hidden layer, W4")
# for i in W4:
#     print(i)
    
#Bias matrix for fifth layer/fourth hidden layer
B4 = []

# top

for l in range(n):
    temp_row = []
    for i in range(1):
        b = C
        temp_row.append(b)
    B4.append(temp_row)

# print("Printing B4")
# for i in B4:
#     print(i)
    
L4 = [] # Tau nodes
for i in range(len(W4)):
    #temp_row = []
    L4_i_entry =np.maximum( (np.dot(W4[i], L3)+B4[i]),0)    
    L4.append(L4_i_entry)
##
# print('Printing Tau nodes of fifth layer/fourth hidden layer')
# for i in L4:
#     print(i)  
    
#To construct weight matrix for sixth layer/fifth hidden layer L5=W5*L4+B5
W5 = []  
##Top(For sai and tau nodes)##
for i in range(n-d):
    for j in range(d+1):
        for m in range (2):
          temp_row = []
          for l in range(n):
            w = 0
            if (i+1)+j-1 == l:
              w = 1 / eps
            temp_row.append(w)
          W5.append(temp_row)

#bottom (For roh and tau nodes)##       
for i in range(n-d):
    for j in range(d+1):
        for m in range (2):
          temp_row = []
          for l in range(n):
            w = 0
            if (i+1)+j-1 == l:
              w = -1 / eps
            temp_row.append(w)
          W5.append(temp_row)

# print("weight matrix for sixth layer/fifth hidden layer")
# print(W5)    

#Bias matrix for sixth layer/fifth hidden layer
B5 = []

# top
for i in range(n-d):
    for j in range(d+1):
        for m in range (2):
          temp_row = []
          for l in range(1):
              b = 0
              if m==0:
                 b = -(i+1)*B / eps+1
              else:    
                 b = -(i+1)*B / eps 
              temp_row.append(b)
          B5.append(temp_row)

# bottom

for i in range(n-d):
    for j in range(d+1):
        for m in range (2):
          temp_row = []
          for l in range(1):
              b = 0
              if m==0:
                 b = ((i+1)*B+1) / eps+1
              else:    
                 b = ((i+1)*B+1) / eps 
              temp_row.append(b)
          B5.append(temp_row)
    
# print("Printing B5")
# for i in B5:
#     print(i)
    
L5 = [] # Sai and rho nodes
for i in range(len(W5)):
    temp_row = []
    L5_i_entry =np.maximum( (np.dot(W5[i], L4)+B5[i]),0)    
    L5.append(L5_i_entry)
#    print('this is index i:', i)
#    print('this is the value L5[i]:', L5_i_entry)
    
# print('Printing Sai and rho nodes of sixth layer/fifth hidden layer')
# for i in L5:
#     print(i)  
    
#To construct weight matrix for seventh layer/sixth hidden layer L6=W6*L5+B6
W6 = []  

##left(For eta and sye)##
D1 = []

for i in range(n-d):
    for j in range(d+1):
        temp_row = []
        for l in range(n-d):
            for k in range(d+1):
                for m in range (2):
                  w = 0
                  if i == l and j==k:
                     if m==0:
                       w = C
                     else:
                       w=-C  
                  temp_row.append(w)
        D1.append(temp_row)
##         
##right(For eta and rho)##

D2 = []

for i in range(n-d):
    for j in range(d+1):
        temp_row = []
        for l in range(n-d):
            for k in range(d+1):
                for m in range (2):
                  w = 0
                  if i == l and j==k:
                     if m==0:
                       w = C
                     else:
                       w=-C  
                  temp_row.append(w)
        D2.append(temp_row)
##
for i in range(len(D1)):
    concatenated_row = D1[i] + D2[i]
    W6.append(concatenated_row)                  

# print("weight matrix for seventh layer/sixth hidden layer")
# print(W6)    

#Bias matrix for seventh layer/sixth hidden layer   

B6 = []
##(zeta nodes)##
for i in range(n-d):
    for j in range(d+1):
        temp_row = []
        for l in range(1):
            b = -2*C+e[i+j]
            temp_row.append(b)
        B6.append(temp_row)            

# print("Bias matrix for seventh layer/sixth, B6")
# print(B6)  

L6 = [] # zeta nodes
for i in range(len(W6)):
    #temp_row = []
    L6_i_entry =np.maximum( (np.dot(W6[i], L5)+B6[i]),0)    
    L6.append(L6_i_entry)
#    print('this is index i:', i)
#    print('this is the value L6[i]:', L6_i_entry)
    
# print('Printing Zeta nodes for seventh layer/sixth hidden layer')
# for i in L6:
#     print(i) 
    
#To construct weight matrix for eighth layer/seventh hidden layer L7=W7*L6+B7

W7 = []  

for i in range(n-d):
      temp_row = []
      for l in range(n-d):
          for j in range (d+1):
            w = 0
            if l == i:
              w = 1
            temp_row.append(w)
      W7.append(temp_row)
    
# print("weight for Output layer")
# print(W7)    

#Bias matrix for Seventh hidden layer(B7)    

B7 = []
for i in range(n-d):
      temp_row = []
      for l in range(1):
        b=0
        temp_row.append(b)
      B7.append(temp_row)

# print("Bias for Output layer")
# print(B7)  

Y = [] # Output nodes
for i in range(len(W7)):
    #temp_row = []
    Y_i_entry =np.maximum( (np.dot(W7[i], L6)+B7[i]),0)    
    Y.append(Y_i_entry)
values = [int(array[0]) for array in Y]  


print("Output:", values) 
    