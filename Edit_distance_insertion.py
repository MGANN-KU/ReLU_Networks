# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 09:33:29 2023

@author: Mamoona Ghafoor
"""

import numpy as np

# Insertion
#parameters
eps =  1e-7
C = 1e6
# input
m = 5
d = 3
e =[3, 2, 4, 1]
n = len(e)
#
# First layer is input layer, Given as
x = [4, 1, 4, 3, 2, 5] 
X = x   
print("Input:")
print("e:", e)
print("d:", d)
print("m:", m)
print("x:", X)

#To construct weight matrix for second layer/first hidden layer is L1=W1*X+B1
W1 = []
##
for k in range(1,d+1):  # eta nodes
   for j in range(1,d+1):
      for q in range(2):
         temp_row = []  
         for l in range (1,(2 * d)+1):  
            w = 0
            if k == l and k!=j:
               w = -1 / eps
            if j==l and k!=j: 
               w=1 / eps
            temp_row.append(w)
         W1.append(temp_row)
#print(W1)
##
for k in range(1,d+1):  #(psi^11,psi^12 nodes)
   for j in range(1,d+1):
      for q in range(2):
         temp_row = []  
         for l in range (1,(2 * d)+1):  
            w = 0
            if k == l and k!=j:
               w = -1 / eps
            if j==l and k!=j: 
               w=1 / eps
            temp_row.append(w)
         W1.append(temp_row)
##
for k in range(1,d+1):  #(rho^11,rho^12 nodes)
   for j in range(1,d+1):
      for q in range(2):
         temp_row = []  
         for l in range (1,(2 * d)+1):  
            w = 0
            if k == l and k!=j:
               w = 1 / eps
            if j==l and k!=j: 
               w=-1 / eps
            temp_row.append(w)
         W1.append(temp_row)
#print(W1)
for i in range(1,(2 * d)+1):#(x_{j} nodes as identity map)
   temp_row = []
   for l in range(1,(2 * d)+1):
       w = 0
       if i == l:
           w = 1 
       temp_row.append(w)
   W1.append(temp_row)
##
#print("weight matrix for second layer/first hidden layer")            
#print(W1)  
    
#Bias matrix for second layer/first hidden layer
B1 = []
##
#bias of eta 1 and eta 2 nodes

for k in range(1,d+1):
    for j in range (1, d+1):
        for q in range(2):
          temp_row = []
          for l in range(1):
                b = 0
                if q==0:
                    b = 1
                temp_row.append(b)
          B1.append(temp_row)     
###
# bias of psi 11 and psi 12

for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for l in range(1):
                b = 0
                if q==0:
                    b = 1
                temp_row.append(b)
            B1.append(temp_row)

# bias of rho 21 and rho 22

for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for l in range(1):
                b = 0
                if q==0:
                    b = 1
                temp_row.append(b)
            B1.append(temp_row)
##            
#bias of x_{j} as identity function)

for k in range(1, (2*d)+1):
   temp_row = []
   for j in range(1):
       b = 0
       temp_row.append(b)
   B1.append(temp_row)

# print("Bias matrix for second layer/first hidden layer")
# print(B1)            

L1 = [] # Eta, psi 11 , psi 12 rho 21,rho 22 nodes
for i in range(len(W1)):
    L1_i_entry =np.maximum( (np.dot(W1[i], X)+B1[i]),0)  
    L1.append(L1_i_entry)
# #    print('this is index i:', i)
# #    print('this is the value E[i]:', E_i_entry)
# print('Eta, psi 11 , psi 12 rho 21,rho 22 nodes of second layer/first hidden layer')
# for i in L1:
#     print(i)
#To construct weight matrix for third layer/second hidden layer is L2=W2*L1+B2
W2 = []
##
#varrho nodes and eta^1 and eta^2 nodes)
A1 = []
for j in range(1, d+1):
    temp_row = []
    for k in range(1,d+1):
        for l in range(1,d+1):
           for q in range(2): 
             w = 0
             if j == l:
                if q == 0:
                  w = 1
                else: # q = 1
                  w = -1
             temp_row.append(w)
    A1.append(temp_row)
##
# varrho nodes and psi^11,psi^12 nodes
A2 = []
for j in range(1, d+1):
    temp_row = []
    for k in range(1, d+1):
       for l in range(1,d+1):
          for q in range(2):
             w = 0
             if j == l and k>=j:
                if q == 0:
                  w = -1
                else: # q = 1
                  w = 1
             temp_row.append(w)
    A2.append(temp_row)         
# varrho nodes and rho^11,rho^12 nodes
A3 = []         
for j in range(1, d+1):
    temp_row = []
    for k in range(1, d+1):
       for l in range(1,d+1):
          for q in range(2):
             w = 0
             if j == l and k>=j:
                if q == 0:
                  w = -1
                else: # q = 1
                  w = 1
             temp_row.append(w)
    A3.append(temp_row)
# varrho nodes and x_{j} nodes
A4 = []
for i in range(1, d+1):
    temp_row = []
    for l in range(1,(2 * d)+1):
        w = 0
        temp_row.append(w)
    A4.append(temp_row)               
# Concatenating all four matrices horizontally
#####################
for i in range(len(A1)):
    concatenated_row1 = A1[i] + A2[i] + A3[i] + A4[i]
    W2.append(concatenated_row1)     
#(x_{j} nodes and eta nodes)
A5 = [] 
for l in range(1,(2*d)+1):
   temp_row = []
   for k in range(1,d+1):
       for j in range(1,d+1):
           for q in range(2):
              w = 0
              temp_row.append(w)
   A5.append(temp_row) 
#( x_{j} nodes and psi^11,psi^12 nodes nodes) 
A6 = [] 
for j in range(1,(2*d)+1):
   temp_row = []
   for k in range(1,d+1):
       for l in range(1,d+1):
           for q in range(2):
               w = 0
               temp_row.append(w)
   A6.append(temp_row)
#( x_{j} nodes and rho^11,rho^12 nodes nodes)
A7 = [] 
for j in range(1,(2*d)+1):
   temp_row = []
   for k in range(1,d+1):
       for l in range(1,d+1):
           for q in range(2):
               w = 0
               temp_row.append(w)
   A7.append(temp_row)              
#(x_{j} nodes and x_{j} nodes)               
A8 = [] 
for j in range(1,(2*d)+1):
   temp_row = []
   for k in range(1,(2*d)+1):
       w = 0
       if j==k:
          w=1
       temp_row.append(w)
   A8.append(temp_row)            
## 
for i in range(len(A5)):
    concatenated_row2 = A5[i] + A6[i] + A7[i] + A8[i]
    W2.append(concatenated_row2)            
##           
# print("weight matrix for third layer/second hidden layer")
# print(W2) 

# Bias matrix for third layer/second hidden layer       
B2 = []

for j in range(1, d+1): #(corresponding to varrho nodes)
   temp_row = []
   for l in range(1):
       b = d-j+1
       temp_row.append(b)
   B2.append(temp_row)           
           
for k in range(1, (2*d)+1):#(corresponding to x_{j} nodes)
   temp_row = []
   for j in range(1):
       b = 0
       temp_row.append(b)
   B2.append(temp_row)           
# print('Printing bias  matrix for third layer/second hidden layer') 
# print(B2)
  
L2 = [] # Varrho nodes
for i in range(len(W2)):
    temp_row = []
    L2_i_entry = np.maximum((np.dot(W2[i], L1) +B2[i]),0)   
    L2.append(L2_i_entry)
#     print('this is index i:', i)
#     print('this is the value L2[i]:', L2_i_entry)
# print('Varrho nodes of third layer/second hidden layer')
# for i in L2:
#     print(i) 
###############
#To construct weight matrix for fourth layer/third hidden layer is L3=W3*L2+B3
W3 = []
##
C1 = []
#(psi^21,psi^22 nodes and varrho)
for l in range(1,d+1):  
    for j in range(1,d+1):
        for q in range(2):
            temp_row = []
            for k in range(1,d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            C1.append(temp_row)
C2 = [] 
#(psi^21,psi^22 nodes and x_j)
for l in range(1,d+1):  
    for j in range(1,d+1):
        for q in range(2):
            temp_row = []
            for k in range(1,(2 * d)+1):
                w = 0
                temp_row.append(w)
            C2.append(temp_row) 
## 
for i in range(len(C1)):
    concatenated_row1 = C1[i] + C2[i] 
    W3.append(concatenated_row1)  
#print(W3)    
C3=[]           
#(rho^21,rho^22 nodes and varrho)
for l in range(1,d+1):  
    for j in range(1,d+1):
        for q in range(2):
            temp_row = []
            for k in range(1,d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            C3.append(temp_row)
C4 = [] 
#(rho^21,rho^22 nodes and x_j)
for l in range(1,d+1):  
    for j in range(1,d+1):
        for q in range(2):
            temp_row = []
            for k in range(1,(2 * d)+1):
                w = 0
                temp_row.append(w)
            C4.append(temp_row) 
## 
for i in range(len(C3)):
    concatenated_row2 = C3[i] + C4[i] 
    W3.append(concatenated_row2)             
##
C5=[]           
#(x_j nodes and varrho) 
for k in range(1,(2 * d)+1):
       temp_row = []
       for j in range(1,d+1):
           w = 0
           temp_row.append(w)
       C5.append(temp_row)
#print(C5)       
C6 = [] 
#(x_j nodes and x_j nodes)
for l in range(1,(2 * d)+1):  
    temp_row = []
    for k in range(1,(2 * d)+1):
        w = 0
        if l==k:
            w=1
        temp_row.append(w)
    C6.append(temp_row)     
## 
for i in range(len(C5)):
    concatenated_row3 = C5[i] + C6[i] 
    W3.append(concatenated_row3) 
#print(W3)    
#Bias matrix for fourth layer/third hidden layer

B3 = []
# (bias of psi^21,psi^22 nodes)

for l in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if q==0:
                    b = ((1 -l) / eps)+1
                else:
                    b=(1 -l) / eps
                temp_row.append(b)
            B3.append(temp_row)

# (bias of rho^21,rho^22 nodes)

for l in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if q==0:
                    b = ((l -1) / eps)+1
                else:
                    b=(l -1) / eps
                temp_row.append(b)
            B3.append(temp_row)           

#(bias of x_{j} as identity function)

for k in range(1, (2*d)+1):
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B3.append(temp_row)

# print("Bias matrix for fourth layer/third hidden layer")
# print(B3)            

L3 = [] # psi 21, 22 nodes and rho 21, 22
for i in range(len(W3)):
    L3_i_entry =np.maximum( (np.dot(W3[i], L2)+B3[i]),0)  
    L3.append(L3_i_entry)
#    print('this is index i:', i)
#    print('this is the value L3[i]:', L3_i_entry)
# print('Psi 21, 22 nodes and rho 21, 22 nodes of fourth layer/third hidden layer')
# for i in L3:
#     print(i) 
############
#To construct weight matrix for fifth layer/fourth hidden layer is L4=W4*L3+B4
W4 = []
##
D1 = []
#(chi_lj nodes and psi^21,psi^22 nodes)
for l in range(1,d+1):  
    for j in range(1, d+1):
       temp_row = []
       for m in range(1,d+1):  
          for k in range(1,d+1):
             for q in range(2):
                w = 0
                if l == m and j==k:
                    if q==0:
                        w=C
                    else:
                        w=-C
                temp_row.append(w)
       D1.append(temp_row)
#print(D1)    
D2 = []
#(chi_lj nodes and rho^21,rho^22 nodes)
for l in range(1,d+1):  
    for j in range(1, d+1):
       temp_row = []
       for m in range(1,d+1):  
          for k in range(1,d+1):
             for q in range(2):
                w = 0
                if l == m and j==k:
                    if q==0:
                        w=C
                    else:
                        w=-C
                temp_row.append(w)
       D2.append(temp_row) 
#print(D2)        
D3 = []
#(chi_lj nodes and x_j nodes)
for l in range(1,d+1): 
    for j in range(1, d+1):
      temp_row = []
      for k in range(1,d+1):  
         w = 0
         if j==k:
             w=1
         temp_row.append(w)
      D3.append(temp_row)
#print(D3)       
D4 = []
#(chi_lj nodes and x_j+d nodes)
for l in range(1,d+1): 
    for j in range(1, d+1):
       temp_row = []
       for k in range(d+1,2*d+1):  
          w = 0
          temp_row.append(w)
       D4.append(temp_row)  
#print(D4)             
##           
for i in range(len(D1)):
    concatenated_row1 = D1[i] + D2[i] + D3[i]+ D4[i]
    W4.append(concatenated_row1) 
#print(W4)     
##
D5 = []
#(chi_l(j+d) nodes and psi^21,psi^22 nodes)
for l in range(1,d+1):  
   for j in range(d+1,2*d+1): 
     temp_row = []
     for m in range(1,d+1):  
        for k in range(1,d+1):
            for q in range(2):
                w = 0
                if l == m and j==d+k:
                    if q==0:
                        w=C
                    else:
                        w=-C
                temp_row.append(w)
     D5.append(temp_row)
#print(D5)      
D6 = []
#(chi_l(j+d) nodes and rho^21,rho^22 nodes)
for l in range(1,d+1):  
   for j in range(d+1,2*d+1): 
     temp_row = []
     for m in range(1,d+1):  
        for k in range(1,d+1):
            for q in range(2):
                w = 0
                if l == m and j==d+k:
                    if q==0:
                        w=C
                    else:
                        w=-C
                temp_row.append(w)
     D6.append(temp_row)
#print(D6)      
D7 = []
#(chi_l(d+j) nodes and x'_j nodes)
for l in range(1,d+1):  
   for j in range(d+1,2*d+1): 
      temp_row = []
      for k in range(1,d+1):  
         w = 0
         temp_row.append(w)
      D7.append(temp_row)  
D8 = []
#(chi_l(d+j) nodes and x'_j+d nodes)
for l in range(1,d+1):  
   for j in range(d+1,2*d+1): 
      temp_row = []
      for k in range(d+1,2*d+1):   
         w = 0
         if j==k:
             w=1
         temp_row.append(w)
      D8.append(temp_row) 
#print(D8)               
##           
for i in range(len(D5)):
    concatenated_row2 = D5[i] + D6[i] + D7[i]+ D8[i]
    W4.append(concatenated_row2) 
#print('weight matrix for fifth layer/fourth hidden layer,W4')    
#print(W4)
     
#Bias matrix for fifth layer/fourth hidden layer

B4 = []
# (bias of chi_lj nodes)

for l in range(1,d+1):  
   for j in range(1,d+1): 
    temp_row = []
    for m in range(1):
        b = -2*C
        temp_row.append(b)
    B4.append(temp_row)

# (bias of Chi_j+d nodes)

for l in range(1,d+1):  
   for j in range(d+1,2*d+1): 
    temp_row = []
    for m in range(1):
        b = -2*C
        temp_row.append(b)
    B4.append(temp_row)

# print("Bias matrix for fifth layer/fourth hidden layer")
# print(B4)            

L4 = [] # Chi nodes
for i in range(len(W4)):
    L4_i_entry =np.maximum( (np.dot(W4[i], L3)+B4[i]),0)  
    L4.append(L4_i_entry)
#    print('this is index i:', i)
#    print('this is the value L4[i]:', L4_i_entry)
# print('Chi nodes of fifth layer/fourth hidden layer')
# for i in L4:
#     print(i)   

#To construct weight matrix for Sixth layer/fifth hidden layer is L5=W5*L4+B5
W5 = []
##
E1 = []
#(x'_j nodes and chi_lj nodes)
for l in range(1,d+1):  
    temp_row = []
    for k in range(1,d+1):  
        for j in range(1, d+1):
            w = 0
            if l ==k:
                w=1
            temp_row.append(w)
    E1.append(temp_row)
#print(E1)    
E2 = []
#(x'_l nodes and chi_l(j+d) nodes)
for l in range(1,d+1):  
    temp_row = []
    for k in range(1,d+1):  
        for j in range(1, d+1):
            w = 0
            temp_row.append(w)
    E2.append(temp_row)
#print(E2)               
##           
for i in range(len(E1)):
    concatenated_row1 = E1[i] + E2[i] 
    W5.append(concatenated_row1) 
#print(W5)     
##
E3 = []
#(x'_(l+d) nodes and chi_l(j) nodes) 
for l in range(d+1,2*d+1): 
    temp_row = []
    for m in range(1,d+1):  
        for k in range(1,d+1):
            w = 0
            temp_row.append(w)
    E3.append(temp_row)
E4 = []
#(x'_(l+d) nodes and chi_l(j+d) nodes) 
for j in range(d+1,2*d+1): 
    temp_row = []
    for m in range(1,d+1):  
        for k in range(d+1,2*d+1): 
                w = 0
                if j==m+d:
                    w=1
                temp_row.append(w)
    E4.append(temp_row)            
##           
for i in range(len(E3)):
    concatenated_row2 = E3[i] + E4[i]
    W5.append(concatenated_row2) 
#print('weight matrix for Sixth layer/fifth hidden layer')    
#print(W5)
     
#Bias matrix for Sixth layer/fifth hidden layer
B5 = []
# (bias of chi_lj nodes)

for l in range(1,d+1):   
    temp_row = []
    for m in range(1):
                b = 0
                temp_row.append(b)
    B5.append(temp_row)

# (bias of Chi_j+d nodes)

for l in range(1,d+1):   
    temp_row = []
    for m in range(1):
                b = 0
                temp_row.append(b)
    B5.append(temp_row)

# print("Bias matrix for Sixth layer/fifth hidden layer")
# print(B5)            

L5 = [] # x' nodes
for i in range(len(W5)):
    L5_i_entry =np.maximum( (np.dot(W5[i], L4)+B5[i]),0)  
    L5.append(L5_i_entry)
#    print('this is index i:', i)
#    print('this is the value L5[i]:', L5_i_entry)
# print('x prime nodes of Sixth layer/fifth hidden layer')
# for i in L5:
#     print(i) 
######################################
#To construct weight matrix for Seventh layer/sixth hidden layer is L6=W6*L5+B6
W6 = []
#(alpha^1,alpha^2 nodes)
for l in range(1,n+2):  
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,(2 * d)+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            W6.append(temp_row)
#(beta^1,beta^2 nodes)
for l in range(1,n+2):  
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,(2 * d)+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            W6.append(temp_row)
# ##
for k in range(1,d+1):  # gamma nodes
    temp_row = []  
    for j in range (1,(2 * d)+1):  
        w = 0
        if k == j:
            w = 1
        temp_row.append(w)
    W6.append(temp_row)
##(x'_{d+l} nodes as identity map)
for i in range(d+1,(2 * d)+1):
    temp_row = []
    for l in range(1,(2 * d)+1):
        w = 0
        if i == l:
            w = 1 
        temp_row.append(w)
    W6.append(temp_row)
# ##
# #print("weight matrix for Seventh layer/sixth hidden layer")            
# #print(W6)  
    
# #Bias matrix for Seventh layer/sixth hidden layer

B6 = []
# #(bias of alpha for k in range(d))

for i in range(1,n+2):
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if q==0:
                    b = -(i / eps)+1
                else:
                    b=-i / eps
                temp_row.append(b)
            B6.append(temp_row)

#(bias of beta for k in range(d))

for l in range(1,n+2):
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if q==0:
                    b = l / eps+1
                else:
                    b=l / eps
                temp_row.append(b)
            B6.append(temp_row)
##
#(gamma nodes)

for k in range(1,d+1):
    temp_row = []
    for j in range(1):
        b = k-1
        temp_row.append(b)
    B6.append(temp_row)            

#(bias of x'_{l+d} as identity function)

for k in range(d+1, (2*d)+1):
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B6.append(temp_row)

# print("Bias matrix for Seventh layer/sixth hidden layer")
# print(B6)            
 

L6 = [] # alpha and beta and gamma nodes
for i in range(len(W6)):
    L6_i_entry =np.maximum( (np.dot(W6[i], L5)+B6[i]),0)  
    L6.append(L6_i_entry)
#    print('this is index i:', i)
#    print('this is the value L6[i]:', L6_i_entry)
# print('Printing alpha, beta and gamma nodes of Seventh layer/sixth hidden layer')
# for i in L6:
#     print(i)

#To construct weight matrix for eighth layer/seventh hidden layer is L7=W7*L6+B7
W7 = []
# tau nodes and alpha^1,alpha^2 nodes

F1 = []
for i in range(1, n+2):
    temp_row = []
    for l in range(1, n+2):
        for k in range(1,d+1):
          for q in range(2):
              w = 0
              if i == l:
                if q == 0:
                  w = 1
                else: # q = 1
                  w = -1
              temp_row.append(w)
    F1.append(temp_row)
#print(F1)         
# tau nodes and beta^1,beta^2 nodes
F2 = []         
for i in range(1, n+2):
    temp_row = []
    for l in range(1, n+2):
        for k in range(1,d+1):
          for q in range(2):
              w = 0
              if i == l:
                if q == 0:
                  w = 1
                else: # q = 1
                  w = -1
              temp_row.append(w)
    F2.append(temp_row)
#print(F2)
#(tau and gamma nodes)
F3 = []
for i in range(1, n+2):
    temp_row = []
    for j in range(1,d+1):
        w = 0
        temp_row.append(w)
    F3.append(temp_row)
##
# tau nodes and x'_{l+d} nodes
F4 = []
for i in range(1, n+2):
    temp_row = []
    for l in range(d+1,(2 * d)+1):
        w = 0
        temp_row.append(w)
    F4.append(temp_row)     
#print(F4)          
# Concatenating all four matrices horizontally

for i in range(len(F1)):
    concatenated_row1 = F1[i] + F2[i] + F3[i] + F4[i]
    W7.append(concatenated_row1)
   
F5 = [] #(mu 11, mu 12 nodes and alpha nodes)   
for l in range(1, n+2):
    for k in range(1,d+1):
        for p in range(2):
            temp_row = []
            for i in range(1, n+2):
                for j in range(1,d+1):
                    for q in range(2):
                        w = 0
                        temp_row.append(w)
            F5.append(temp_row)
##            
F6 = [] #(mu 11, mu 12 and beta nodes)   
for l in range(1, n+2):
    for k in range(1,d+1):
        for p in range(2):
            temp_row = []
            for i in range(1, n+2):
                for j in range(1,d+1):
                    for q in range(2):
                        w = 0
                        temp_row.append(w)
            F6.append(temp_row)  
#print(F6)
F7 = []   #(mu 11, mu 12 and gamma nodes) 
for l in range(1, n+2):
    for k in range(1,d+1):
        for p in range(2):
            temp_row = []
            for j in range(1,d+1):
                w = 0
                if j==k:
                  w= 1 / eps
                temp_row.append(w)
            F7.append(temp_row)
#print(F7)
##            
F8 = [] #(mu 11, mu 12 and x'_{l+d} nodes)   
for l in range(1, n+2):
    for k in range(1,d+1):
        for p in range(2):
            temp_row = []
            for j in range(d+1,(2*d)+1):
                w = 0
                temp_row.append(w)
            F8.append(temp_row)             
#print(F8) 

for i in range(len(F5)):
    concatenated_row2 = F5[i] + F6[i] + F7[i] + F8[i]
    W7.append(concatenated_row2) 

F9 = []   #(lambda 11, lambda 12 and alpha nodes) 
for l in range(1, n+2):
    for k in range(1,d+1):
        for p in range(2):
            temp_row = []
            for i in range(1, n+2):
                for j in range(1,d+1):
                    for q in range(2):
                        w = 0
                        temp_row.append(w)
            F9.append(temp_row)
##            
F10 = [] #(lambda 11, lambda 12 and beta nodes)   
for l in range(1, n+2):
    for k in range(1,d+1):
        for p in range(2):
            temp_row = []
            for i in range(1, n+2):
                for j in range(1,d+1):
                    for q in range(2):
                        w = 0
                        temp_row.append(w)
            F10.append(temp_row)  
#print(F10)
F11 = []   #(lambda 11, lambda 12 and gamma nodes) 
for l in range(1, n+2):
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,d+1):
                w = 0
                if j==k:
                  w= -1 / eps
                temp_row.append(w)
            F11.append(temp_row)
##            
F12 = [] #(lambda 11, lambda 12 and x'_{l+d} nodes)   
for l in range(1, n+2):
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(d+1,(2*d)+1):
                w = 0
                temp_row.append(w)
            F12.append(temp_row)  
#print(F12)

for i in range(len(F9)):
    concatenated_row3 = F9[i] + F10[i] + F11[i] + F12[i]
    W7.append(concatenated_row3)
##
F13 = [] 
for k in range(d+1,(2*d)+1):#( x'_{l+d} nodes and alpha nodes) 
    temp_row = []
    for i in range(1,n+2):
        for j in range(1,d+1):
            for p in range(2):
                w = 0
                temp_row.append(w)
    F13.append(temp_row)
#
F14 = [] 
for k in range(d+1,(2*d)+1):#( x'_{l+d} nodes and beta nodes)
    temp_row = []
    for i in range(1,n+2):
        for j in range(1,d+1):
            for p in range(2):
                w = 0
                temp_row.append(w)
    F14.append(temp_row)  
##
F15 = [] 
for l in range(d+1,(2*d)+1):#(x'_{l+d} nodes and gamma nodes)
    temp_row = []
    for j in range(1,d+1):
        w = 0
        temp_row.append(w)
    F15.append(temp_row) 
##
F16 = [] #
for l in range(d+1,(2*d)+1):#(x'_{l+d} nodes and x'_{l+d} nodes) 
    temp_row = []
    for i in range(d+1,(2*d)+1):
        w = 0
        if l==i:
          w=1
        temp_row.append(w)
    F16.append(temp_row)            
## 
for i in range(len(F13)):
    concatenated_row4 = F13[i] + F14[i] + F15[i] + F16[i]
    W7.append(concatenated_row4)            
##           
# print("weight matrix for eighth layer/seventh hidden layer")
# print(W7) 

# Bias matrix for eighth layer/seventh hidden layer       
B7 = []
for l in range(1, n+2):#(corresponding to tau nodes)
    temp_row = []
    for k in range(1):
        b = (-d)
        temp_row.append(b)
    B7.append(temp_row)

for i in range(1, n+2): #(corresponding to mu 11 and mu 12 nodes)
    for j in range(1,d+1):
        for q in range(2):
            temp_row = []
            for l in range(1):
                b = 0
                if q==0:
                    b= -(i+j-1)/eps+1
                else:
                    b= -(i+j-1)/eps
                temp_row.append(b)
            B7.append(temp_row)
for i in range(1, n+2): #(corresponding to lambda 11, lambda 12 nodes)
    for j in range(1,d+1):
        for q in range(2):
            temp_row = []
            for l in range(1):
                b = 0
                if q==0:
                    b=(i+j-1)/eps+1
                else:
                    b= (i+j-1)/eps
                temp_row.append(b)
            B7.append(temp_row)            
            
for k in range(d+1, (2*d)+1):#(corresponding to x'_{l+d} nodes)
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B7.append(temp_row)           
# print('Printing bias for eighth layer/seventh hidden layer') 
# print(B7)
  
L7 = [] # tau , mu and lambda nodes
for i in range(len(W7)):
    L7_i_entry = np.maximum((np.dot(W7[i], L6) +B7[i]),0)   
    L7.append(L7_i_entry)
    
# print('Printing tau,mu 11, mu 12 and lambda 11, lambda 12 nodes of eighth layer/seventh hidden layer')
# for i in L7:
#     print(i)      

#To construct weight matrix for ninth layer/eighth hidden layer L8=W8*L7+B8
W8 = []
#(tau' nodes and tau nodes)
G1 = []  
for i in range(1, n+1):
    temp_row = []
    for l in range(1, n+2):
        w = 0
        if l <= i:
          w = 1
        temp_row.append(w)
    G1.append(temp_row)    
#print(G1) 
#(tau' nodes and mu nodes) 
G2 = []    
for i in range(1, n+1):
    temp_row = []
    for l in range(1,n+2):
        for d in range (1, d+1):
            for q in range(2):
              w = 0
              temp_row.append(w)
    G2.append(temp_row)            
#print(G2) 
# (tau' nodes and lambda nodes)    
G3 = []    
for i in range(1, n+1):
    temp_row = []
    for l in range(1,n+2):
        for d in range (1, d+1):
            for q in range(2):
              w = 0
              temp_row.append(w)
    G3.append(temp_row)             
#print(G3)
G4 = [] # (tau' nodes and x'_{l+d} nodes)    
for i in range(1, n+1):
    temp_row = []
    for k in range(d+1, (2*d)+1):
        w = 0
        temp_row.append(w)
    G4.append(temp_row) 
###    
for i in range(len(G1)):
    concatenated_row = G1[i] + G2[i] + G3[i] + G4[i]
    W8.append(concatenated_row)
#print(W8) 

# (omega nodes and tau nodes)   
G5 = []  
for i in range(1, n+2):
    for q in range(1,d+1):
          temp_row = []
          for l in range(1, n+2):
              w = 0
              temp_row.append(w)
          G5.append(temp_row)   
#print(G5) 
G6 = []  # (omega nodes and mu 11, mu 12 nodes) 
for i in range(1, n+2):
    for j in range(1,d+1):
        temp_row = []
        for l in range(1, n+2):
            for k in range (1, d+1):
                for q in range(2):
                  w = 0
                  if i == l and j==k:
                      if q == 0:
                          w = C
                      else: # q = 1
                          w = - (C)  
                  temp_row.append(w)
        G6.append(temp_row)   
#print(G6)
G7 = []  # (omega nodes and lambda 11, lambda 12 nodes) 
for i in range(1, n+2):
    for j in range(1,d+1):
        temp_row = []
        for l in range(1, n+2):
            for k in range (1, d+1):
                for q in range(2):
                  w = 0
                  if i == l and j==k:
                      if q == 0:
                          w = C
                      else: # q = 1
                          w = -( C ) 
                  temp_row.append(w)
        G7.append(temp_row)    
#print(G7)
G8 = []  # (omega nodes and x'_{l+d} nodes) 
for i in range(1, n+2):
    for j in range(1,d+1):
        temp_row = []
        for k in range(d+1, (2*d)+1):
            w = 0
            if j+d==k:
              w = 1 
            temp_row.append(w)
        G8.append(temp_row)   
#print(G8)   
for i in range(len(G5)):
    concatenated_row = G5[i] + G6[i] + G7[i] + G8[i] 
    W8.append(concatenated_row)
# print('Printing weight matrix for ninth layer/eighth hidden layer, W8')    
# print(W8) 

# Bias matrix for ninth layer/eighth hidden layer       
B8 = [] 
for i in range(1, n+1):#(corresponding to tau' nodes)
    temp_row = []
    for l in range(1):
        w = i
        temp_row.append(w)
    B8.append(temp_row)

for i in range(1, n+2):#(corresponding to omega nodes)
    for j in range(1,d+1):
        temp_row = []
        for l in range(1):
            w = -2*C
            temp_row.append(w)
        B8.append(temp_row) 
# print('Printing Bias matrix for ninth layer/eighth hidden layer, B8')    
# print(B8) 

L8 = [] # Tau prime and omega nodes
for i in range(len(W8)):
    L8_i_entry =  np.maximum((np.dot(W8[i], L7) +B8[i]),0)   
    L8.append(L8_i_entry)
#print('Printing Tau prime and omega nodes of ninth layer/eighth hidden layer')
#for i in L8:
#    print(i) 
##
#To construct weight matrix for tenth layer/ninth hidden layer L9=W9*L8+B9
W9 = []

# (mu 21 and mu 22 nodes and tau' nodes )  
H1 = []  
for l in range(1, n+1):
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+1):
                w = 0
                if l==i:
                    w=1/eps
                temp_row.append(w)
            H1.append(temp_row)   
#print(H1)  
# (mu 21 and mu 22 nodes and omega nodes )  
H2 = []  
for l in range(1, n+1):
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+2):
                for k in range (1, d+1):
                  w = 0
                  temp_row.append(w)
            H2.append(temp_row)   
#print(H2) 
for i in range(len(H1)):
    concatenated_row1 = H1[i] + H2[i] 
    W9.append(concatenated_row1)  
#print(W9)

# (lambda 21, lambda 22 nodes and tau' nodes )  
H3 = []  
for l in range(1, n+1):
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+1):
                w = 0
                if l==i:
                    w=-1/eps
                temp_row.append(w)
            H3.append(temp_row)   
#print(H3)  
# (lambda 21 , lambda 22 nodes and omega nodes )  
H4 = []  
for l in range(1, n+1):
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+2):
                for k in range (1, d+1):
                      w = 0
                      temp_row.append(w)
            H4.append(temp_row)   
#print(H4) 
for i in range(len(H3)):
    concatenated_row2 = H3[i] + H4[i] 
    W9.append(concatenated_row2) 
##
H5 = [] # (zeta nodes and tau' nodes ) 
for h in range(1, n+d+1):
  temp_row = []
  for i in range(1, n+1):
      w = 0
      temp_row.append(w)
  H5.append(temp_row)  
  
H6 = [] # (zeta nodes and omega nodes ) 
for h in range(1, n+d+1):
    temp_row = []
    for i in range(1, n+2):
        for j in range (1, d+1):
          w = 0
          if h==i+j-1:
              w = 1
          temp_row.append(w)
    H6.append(temp_row)
#####          
for i in range(len(H5)):
      concatenated_row3 = H5[i] + H6[i] 
      W9.append(concatenated_row3)     
#print('Printing weight matrix for tenth layer/ninth hidden layer')     
#print(W9) 

# Bias matrix for tenth layer/ninth hidden layer       
B9 = [] 

for i in range(1, n+1):#(corresponding to mu 21 and mu 22 nodes)
    for j in range(1, d+2):
        for q in range(2):
            temp_row = []
            for l in range(1):
                w = 0
                if q==0:
                    w=-(i+j-1)/eps +1
                else: 
                    w=-(i+j-1)/eps
                temp_row.append(w)
            B9.append(temp_row) 
for i in range(1, n+1):#(corresponding to lambda 21 and lambda 22 nodes )
    for j in range(1, d+2):
        for q in range(2):
            temp_row = []
            for l in range(1):
                w = 0
                if q==0:
                    w=(i+j-1)/eps +1
                else: 
                    w=(i+j-1)/eps
                temp_row.append(w)
            B9.append(temp_row)  
 
for h in range(1, n+d+1):#(corresponding to zeta nodes)
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B9.append(temp_row)            
#print('Printing Bias matrix for nineth hidden layer')               
#print(B9)
      
L9 = [] # mu 21 , mu 22,lambda 21 , lambda 22 and zeta nodes
for i in range(len(W9)):
    L9_i_entry = np.maximum((np.dot(W9[i], L8) +B9[i]),0)   
    L9.append(L9_i_entry)
# print('Printing mu 21, mu 22, lambda 21, lambda 22 and zeta nodes of tenth layer/ninth hidden layer')
# for i in L9:
#     print(i) 

#To construct weight matrix for eleventh layer/tenth hidden layer L10=W10*L9+B10.   
W10 = [] 
 
I1 = [] 
for i in range(1, n+1): #(corresponding to omega' and mu nodes)
    for j in range(1, d+2):  
      temp_row = []  
      for l in range(1, n+1):
          for k in range(1, d+2):
            for q in range(2):
                w = 0    
                if i == l and j==k:
                    if q==0:
                        w=C
                    else:       
                          w =-C
                temp_row.append(w)
      I1.append(temp_row)
#print(I1)            
I2 = [] 
for i in range(1, n+1): #(corresponding to omega' and lambda nodes)
    for j in range(1, d+2):  
      temp_row = []  
      for l in range(1, n+1):
          for k in range(1, d+2):
            for q in range(2):
                w = 0    
                if i == l and j==k:
                    if q==0:
                        w=C
                    else:       
                        w =-C
                temp_row.append(w)
      I2.append(temp_row)
#print(I2)
I3 = [] 
for i in range(1, n+1): #(corresponding to omaga' and zeta nodes)
    for j in range(1, d+2):
      temp_row = []  
      for h in range(1, n+d+1):
          w = 0
          temp_row.append(w)
      I3.append(temp_row)
#print(I3)
for i in range(len(I1)):
    concatenated_row1 = I1[i] + I2[i] + I3[i]
    W10.append(concatenated_row1) 
#
I4 = [] 
for h in range(1, n+d+1): #(corresponding to zeta and mu nodes)
    temp_row = []  
    for i in range(1, n+1):
        for j in range(1, d+2):
            for q in range(2):
                w = 0    
                temp_row.append(w)
    I4.append(temp_row)
#print(I4)            
I5 = [] 
for h in range(1, n+d+1): #(corresponding to zeta and lambda nodes)
    temp_row = []  
    for i in range(1, n+1):
        for j in range(1, d+2):
            for q in range(2):
                w = 0    
                temp_row.append(w)
    I5.append(temp_row)
#print(I5)
I6 = [] 
for h in range(1, n+d+1): #(corresponding to zeta and zeta' nodes)
    temp_row = []  
    for p in range(1, n+d+1):
        w = 0 
        if h==p:
            w=1
        temp_row.append(w)
    I6.append(temp_row)
#print(I6)
for i in range(len(I4)):
    concatenated_row2 = I4[i] + I5[i] + I6[i]
    W10.append(concatenated_row2)
#print('Printing weight matrix for eleventh layer/tenth hidden layer')     
#print(W10)     

# # Bias matrix for eleventh layer/tenth hidden layer       
B10 = [] 
for i in range(1, n+1):#(corresponding to omega nodes)
    for j in range (1, d+2):
      temp_row = []
      for l in range(1):
          w=e[i-1]-2*C
          temp_row.append(w)
      B10.append(temp_row) 

for i in range(1, n+d+1):#(corresponding to zeta nodes)
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B10.append(temp_row)
   
#print('Printing Bias matrix for eleventh layer/tenth hidden layer')              
#print(B10)
      
L10 = [] # omega' and zeta nodes
for i in range(len(W10)):
    L10_i_entry = np.maximum((np.dot(W10[i], L9) +B10[i]),0)   
    L10.append(L10_i_entry)
#print('omega prime and zeta nodes of eleventh layer/tenth hidden layer')
#print('this is index i:', i)
#for i in L10:
#    print(i)  
# ##   
#To construct weight matrix for twelveth layer/eleventh hidden layer L11=W11*L10+B11.   
W11 = [] 

J1 = [] 
for h in range(1, n+d+1): #(corresponding to zeta' and omega' nodes)
    temp_row = []  
    for i in range(1, n+1):
        for j in range(1, d+2):
          w = 0 
          if h==i+j-1:
            w=1
          temp_row.append(w)
    J1.append(temp_row)
##
J2 = [] 
for h in range(1, n+d+1): #(corresponding to zeta' and zeta nodes)
    temp_row = []  
    for p in range(1, n+d+1):
        w = 0
        temp_row.append(w)
    J2.append(temp_row) 
## 
for i in range(len(J1)):
    concatenated_row1 = J1[i] + J2[i]
    W11.append(concatenated_row1)    
###
J3 = [] 
for h in range(1, n+d+1): #(corresponding to zeta and omega' nodes)
    temp_row = []  
    for i in range(1, n+1):
        for j in range(1, d+2):
          w = 0 
          temp_row.append(w)
    J3.append(temp_row)
##
J4 = [] 
for h in range(1, n+d+1): #(corresponding to zeta' and zeta nodes)
    temp_row = []  
    for p in range(1, n+d+1):
        w = 0
        if h==p:
            w=1
        temp_row.append(w)
    J4.append(temp_row)
#print(J4)    
## 
for i in range(len(J3)):
    concatenated_row2 = J3[i] + J4[i]
    W11.append(concatenated_row2) 
#print('Printing weight matrix for twelveth layer/eleventh hidden layer')     
#print(W11)    

#Bias matrix for twelveth layer/eleventh hidden layer      
B11 = [] 
for h in range(1, n+d+1):#(corresponding to zeta' nodes)
    temp_row = []
    for l in range(1):
      w=0
      temp_row.append(w)
    B11.append(temp_row) 

for i in range(1, n+d+1):#(corresponding to zeta nodes)
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B11.append(temp_row)
#print('Printing Bias matrix for twelveth layer/eleventh hidden layer')               
#print(B11) 
L11 = [] # zeta prime nodes
for i in range(len(W11)):
    L11_i_entry = np.maximum((np.dot(W11[i], L10) +B11[i]),0)   
    L11.append(L11_i_entry)
#print('zeta prime and zeta nodes of twelveth layer/eleventh hidden layer')
#print('this is index i:', i)
#for i in L11:
#    print(i) 

###
#To construct weight matrix for thirteenth layer/twelvth hidden layer L12=W12*L11+B12
W12=[]        
K1 = [] #output layer     
for i in range(1,n+d+1):  
    temp_row = []
    for l in range(1,n+d+1):
        w = 0
        if i==l:
            w = 1
        temp_row.append(w)
    K1.append(temp_row) 
# # 
K2 = []     
for i in range(1,n+d+1):  
    temp_row = []
    for l in range(1,n+d+1):
        w = 0
        if i==l:
            w = 1
        temp_row.append(w)
    K2.append(temp_row) 
#print(F12)
for i in range(len(K1)):
    concatenated_row1 = K1[i] + K2[i] 
    W12.append(concatenated_row1)
    
# # Bias matrix for thirteenth layer/twelvth hidden layer   
B12 = [] 

for h in range(1, n+d+1):  #(Zeta nodes)
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B12.append(temp_row)       
            
# print('Printing Bias matrix for output layer')               
# print(B12)
      
Y = [] # 
for i in range(len(W12)):
    Y_i_entry =np.maximum((np.dot(W12[i], L11) +B12[i]), 0)
    Y.append(Y_i_entry) 
    
values = [int(array[0]) for array in Y]    


print("Output:", values) 
