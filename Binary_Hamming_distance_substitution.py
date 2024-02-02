# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:20:36 2024

@author: Mamoona Ghafoor
"""
import numpy as np
# Parameters
eps = 1e-7

#input
d = 2
e = [1,1,0]
#First layer is input layer given as
x = [1, 3]
X = x
print("Input:")
print("e:", e)
print("d:", d)
print("x:", X)
n = len(e)

#To construct weight matrix for second layer/first hidden layer is L1=W1*X+B1
W1 = []

#for alpha nodes     
for i in range(n):  
    for k in range(d):
        for q in range(2):
            temp_row = []
            for j in range(d):
                w = 0
                if k == j:
                    w = 1 / eps  
                temp_row.append(w)
            W1.append(temp_row)
##
#for beta nodes     
for i in range(n):  
    for k in range(d):
        for q in range(2):
            temp_row = []
            for j in range(d):
                w = 0
                if k == j:
                    w = -1 / eps  
                temp_row.append(w)
            W1.append(temp_row)
# print('weight matrix of second layer/first hidden layer')    
# for i in W1:
#     print(i)
    
#Bias matrix for second layer/first hidden layer

B1 = []
# (bias of alpha nodes)

for i in range(n):
    for k in range(d):
        for q in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if q==0:
                    b = -(i+1)/eps +1
                else:
                    b= -(i+1)/eps
                temp_row.append(b)
            B1.append(temp_row)

# (bias of beta nodes)

for i in range(n):
    for k in range(d):
        for q in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if q==0:
                    b = (i+1)/eps +1
                else:
                    b= (i+1)/eps
                temp_row.append(b)
            B1.append(temp_row)
    
L1 = [] # psi and rho nodes
for i in range(len(W1)):
    L1_i_entry =np.maximum( (np.dot(W1[i], X)+B1[i]),0)   
    L1.append(L1_i_entry)
    # print('this is index i:', i)
    # print('this is the value L1[i]:', L1_i_entry)
    
# print('alpha and beta nodes for second layer/first hidden layer')
# for i in L1:
#     print(i)
##################
#To construct weight matrix for third layer/second hidden layer is L2=W2*L1+B2
W2 = []
# eta nodes
A1=[]
for i in range(n):
   for p in range(2):
       temp_row = []
       for l in range(n):  #(alpha nodes)
          for k in range(d):
              for q in range(2):
                  w = 0
                  if i == l:
                     if q==0:
                         w= 1 / eps
                     else: 
                         w = -1 / eps
                  temp_row.append(w)
       A1.append(temp_row)
## 
A2=[]      
for i in range(n):
   for p in range(2):
       temp_row = []
       for l in range(n):  #(beta nodes)
          for k in range(d):
              for q in range(2):
                  w = 0
                  if i == l:
                     if q==0:
                         w= 1 / eps
                     else: 
                         w = -1 / eps
                  temp_row.append(w)
       A2.append(temp_row)
for i in range(len(A1)):
    concatenated_row = A1[i] + A2[i] 
    W2.append(concatenated_row)             
# print('weight matrix for third layer/second hidden layer')    
# for i in W2:
#     print(i)
    
#Bias matrix for third layer/second hidden layer

B2 = []

for l in range(n):
    for p in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if p==0:
                    b = -(d+1) / eps +1
                else:
                    b=(-(d+1) / eps)
                temp_row.append(b)
            B2.append(temp_row)

    
L2 = [] # eta nodes
for i in range(len(W2)):
    L2_i_entry =np.maximum( (np.dot(W2[i], L1)+B2[i]),0)   
    L2.append(L2_i_entry)
    
# print('Eta nodes of third layer/second hidden layer')
# for i in L2:
#     print(i)
##################
#To construct weight matrix for fourth layer/third hidden layer is L2=W2*L1+B2
W3 = []
#for mu nodes     
for i in range(n):  
    for p in range(2):
        temp_row = []
        for l in range(n): #eta nodes 
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
#for gamma nodes     
for i in range(n):  
    for p in range(2):
        temp_row = []
        for l in range(n): #eta nodes 
           for q in range(2):
                w = 0
                if i == l:
                   if q==0:
                       w= -1 / eps
                   else: 
                       w = 1 / eps  
                temp_row.append(w)
        W3.append(temp_row)            
# print('weight matrix for fourth layer/third hidden layer')    
# for i in W3:
#     print(i)
    
#Bias matrix for fourth layer/third hidden layer

B3 = []

# (bias of mu nodes)

for i in range(n):
    for p in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if p==0:
                    b = -e[i]/eps +1
                else:
                    b= -e[i]/eps 
                temp_row.append(b)
            B3.append(temp_row)

# (bias of gamma nodes)

for i in range(n):
    for p in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if p==0:
                    b = e[i]/eps +1
                else:
                    b= e[i]/eps 
                temp_row.append(b)
            B3.append(temp_row)

    
L3 = [] # Mu and Gamma nodes
for i in range(len(W3)):
    L3_i_entry =np.maximum( (np.dot(W3[i], L2)+B3[i]),0)   
    L3.append(L3_i_entry)
    
# print('Mu and Gamma nodes of fourth layer/third hidden layer')
# for i in L3:
#     print(i)    
#To construct weight matrix for fifth layer/fourth hidden layer is L4=W4*L3+B4
W4 = [] 
##
D1=[]
for i in range(n):
    temp_row = []
    for l in range(n):# Mu nodes
        for p in range(2):
           w = 0
           if l==i:
               if p==0:
                   w = -1
               else:
                   w = 1 
           temp_row.append(w)
    D1.append(temp_row)
##
D2=[]
for i in range(n):
    temp_row = []
    for l in range(n):# Gamma nodes
        for p in range(2):
           w = 0
           if l==i:
               if p==0:
                   w = -1
               else:
                   w = 1 
           temp_row.append(w)
    D2.append(temp_row)   
for i in range(len(D1)):
    concatenated_row = D1[i] + D2[i]
    W4.append(concatenated_row)
# print("weight for output Layer")
# print(W4)

#Bias matrix for output layer

B4 = []
for i in range(n):
    temp_row = []
    for l in range (1):
        b = 2
        temp_row.append(b)
    B4.append(temp_row)

Y = [] # Output nodes
for i in range(len(W4)):
    Y_i_entry = np.maximum((np.dot(W4[i], L3) +B4[i]),0)   
    Y.append(Y_i_entry)
    # print('this is index i:', i)
    # print('this is the value Y[i]:', Y_i_entry)
values = [int(array[0]) for array in Y]
print("Output:", values)       
#####################################
