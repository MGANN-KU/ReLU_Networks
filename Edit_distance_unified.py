# -*- coding: utf-8 -*-
"""
Created on Mon jan 1 13:12:44 2024

@author: Mamoona Ghafoor
"""

import numpy as np

######## 
#parameters   
eps = 1e-7
C = 1e6 
B = 1e4
# B>>n and B>>C

#input
m = 7
d = 3
e = [4, 1, 3, 2, 5]
Delta = 0.01
n = len(e)

# First layer is input layer, Given as
x = [0.03, 0, 0.03, 0.27, 0, 0.6, 0, 0.55, 0.55, 0, 0.25, 0.9, 0, 0.7, 0.24]
X = x
print("Input:")
print("e:", e)
print("d:", d)
print("m:", m)
print("Delta:", Delta)
print("x:", X)

# B>>n and B>>C
# for x_i in X:    
#     if math.isinteger((x_i/Delta)):
#         print("Integer", x_i/Delta)
#     else: 
#         print("Error with input x")
#         #exit(1)
 

###
#first second layer is L1=W1*X+B1
W1 = []
# for gamma 11,12 in range 1<=j<=d
for j in range(1,d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)
# for gamma 11,12 in range d+1<=j<=2d
for j in range(d+1,2*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)            
# for gamma 11,12 in range 2d+1<=j<=4d
for j in range(2*d+1,4*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)
# for gamma 11,12 in range 4d+1<=j<=5d
for j in range(4*d+1,5*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)            
# print(W1)
################
# for gamma 21,22 in range 1<=j<=d
for j in range(1,d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)
# for gamma 21,22 in range d+1<=j<=2d
for j in range(d+1,2*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)            
# for gamma 21,22 in range 2d+1<=j<=4d
for j in range(2*d+1,4*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)
# for gamma 21,22 in range 4d+1<=j<=5d
for j in range(4*d+1,5*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)            
# print(W1)
################
# for alpha 11,12 in range 1<=j<=d
for j in range(1,d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)
# for alpha 11,12 in range d+1<=j<=2d
for j in range(d+1,2*d+1): 
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)            
# for alpha 11,12 in range 2d+1<=j<=4d
for k in range(2*d+1,4*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for j in range(1,5*d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)
# for alpha 11,12 in range 4d+1<=j<=5d
for k in range(4*d+1,5*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for j in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)            
######### 
################
# for beta 11,12 in range 1<=j<=d
for j in range(1,d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)
# for beta 11,12 in range d+1<=j<=2d
for j in range(d+1,2*d+1): 
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)            
# for beta 11,12 in range 2d+1<=j<=4d
for k in range(2*d+1,4*d+1):  
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for j in range(1,5*d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)
# for beta 11,12 in range 4d+1<=j<=5d
for k in range(4*d+1,5*d+1):  #(beta nodes)
    for i in range(0,n+2):
        for q in range(2):
            temp_row = []
            for j in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)             
#print(W1)####################################
# for omega 11,12 in range 1<=j<=d
for j in range(1,d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)
# for omega 11,12 in range d+1<=j<=2d
for j in range(d+1,2*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)            
# for omega 11,12 in range 2d+1<=j<=4d
for j in range(2*d+1,4*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)
# for omega 11,12 in range 4d+1<=j<=5d
for j in range(4*d+1,5*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)            
# print(W1)
################
# for omega 21,22 in range 1<=j<=d
for j in range(1,d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)
# for omega 21,22 in range d+1<=j<=2d
for j in range(d+1,2*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)            
# for omega 21,22 in range 2d+1<=j<=4d
for j in range(2*d+1,4*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)
# for omega 21,22 in range 4d+1<=j<=5d
for j in range(4*d+1,5*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)            
# print(W1)
################
# for alpha 21,22 in range 1<=j<=d
for j in range(1,d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)
# for alpha 21,22 in range d+1<=j<=2d
for j in range(d+1,2*d+1): 
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                if k == j and l!=1:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)            
# for alpha 21,22 in range 2d+1<=j<=4d
for k in range(2*d+1,4*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for j in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)
# for alpha 21,22 in range 4d+1<=j<=5d
for k in range(4*d+1,5*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for j in range(1,5*d+1):
                w = 0
                if k == j and l!=1:
                    w = 1 / eps
                temp_row.append(w)
            W1.append(temp_row)            
######### 
# for beta 21,22 in range 1<=j<=d
for j in range(1,d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)
# for beta 21,22 in range d+1<=j<=2d
for j in range(d+1,2*d+1): 
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for k in range(1,5*d+1):
                w = 0 
                if k == j and l!=1:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)            
# for beta 21,22 in range 2d+1<=j<=4d
for k in range(2*d+1,4*d+1):  
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for j in range(1,5*d+1):
                w = 0
                temp_row.append(w)
            W1.append(temp_row)
# for beta 21,22 in range 4d+1<=j<=5d
for k in range(4*d+1,5*d+1):  #(beta nodes)
    for l in range(1,m+1):
        for q in range(2):
            temp_row = []
            for j in range(1,5*d+1):
                w = 0
                if k == j and l!=1:
                    w = -1 / eps
                temp_row.append(w)
            W1.append(temp_row)             
#print(W1)
# # Use the len() function to find the number of rows in the matrix
# num_rows = len(W1)

# # # Print the result
# print("Number of rows in the matrix W1 is:", num_rows) 
############################## 
# Bias matrix for second layer or first Hidden layer 1       
B1 = []
for j in range(1, d+1):#(corresponding to gamma 11,12 nodes)
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0
             if q==0:
               b= (-(i-1)/(eps*(n+1)))+1 
             else:
               b= -(i-1)/(eps*(n+1))       
             temp_row.append(b)
          B1.append(temp_row)
##          
for j in range(d+1,2*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0      
             temp_row.append(b)
          B1.append(temp_row)
##          
for j in range(2*d+1,4*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0
             if q==0:
               b= (-(i-1)/(eps*(n+1)))+1 
             else:
               b= -(i-1)/(eps*(n+1))       
             temp_row.append(b)
          B1.append(temp_row) 
for j in range(4*d+1,5*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0       
             temp_row.append(b)
          B1.append(temp_row) 
#(corresponding to gamma 21, 22 nodes)          
for j in range(1, d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0
             if q==0:
               b=( i/(eps*(n+1)) )+1 
             else:
               b= i/(eps*(n+1))       
             temp_row.append(b)
          B1.append(temp_row)
##          
for j in range(d+1,2*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0      
             temp_row.append(b)
          B1.append(temp_row)
##          
for j in range(2*d+1,4*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0
             if q==0:
               b= (i/(eps*(n+1)) )+1 
             else:
               b= i/(eps*(n+1))      
             temp_row.append(b)
          B1.append(temp_row) 
for j in range(4*d+1,5*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0       
             temp_row.append(b)
          B1.append(temp_row)         
###########          
#(corresponding to alpha 11,12 nodes)
for j in range(1, d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0
             if q==0:
               b= (-(i-1)/(eps*(n+1)))+1 
             else:
               b= -(i-1)/(eps*(n+1))       
             temp_row.append(b)
          B1.append(temp_row)
##          
for j in range(d+1,2*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0      
             temp_row.append(b)
          B1.append(temp_row)
##          
for j in range(2*d+1,4*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0
             if q==0:
               b= (-(i-1)/(eps*(n+1)))+1 
             else:
               b= -(i-1)/(eps*(n+1))       
             temp_row.append(b)
          B1.append(temp_row) 
for j in range(4*d+1,5*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0       
             temp_row.append(b)
          B1.append(temp_row)      
########## 
for j in range(1, d+1):#(corresponding to beta 11,12 nodes)
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0
             if q==0:
               b=( (i-1)/(eps*(n+1)) )+1 
             else:
               b= (i-1)/(eps*(n+1))       
             temp_row.append(b)
          B1.append(temp_row)
##          
for j in range(d+1,2*d+1):
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0      
             temp_row.append(b)
          B1.append(temp_row)
##          
for j in range(2*d+1,4*d+1):#(corresponding to beta nodes)
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0
             if q==0:
               b= ((i-1)/(eps*(n+1)) )+1 
             else:
               b= (i-1)/(eps*(n+1))      
             temp_row.append(b)
          B1.append(temp_row) 
for j in range(4*d+1,5*d+1):#(corresponding to beta nodes)
    for i in range(0, n+2):
        for q in range(2):
          temp_row = []
          for k in range(1):
             b = 0       
             temp_row.append(b)
          B1.append(temp_row)         
###########
#(corresponding to omega 11,12 nodes)
for j in range(1,d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0
                temp_row.append(b)
            B1.append(temp_row)   
for j in range(d+1,2*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0 
                if q==0:
                  b= (-(l-1)/(eps*m) )+1 
                else:
                  b= -(l-1)/(eps*m)                
                temp_row.append(b)
            B1.append(temp_row)  
for j in range(2*d+1,4*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0 
                temp_row.append(b)
            B1.append(temp_row)
for j in range(4*d+1,5*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0
                if q==0:
                  b= (-(l-1)/(eps*m) )+1 
                else:
                  b= -(l-1)/(eps*m)                
                temp_row.append(b)
            B1.append(temp_row)            
###########
#(corresponding to omega 21,22 nodes)
for j in range(1,d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0
                temp_row.append(b)
            B1.append(temp_row)   
for j in range(d+1,2*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0 
                if q==0:
                  b= (l/(eps*m))+1 
                else:
                  b= l/(eps*m)                
                temp_row.append(b)
            B1.append(temp_row)  
for j in range(2*d+1,4*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0 
                temp_row.append(b)
            B1.append(temp_row)
for j in range(4*d+1,5*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0
                if q==0:
                  b= (l/(eps*m) )+1 
                else:
                  b= l/(eps*m)                
                temp_row.append(b)
            B1.append(temp_row)            
###########
#(corresponding to alpha 21,22 nodes)
for j in range(1,d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0
                temp_row.append(b)
            B1.append(temp_row)   
for j in range(d+1,2*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0 
                if l!=1:
                  if q==0:
                    b= (-(l-1)/(eps*m) )+1 
                  else:
                    b= -(l-1)/(eps*m)                
                temp_row.append(b)
            B1.append(temp_row)  
for j in range(2*d+1,4*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0 
                temp_row.append(b)
            B1.append(temp_row)
for j in range(4*d+1,5*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0
                if l!=1:
                  if q==0:
                    b= (-(l-1)/(eps*m) )+1 
                  else:
                    b= -(l-1)/(eps*m)                
                temp_row.append(b)
            B1.append(temp_row)
###########
#(corresponding to beta 21,22 nodes)
for j in range(1,d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0
                temp_row.append(b)
            B1.append(temp_row)   
for j in range(d+1,2*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0 
                if l!=1:
                  if q==0:
                    b= ((l-1)/(eps*m) )+1 
                  else:
                    b= (l-1)/(eps*m)                
                temp_row.append(b)
            B1.append(temp_row)  
for j in range(2*d+1,4*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0 
                temp_row.append(b)
            B1.append(temp_row)
for j in range(4*d+1,5*d+1): 
    for l in range(1, m+1):
        for q in range(2):
            temp_row = []
            for k in range(1):
                b = 0
                if l!=1:
                  if q==0:
                    b= ((l-1)/(eps*m) )+1 
                  else:
                    b= (l-1)/(eps*m)                
                temp_row.append(b)
            B1.append(temp_row)            
###########              
#print(B1) 
#num_rows = len(B1)

# Print the result
#print("Number of rows in the matrix B1 is:", num_rows)                        
#print('Printing bias  matrix for first hidden layer') 
#print(B1)  
L1 = [] # gamma, alpha 11,12, beta 11,12, omega, alpha 21,22, beta 11,12, nodes
for i in range(len(W1)):
    L1_i_entry = np.maximum( (np.dot(W1[i], X) +B1[i]),0)  
    L1.append(L1_i_entry)
# print('Printing gamma, alpha 11,12, beta 11,12, omega, alpha 21,22, beta 11,12, nodes for first hidden layer')    
# print(L1)
########################################################################
#To construct the weight matrix for third layer (second hidden layer L2=W2*L1+B2)
W2=[]
# rho nodes in in (1, d) and gamma 11,12 nodes
A1=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=i
                else:
                  w=-i
              temp_row.append(w)
    A1.append(temp_row) 
#print(A1) 
# rho nodes in in (1, d) and gamma 21,22 nodes
A2=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=i
                else:
                  w=-i
              temp_row.append(w)
    A2.append(temp_row) 
#print(A2)
# rho nodes in in (1, d) and alpha 11,12 nodes
A3=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=-i
                else:
                  w=i
              temp_row.append(w)
    A3.append(temp_row) 
#print(A3) 
# rho nodes in in (1, d) and beta 11,12 nodes
A4=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=-i
                else:
                  w=i
              temp_row.append(w)
    A4.append(temp_row) 
# rho nodes in in (1, d) and omega 11,12 nodes
A5=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A5.append(temp_row) 
#print(A5) 
# rho nodes in in (1, d) and omega 21,22 nodes
A6=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A6.append(temp_row) 
#print(A6)
# rho nodes in in (1, d) and alpha 21,22 nodes
A7=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A7.append(temp_row) 
#print(A7) 
# rho nodes in in (1, d) and beta 21,22 nodes
A8=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A8.append(temp_row)    
for i in range(len(A1)):  #weight matrix for psi nodes in interval 4d+1 <= j <= 5d
    concatenated_row1 = A1[i] + A2[i] + A3[i] + A4[i]+A5[i] + A6[i] + A7[i] + A8[i]
    W2.append(concatenated_row1)
#print('weight matrix for third layer/second hidden layer W2')
#print(W2) 
######################################## 
# row_index = 0
# row = W2[row_index]

# # Find the number of elements in the selected row
# number_of_elements = len(row)

# # Print the result
# print(f"The number of elements in row {row_index + 3} is: {number_of_elements}")  
###########################
# rho nodes in in (d+1, 2*d+1): and gamma 11,12 nodes
A9=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    A9.append(temp_row) 
#print(A9) 
# rho nodes in in (d+1, 2*d+1): and gamma 21,22 nodes
A10=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    A10.append(temp_row) 
#print(A10)
# rho nodes in in (d+1, 2*d+1) and alpha 11,12 nodes
A11=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    A11.append(temp_row) 
#print(11) 
# rho nodes in in (d+1, 2*d+1) and beta 11,12 nodes
A12=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    A12.append(temp_row) 
# rho nodes in in (d+1, 2*d+1) and omega 11,12 nodes
A13=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A13.append(temp_row) 
#print(A13) 
# rho nodes in in (d+1, 2*d+1) and omega 21,22 nodes
A14=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A14.append(temp_row) 
#print(A14)
# rho nodes in in (d+1, 2*d+1) and alpha 21,22 nodes
A15=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A15.append(temp_row) 
#print(A15) 
# rho nodes in in (d+1, 2*d+1) and beta 21,22 nodes
A16=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A16.append(temp_row)    
for i in range(len(A9)):  #weight matrix for psi nodes in interval 4d+1 <= j <= 5d
    concatenated_row2 = A9[i] + A10[i] + A11[i] + A12[i]+A13[i] + A14[i] + A15[i] + A16[i]
    W2.append(concatenated_row2)
##################################
# rho nodes in in (2*d+1, 4*d+1) and gamma 11,12 nodes
A17=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=i
                else:
                  w=-i
              temp_row.append(w)
    A17.append(temp_row) 
#print(A17) 
# rho nodes in in (2*d+1, 4*d+1) and gamma 21,22 nodes
A18=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=i
                else:
                  w=-i
              temp_row.append(w)
    A18.append(temp_row) 
#print(A18)
# rho nodes in in (2*d+1, 4*d+1) and alpha 11,12 nodes
A19=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=-i
                else:
                  w=i
              temp_row.append(w)
    A19.append(temp_row) 
#print(A19) 
# rho nodes in in (2*d+1, 4*d+1) and beta 11,12 nodes
A20=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=-i
                else:
                  w=i
              temp_row.append(w)
    A20.append(temp_row) 
# rho nodes in in (2*d+1, 4*d+1) and omega 11,12 nodes
A21=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A21.append(temp_row) 
#print(A21) 
# rho nodes in in (2*d+1, 4*d+1) and omega 21,22 nodes
A22=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A22.append(temp_row) 
#print(A22)
# rho nodes in in (2*d+1, 4*d+1) and alpha 21,22 nodes
A23=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A23.append(temp_row) 
#print(A23) 
# rho nodes in in (2*d+1, 4*d+1) and beta 21,22 nodes
A24=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A24.append(temp_row)  
for i in range(len(A17)):  
    concatenated_row3 = A17[i] + A18[i] + A19[i] + A20[i]+A21[i] + A22[i] + A23[i] + A24[i]
    W2.append(concatenated_row3)
#print('weight matrix for third layer/second hidden layer W2')
#print(W2)  
###########################
# rho nodes in in (4*d+1, 5*d+1) and gamma 11,12 nodes
A25=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    A25.append(temp_row) 
#print(A25) 
# rho nodes in in (4*d+1, 5*d+1) and gamma 21,22 nodes
A26=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    A26.append(temp_row) 
#print(A26)
# rho nodes in in (4*d+1, 5*d+1) and alpha 11,12 nodes
A27=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    A27.append(temp_row) 
#print(A27) 
# rho nodes in in (4*d+1, 5*d+1) and beta 11,12 nodes
A28=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    A28.append(temp_row) 
# rho nodes in in (4*d+1, 5*d+1) and omega 11,12 nodes
A29=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A29.append(temp_row) 
#print(A29) 
# rho nodes in in (4*d+1, 5*d+1) and omega 21,22 nodes
A30=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A30.append(temp_row) 
#print(A30)
# rho nodes in in (4*d+1, 5*d+1) and alpha 21,22 nodes
A31=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A31.append(temp_row) 
#print(A31) 
# rho nodes in in (4*d+1, 5*d+1) and beta 21,22 nodes
A32=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    A32.append(temp_row)    
for i in range(len(A25)):  #weight matrix for psi nodes in interval 4d+1 <= j <= 5d
    concatenated_row4 = A25[i] + A26[i] + A27[i] + A28[i]+A29[i] + A30[i] + A31[i] + A32[i]
    W2.append(concatenated_row4)
# row_index = 1  # Replace this with the desired row index (0-based index)

# # Use the len() function to find the number of elements in the specified row
# num_elements = len(A23[row_index])

# # Print the result
# print("Number of elements in row", row_index, "is:", num_elements) 
################################
# psi nodes in in (1, d) and gamma 11,12 nodes
C1=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C1.append(temp_row) 
#print(C1) 
# psi nodes in in (1, d) and gamma 21,22 nodes
C2=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C2.append(temp_row) 
#print(C2)
# psi nodes in in (1, d) and alpha 11,12 nodes
C3=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C3.append(temp_row) 
#print(C3) 
# psi nodes in in (1, d) and beta 11,12 nodes
C4=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C4.append(temp_row) 
# psi nodes in in (1, d) and omega 11,12 nodes
C5=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    C5.append(temp_row) 
#print(C5) 
# psi nodes in in (1, d) and omega 21,22 nodes
C6=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    C6.append(temp_row) 
#print(A6)
# psi nodes in in (1, d) and alpha 21,22 nodes
C7=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    C7.append(temp_row) 
#print(A7) 
# psi nodes in in (1, d) and beta 21,22 nodes
C8=[]
for j in range(1, d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    C8.append(temp_row)    
for i in range(len(C1)):  
    concatenated_row5 = C1[i] + C2[i] + C3[i] + C4[i]+C5[i] + C6[i] + C7[i] + C8[i]
    W2.append(concatenated_row5)
#print('weight matrix for third layer/second hidden layer W2')
#print(W2)  
###########################
# psi nodes in in (d+1, 2*d+1): and gamma 11,12 nodes
C9=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C9.append(temp_row) 
#print(C9) 
# psi nodes in in (d+1, 2*d+1): and gamma 21,22 nodes
C10=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C10.append(temp_row) 
#print(C10)
# psi nodes in in (d+1, 2*d+1) and alpha 11,12 nodes
C11=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C11.append(temp_row) 
#print(11) 
# psi nodes in in (d+1, 2*d+1) and beta 11,12 nodes
C12=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C12.append(temp_row) 
# psi nodes in in (d+1, 2*d+1) and omega 11,12 nodes
C13=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=i
                else:
                  w=-i
              temp_row.append(w)
    C13.append(temp_row) 
#print(A13) 
# psi nodes in in (d+1, 2*d+1) and omega 21,22 nodes
C14=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=i
                else:
                  w=-i
              temp_row.append(w)
    C14.append(temp_row) 
#print(A14)
# psi nodes in in (d+1, 2*d+1) and alpha 21,22 nodes
C15=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=-i
                else:
                  w=i
              temp_row.append(w)
    C15.append(temp_row) 
#print(C15) 
# psi nodes in in (d+1, 2*d+1) and beta 21,22 nodes
C16=[]
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=-i
                else:
                  w=i
              temp_row.append(w)
    C16.append(temp_row)    
for i in range(len(C9)):  
    concatenated_row6 = C9[i] + C10[i] + C11[i] + C12[i]+C13[i] + C14[i] + C15[i] + C16[i]
    W2.append(concatenated_row6)
##################################
################################
# psi nodes in in (2*d+1, 4*d+1) and gamma 11,12 nodes
C17=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C17.append(temp_row) 
#print(C17) 
# psi nodes in in (2*d+1, 4*d+1) and gamma 21,22 nodes
C18=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C18.append(temp_row) 
#print(C18)
# psi nodes in in (2*d+1, 4*d+1) and alpha 11,12 nodes
C19=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C19.append(temp_row) 
#print(C19) 
# psi nodes in in (2*d+1, 4*d+1) and beta 11,12 nodes
C20=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C20.append(temp_row) 
# psi nodes in in (2*d+1, 4*d+1) and omega 11,12 nodes
C21=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    C21.append(temp_row) 
#print(C21) 
# psi nodes in in (2*d+1, 4*d+1) and omega 21,22 nodes
C22=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    C22.append(temp_row) 
#print(A22)
# psi nodes in in (2*d+1, 4*d+1) and alpha 21,22 nodes
C23=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    C23.append(temp_row) 
#print(A23) 
# psi nodes in in (2*d+1, 4*d+1) and beta 21,22 nodes
C24=[]
for j in range(2*d+1, 4*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              temp_row.append(w)
    C24.append(temp_row)    
for i in range(len(C17)):  
    concatenated_row7 = C17[i] + C18[i]+ C19[i] + C20[i] + C21[i] + C22[i] + C23[i] + C24[i]
    W2.append(concatenated_row7)
#print('weight matrix for third layer/second hidden layer W2')
#print(W2)  
###########################
# psi nodes in in (4*d+1, 5*d+1) and gamma 11,12 nodes
C25=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C25.append(temp_row) 
#print(C25) 
# psi nodes in in (4*d+1, 5*d+1) and gamma 21,22 nodes
C26=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C26.append(temp_row) 
#print(C26)
# psi nodes in in (4*d+1, 5*d+1) and alpha 11,12 nodes
C27=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C27.append(temp_row) 
#print(27) 
# psi nodes in in (4*d+1, 5*d+1) and beta 11,12 nodes
C28=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(0, n+2):
            for q in range(2):
              w=0
              temp_row.append(w)
    C28.append(temp_row) 
# psi nodes in in (4*d+1, 5*d+1) and omega 11,12 nodes
C29=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=i
                else:
                  w=-i
              temp_row.append(w)
    C29.append(temp_row) 
#print(C29) 
# psi nodes in in (4*d+1, 5*d+1) and omega 21,22 nodes
C30=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=i
                else:
                  w=-i
              temp_row.append(w)
    C30.append(temp_row) 
# psi nodes in in (4*d+1, 5*d+1) and alpha 21,22 nodes
C31=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=-i
                else:
                  w=i
              temp_row.append(w)
    C31.append(temp_row) 
#print(C31) 
# psi nodes in in (4*d+1, 5*d+1) and beta 21,22 nodes
C32=[]
for j in range(4*d+1, 5*d+1):
    temp_row = []
    for k in range(1, 5*d+1):
      for i in range(1, m+1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                  w=-i
                else:
                  w=i
              temp_row.append(w)
    C32.append(temp_row)    
for i in range(len(C25)):  
    concatenated_row8 = C25[i] + C26[i] + C27[i] + C28[i]+C29[i] + C30[i] + C31[i] + C32[i]
    W2.append(concatenated_row8)
# print('weight matrix for third layer/second hidden layer W2')
# print(W2)
############################################################################################   
###########################################################################################
#          To find the number of elements in a Row
##########################################################################################
#########################################################################################
# row_index = 0
# row = W2[row_index]

# # Find the number of elements in the selected row
# number_of_elements = len(row)

# # Print the result
# print(f"The number of elements in row {row_index + 10} is: {number_of_elements}")    
############################################################################################   
###########################################################################################
#          To find the number of elements in a column
##########################################################################################
#########################################################################################
# column_index = 0
# column = [row[column_index] for row in W2]

# # Find the number of elements in the selected column
# number_of_elements = len(column)

# # Print the result
# print(f"The number of elements in column {column_index + 1} is: {number_of_elements}")
########################################################################################
#######################################################################################
# Bias matrix for third layer/second hidden layer       
B2 = []
#(corresponding to rho nodes)
for j in range(1, d+1):
    temp_row = []
    for k in range(1):
              b=0       
              temp_row.append(b)
    B2.append(temp_row)
##          
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1):
              b=0       
              temp_row.append(b)
    B2.append(temp_row)
##          
for j in range(2*d+1,4*d+1):
          temp_row = []
          for k in range(1):  
              b=0      
              temp_row.append(b)
          B2.append(temp_row) 
for j in range(4*d+1,5*d+1):
    temp_row = []
    for k in range(1):
              b=0       
              temp_row.append(b)
    B2.append(temp_row) 
#(corresponding to psi nodes)
for j in range(1, d+1):
    temp_row = []
    for k in range(1):
              b=0       
              temp_row.append(b)
    B2.append(temp_row)
##          
for j in range(d+1, 2*d+1):
    temp_row = []
    for k in range(1):
              b=-1       
              temp_row.append(b)
    B2.append(temp_row)
##          
for j in range(2*d+1,4*d+1):
          temp_row = []
          for k in range(1):  
              b=0       
              temp_row.append(b)
          B2.append(temp_row) 
for j in range(4*d+1,5*d+1):
    temp_row = []
    for k in range(1):
              b=-1
              temp_row.append(b)
    B2.append(temp_row) 
#print(B2)  
L2 = [] # rho and psi nodes nodes
for i in range(len(W2)):
    L2_i_entry = np.maximum( (np.dot(W2[i], L1) +B2[i]),0)  
    L2.append(L2_i_entry)
# print('Printing rho and psi nodes for second hidden layer')    
# print(L2)
#To construct the weight matrix for fourth layer (third hidden layer L3=W3*L2+B3)
W3=[]
# rho nodes as identity map
D1=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    D1.append(temp_row)
D2=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    D2.append(temp_row) 
for i in range(len(D1)):  
    concatenated_row1 = D1[i] + D2[i] 
    W3.append(concatenated_row1)
#print(W3)
#psi nodes as identity map
D3=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    D3.append(temp_row)
D4=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    D4.append(temp_row) 
for i in range(len(D3)):  
    concatenated_row2 = D3[i] + D4[i] 
    W3.append(concatenated_row2)
##print(W3) 
# mu 11,12 nodes
D5=[]
for j in range(1,5*d+1):
    for i in range(1):
        for q in range(2):
          temp_row = []
          for k in range(1,d+1):
            w=0
            if j==k:
                w=1/eps
            temp_row.append(w)
          D5.append(temp_row)
D6=[]
for j in range(1,5*d+1):
    for i in range(1):
      for q in range(2):
          temp_row = []
          for k in range(d+1,2*d+1):
            w=0
            temp_row.append(w)
          D6.append(temp_row) 
D7=[]
for j in range(1,5*d+1):
    for i in range(1):
      for q in range(2):
          temp_row = []
          for k in range(2*d+1,4*d+1):
            w=0
            if j==k:
                w=1/eps
            temp_row.append(w)
          D7.append(temp_row)
D8=[]
for j in range(1,5*d+1):
    for i in range(1):
      for q in range(2):
          temp_row = []
          for k in range(4*d+1,5*d+1):
            w=0
            temp_row.append(w)
          D8.append(temp_row)
D9=[]
for j in range(1,5*d+1):
    for i in range(1):
      for q in range(2):
          temp_row = []
          for k in range(1,5*d+1):
            w=0
            temp_row.append(w)
          D9.append(temp_row)         
for i in range(len(D5)):  
    concatenated_row3 = D5[i] + D6[i] + D7[i]+ D8[i]+ D9[i]
    W3.append(concatenated_row3) 
#print(W3)    
#lambda 11,12 nodes
D10=[]
for j in range(1,5*d+1):
    for i in range(1):
        for q in range(2):
          temp_row = []
          for k in range(1,d+1):
            w=0
            if j==k:
                w=-1/eps
            temp_row.append(w)
          D10.append(temp_row)
D11=[]
for j in range(1,5*d+1):
    for i in range(1):
      for q in range(2):
          temp_row = []
          for k in range(d+1,2*d+1):
            w=0
            temp_row.append(w)
          D11.append(temp_row) 
D12=[]
for j in range(1,5*d+1):
    for i in range(1):
      for q in range(2):
          temp_row = []
          for k in range(2*d+1,4*d+1):
            w=0
            if j==k:
                w=-1/eps
            temp_row.append(w)
          D12.append(temp_row)
D13=[]
for j in range(1,5*d+1):
    for i in range(1):
      for q in range(2):
          temp_row = []
          for k in range(4*d+1,5*d+1):
            w=0
            temp_row.append(w)
          D13.append(temp_row)
D14=[]
for j in range(1,5*d+1):
    for i in range(1):
      for q in range(2):
          temp_row = []
          for k in range(1,5*d+1):
            w=0
            temp_row.append(w)
          D14.append(temp_row)         
for i in range(len(D10)):  
    concatenated_row4 = D10[i] + D11[i] + D12[i]+ D13[i]+ D14[i]
    W3.append(concatenated_row4) 
#print(W3)    
#mu 21,22 nodes in range(1,d+1)
D15=[]
for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
          temp_row = []
          for l in range(1,d+1):
              w=0
              if j==l and j != k:
                w=1/eps
              if k==l and j != k:
                w= -1/eps
              temp_row.append(w)
          D15.append(temp_row)
#print(D15)          
D16=[]
for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
          temp_row = []
          for l in range(d+1,5*d+1):
              w=0
              temp_row.append(w)
          D16.append(temp_row) 
D17=[]
for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
          temp_row = []
          for l in range(1,5*d+1):
              w=0
              temp_row.append(w)
          D17.append(temp_row)         
for i in range(len(D15)):  
    concatenated_row5 = D15[i] + D16[i] + D17[i]
    W3.append(concatenated_row5)
# print(W3)    
# mu 21,22 nodes in range(2d+1,3d+1)
D18=[]
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(1,2*d+1):
             w=0
             temp_row.append(w)
          D18.append(temp_row)
#print(D18)          
D19=[]
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(2*d+1,3*d+1):
             w=0
             if j==l and j != k:
               w=1/eps
             if k==l and j != k:
                w= -1/eps
             temp_row.append(w)
          D19.append(temp_row) 
D20=[]
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(3*d+1,5*d+1):
             w=0
             temp_row.append(w)
          D20.append(temp_row) 
D21=[]
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(1,5*d+1):
             w=0
             temp_row.append(w)
          D21.append(temp_row)           
for i in range(len(D18)):  
    concatenated_row6 = D18[i] + D19[i] + D20[i] + D21[i]
    W3.append(concatenated_row6)  
#print(W3)    
# lambda 21,22 nodes in range (1,d+1)
D22=[]
for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
          temp_row = []
          for l in range(1,d+1):
             w=0
             if j==l and j != k:
               w=-1/eps
             if k==l and j != k:
                w= 1/eps
             temp_row.append(w)
          D22.append(temp_row)
#print(D22)          
D23=[]
for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
          temp_row = []
          for l in range(d+1,5*d+1):
             w=0
             temp_row.append(w)
          D23.append(temp_row) 
D24=[]
for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
          temp_row = []
          for l in range(1,5*d+1):
             w=0
             temp_row.append(w)
          D24.append(temp_row)         
for i in range(len(D22)):  
    concatenated_row7 = D22[i] + D23[i] + D24[i]
    W3.append(concatenated_row7)  
# lambda 21,22 nodes in range(2d+1,3d+1)
D25=[]
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(1,2*d+1):
             w=0
             temp_row.append(w)
          D25.append(temp_row)
#print(D25)          
D26=[]
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(2*d+1,3*d+1):
             w=0
             if j==l and j != k:
               w=-1/eps
             if k==l and j != k:
                w= 1/eps
             temp_row.append(w)
          D26.append(temp_row) 
D27=[]
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(3*d+1,5*d+1):
             w=0
             temp_row.append(w)
          D27.append(temp_row) 
D28=[] #lambda 21,22 nodes in range(2d+1,3d+1) and psi nodes
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(1,5*d+1):
             w=0
             temp_row.append(w)
          D28.append(temp_row)           
for i in range(len(D25)):  
    concatenated_row8 = D25[i] + D26[i] + D27[i]+ D28[i]
    W3.append(concatenated_row8)  
# print('weight matrix for fourth layer /third hidden layer,W3')
# print(W3) 
B3=[]
# for rho nodes 
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B3.append(temp_row) 
# for psi nodes 
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B3.append(temp_row) 
# for mu 11,12 nodes 
for j in range(1,d+1):
    for k in range(1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             if q==0 :
               b=1
             temp_row.append(b)
          B3.append(temp_row)  
for j in range(d+1,2*d+1):
    for k in range(1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             temp_row.append(b)
          B3.append(temp_row) 
for j in range(2*d+1,4*d+1):
    for k in range(1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             if q==0 :
               b=1
             temp_row.append(b)
          B3.append(temp_row) 
for j in range(4*d+1,5*d+1):
    for k in range(1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             temp_row.append(b)
          B3.append(temp_row) 
# for lambda 11,12 nodes 
for j in range(1,d+1):
    for k in range(1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             if q==0 :
               b=1
             temp_row.append(b)
          B3.append(temp_row)  
for j in range(d+1,2*d+1):
    for k in range(1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             temp_row.append(b)
          B3.append(temp_row) 
for j in range(2*d+1,4*d+1):
    for k in range(1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             if q==0 :
               b=1
             temp_row.append(b)
          B3.append(temp_row) 
for j in range(4*d+1,5*d+1):
    for k in range(1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             temp_row.append(b)
          B3.append(temp_row) 
# for mu 21,22 nodes 
for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             if q==0:
               b=1
             temp_row.append(b)
          B3.append(temp_row)
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             if q==0:
               b=1
             temp_row.append(b)
          B3.append(temp_row)           
# for lambda 21,22 nodes 
for j in range(1,d+1):
    for k in range(1,d+1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             if q==0:
               b=1
             temp_row.append(b)
          B3.append(temp_row)
for j in range(2*d+1,3*d+1):
    for k in range(2*d+1,3*d+1):
        for q in range(2):
          temp_row = []
          for l in range(1):
             b=0
             if q==0:
               b=1
             temp_row.append(b)
          B3.append(temp_row)
#print(B3)          
L3 = [] # mu 11,12, lambda 11,12, mu 21,22, lambda 21,22 nodes
for i in range(len(W3)):
    L3_i_entry = np.maximum( (np.dot(W3[i], L2) +B3[i]),0) 
    L3.append(L3_i_entry)
# print('Printing mu 11,12, lambda 11,12, mu 21,22, lambda 21,22 nodes for third hidden layer')    
# print(L3) 
#To construct the weight matrix for fifth layer (fourth hidden layer L4=W4*L3+B4)
W4=[]
# rho nodes as identity map
E1=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    E1.append(temp_row)
E2=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E2.append(temp_row)
E3=[]
for j in range(1,5*d+1):
           temp_row = []
           for k in range(1,5*d+1):
              for l in range(1):
                 for q in range(2):
                    w=0
                    temp_row.append(w)
           E3.append(temp_row)
E4=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E4.append(temp_row) 
E5=[]
for j in range(1,5*d+1):
    temp_row = []
    for l in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
                w=0
                temp_row.append(w)
    E5.append(temp_row)
E6=[]
for j in range(1,5*d+1):
    temp_row = []
    for l in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
                w=0
                temp_row.append(w)
    E6.append(temp_row)
E7=[]
for j in range(1,5*d+1):
    temp_row = []
    for l in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
                w=0
                temp_row.append(w)
    E7.append(temp_row)
E8=[]
for j in range(1,5*d+1):
    temp_row = []
    for l in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
                w=0
                temp_row.append(w)
    E8.append(temp_row)    
for i in range(len(E1)): 
    concatenated_row1 = E1[i] + E2[i] +E3[i] + E4[i]+E5[i] + E6[i]+E7[i] + E8[i]
    W4.append(concatenated_row1)
#print(W4)
# psi nodes as identity map
E9=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E9.append(temp_row)
E10=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    E10.append(temp_row) 
E11=[]
for j in range(1,5*d+1):
           temp_row = []
           for k in range(1,5*d+1):
              for l in range(1):
                 for q in range(2):
                    w=0
                    temp_row.append(w)
           E11.append(temp_row)
E12=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E12.append(temp_row) 
E13=[]
for j in range(1,5*d+1):
    temp_row = []
    for l in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
                w=0
                temp_row.append(w)
    E13.append(temp_row)
E14=[]
for j in range(1,5*d+1):
    temp_row = []
    for l in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
                w=0
                temp_row.append(w)
    E14.append(temp_row)
E15=[]
for j in range(1,5*d+1):
    temp_row = []
    for l in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
                w=0
                temp_row.append(w)
    E15.append(temp_row)
E16=[]
for j in range(1,5*d+1):
    temp_row = []
    for l in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
                w=0
                temp_row.append(w)
    E16.append(temp_row)        
for i in range(len(E9)):  
    concatenated_row2 = E9[i] + E10[i] +E11[i] + E12[i]+E13[i] + E14[i]+E15[i] + E16[i]
    W4.append(concatenated_row2)
#print(W4)  
# tau nodes in range (1,d+1) and rho nodes
E17=[]
for j in range(1,d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E17.append(temp_row)
# tau nodes in range (1,d+1) and psi nodes    
E18=[]
for j in range(1,d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E18.append(temp_row) 
# tau nodes in range (1,d+1) and mu 11,12 nodes
E19=[]
for k in range(1,d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               if j==k:
                   if q==0:
                       w=-1
                   else:    
                       w=1
               temp_row.append(w)
    E19.append(temp_row)
# tau nodes in range (1,d+1) and lambda 11,12 nodes    
E20=[]
for k in range(1,d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               if j==k:
                   if q==0:
                       w=-1
                   else:    
                       w=1
               temp_row.append(w)
    E20.append(temp_row)   
# tau nodes in range (1,d+1) and mu 21,22 nodes in range (1,d+1) 
E21=[]
for j in range(1,d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               if j==m and k<j:
                   if q==0:
                       w=-1
                   else:   
                       w=1
               temp_row.append(w)
    E21.append(temp_row)
# tau nodes in range (1,d+1) and mu 21,22 nodes in range (2d+1,3d+1)     
E22=[]
for j in range(1,d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E22.append(temp_row) 
# tau nodes in range (1,d+1) and lambda 21,22 nodes in range (1,d+1) 
E23=[]
for j in range(1,d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               if j==m and k<j:
                   if q==0:
                       w=-1
                   else:   
                       w=1
               temp_row.append(w)
    E23.append(temp_row)
# tau nodes in range (1,d+1) and lambda 21,22 nodes in range (2d+1,3d+1)     
E24=[]
for j in range(1,d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E24.append(temp_row)    
for i in range(len(E17)):  
    concatenated_row3 = E17[i] + E18[i] +E19[i] + E20[i]+E21[i] + E22[i]+E23[i] + E24[i]
    W4.append(concatenated_row3) 
# tau nodes in range (d+1,2d+1) and rho nodes
E25=[]
for j in range(d+1,2*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E25.append(temp_row)
# tau nodes in range (d+1,2*d+1) and psi nodes    
E26=[]
for j in range(d+1,2*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E26.append(temp_row) 
# tau nodes in range (d+1,2*d+1) and mu 11,12 nodes
E27=[]
for k in range(d+1,2*d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E27.append(temp_row)
# tau nodes in range (d+1,2*d+1) and lambda 11,12 nodes    
E28=[]
for k in range(d+1,2*d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E28.append(temp_row)   
# tau nodes in range (d+1,2*d+1) and mu 21,22 nodes in range (1,d+1) 
E29=[]
for j in range(d+1,2*d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E29.append(temp_row)
# tau nodes in range (d+1,2*d+1) and mu 21,22 nodes in range (2d+1,3d+1)     
E30=[]
for j in range(d+1,2*d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E30.append(temp_row) 
# tau nodes in range (d+1,2*d+1) and lambda 21,22 nodes in range (1,d+1) 
E31=[]
for j in range(d+1,2*d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E31.append(temp_row)
# tau nodes in range (d+1,2*d+1) and lambda 21,22 nodes in range (2d+1,3d+1)     
E32=[]
for j in range(d+1,2*d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E32.append(temp_row)    
for i in range(len(E25)):  
    concatenated_row4 = E25[i] + E26[i] +E27[i] + E28[i]+E29[i] + E30[i]+E31[i] + E32[i]
    W4.append(concatenated_row4) 
# tau nodes in range (2*d+1,3*d+1) and rho nodes
E33=[]
for j in range(2*d+1,3*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E33.append(temp_row)
# tau nodes in range (2*d+1,3*d+1) and psi nodes    
E34=[]
for j in range(2*d+1,3*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E34.append(temp_row) 
# tau nodes in range (2*d+1,3*d+1) and mu 11,12 nodes
E35=[]
for k in range(2*d+1,3*d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               if j==k:
                   if q==0:
                       w=-1
                   else:    
                       w=1
               temp_row.append(w)
    E35.append(temp_row)
# tau nodes in range (2*d+1,3*d+1) and lambda 11,12 nodes    
E36=[]
for k in range(2*d+1,3*d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               if j==k:
                   if q==0:
                       w=-1
                   else:    
                       w=1
               temp_row.append(w)
    E36.append(temp_row)   
# tau nodes in range (2*d+1,3*d+1) and mu 21,22 nodes in range (1,d+1) 
E37=[]
for j in range(2*d+1,3*d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E37.append(temp_row)
# tau nodes in range (2*d+1,3*d+1) and mu 21,22 nodes in range (2d+1,3d+1)     
E38=[]
for j in range(2*d+1,3*d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               if j==m and k<j:
                   if q==0:
                       w=-1
                   else:   
                       w=1
               temp_row.append(w)
    E38.append(temp_row) 
# tau nodes in range (2*d+1,3*d+1) and lambda 21,22 nodes in range (1,d+1) 
E39=[]
for j in range(2*d+1,3*d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E39.append(temp_row)
# tau nodes in range (2*d+1,3*d+1) and lambda 21,22 nodes in range (2d+1,3d+1)     
E40=[]
for j in range(2*d+1,3*d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               if j==m and k<j:
                   if q==0:
                       w=-1
                   else:   
                       w=1
               temp_row.append(w)
    E40.append(temp_row)    
for i in range(len(E33)):  
    concatenated_row5 = E33[i] + E34[i] +E35[i] + E36[i]+E37[i] + E38[i]+E39[i] + E40[i]
    W4.append(concatenated_row5) 
# tau nodes in range (3*d+1,4*d+1) and rho nodes
E41=[]
for j in range(3*d+1,4*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E41.append(temp_row)
# tau nodes in range (3*d+1,4*d+1) and psi nodes    
E42=[]
for j in range(3*d+1,4*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E42.append(temp_row) 
# tau nodes in range (3*d+1,4*d+1) and mu 11,12 nodes
E43=[]
for k in range(3*d+1,4*d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               if j==k:
                   if q==0:
                       w=-1
                   else:    
                       w=1
               temp_row.append(w)
    E43.append(temp_row)
# tau nodes in range (3*d+1,4*d+1) and lambda 11,12 nodes    
E44=[]
for k in range(3*d+1,4*d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               if j==k:
                   if q==0:
                       w=-1
                   else:    
                       w=1
               temp_row.append(w)
    E44.append(temp_row)   
# tau nodes in range (3*d+1,4*d+1) and mu 21,22 nodes in range (1,d+1) 
E45=[]
for j in range(3*d+1,4*d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E45.append(temp_row)
# tau nodes in range (3*d+1,4*d+1) and mu 21,22 nodes in range (2d+1,3d+1)     
E46=[]
for j in range(3*d+1,4*d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E46.append(temp_row) 
# tau nodes in range (3*d+1,4*d+1) and lambda 21,22 nodes in range (1,d+1) 
E47=[]
for j in range(3*d+1,4*d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E47.append(temp_row)
# tau nodes in range (3*d+1,4*d+1) and lambda 21,22 nodes in range (2d+1,3d+1)     
E48=[]
for j in range(3*d+1,4*d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E48.append(temp_row)    
for i in range(len(E41)):  
    concatenated_row6 = E41[i] + E42[i] +E43[i] + E44[i]+E45[i] + E46[i]+E47[i] + E48[i]
    W4.append(concatenated_row6)    
# tau nodes in range (4*d+1,5*d+1) and rho nodes
E49=[]
for j in range(4*d+1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E49.append(temp_row)
# tau nodes in range (4*d+1,5*d+1) and psi nodes    
E50=[]
for j in range(4*d+1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    E50.append(temp_row) 
# tau nodes in range (4*d+1,5*d+1) and mu 11,12 nodes
E51=[]
for k in range(4*d+1,5*d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E51.append(temp_row)
# tau nodes in range (4*d+1,5*d+1) and lambda 11,12 nodes    
E52=[]
for k in range(4*d+1,5*d+1):
    temp_row = []
    for j in range(1,5*d+1):
        for l in range(1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E52.append(temp_row)   
# tau nodes in range (4*d+1,5*d+1) and mu 21,22 nodes in range (1,d+1) 
E53=[]
for j in range(4*d+1,5*d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E53.append(temp_row)
# tau nodes in range (4*d+1,5*d+1) and mu 21,22 nodes in range (2d+1,3d+1)     
E54=[]
for j in range(4*d+1,5*d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E54.append(temp_row) 
# tau nodes in range (4*d+1,5*d+1) and lambda 21,22 nodes in range (1,d+1) 
E55=[]
for j in range(4*d+1,5*d+1):
    temp_row = []
    for m in range(1,d+1):
        for k in range(1,d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E55.append(temp_row)
# tau nodes in range (4*d+1,5*d+1) and lambda 21,22 nodes in range (2d+1,3d+1)     
E56=[]
for j in range(4*d+1,5*d+1):
    temp_row = []
    for m in range(2*d+1,3*d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
               w=0
               temp_row.append(w)
    E56.append(temp_row)       
for i in range(len(E49)):  
    concatenated_row7 = E49[i] + E50[i] +E51[i] + E52[i]+E53[i] + E54[i]+E55[i] + E56[i]
    W4.append(concatenated_row7) 
# print('weight matrix for fifth layer /fourth hidden layer W4')
# print(W4)   
#To construct the bias matrix for fifth layer /fourth hidden layer hidden layer 
B4=[]
# for rho nodes 
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B4.append(temp_row) 
# for psi nodes 
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B4.append(temp_row) 
# for tau nodes in range
for j in range(1,d+1):
    temp_row = []
    for l in range(1):
        b=j+1
        temp_row.append(b)
    B4.append(temp_row)  
for j in range(d+1,2*d+1):
    temp_row = []
    for l in range(1):
        b=0
        temp_row.append(b)
    B4.append(temp_row) 
for j in range(2*d+1,3*d+1):
    temp_row = []
    for l in range(1):
        b=j-2*d+1
        temp_row.append(b)
    B4.append(temp_row) 
for j in range(3*d+1,4*d+1):
          temp_row = []
          for l in range(1):
             b=2
             temp_row.append(b)
          B4.append(temp_row) 
for j in range(4*d+1,5*d+1):
          temp_row = []
          for l in range(1):
             b=0
             temp_row.append(b)
          B4.append(temp_row)          
#print(B4)          
L4 = [] # Tau nodes
for i in range(len(W4)):
    L4_i_entry = np.maximum( (np.dot(W4[i], L3) +B4[i]),0) 
    L4.append(L4_i_entry)
# print('Printing Tau nodes for fifth layer /fourth hidden layer hidden layer')    
# print(L4) 
#To construct the weight matrix for sixth layer (fifth hidden layer L5=W5*L4+B5)
W5=[]
# rho nodes as identity map
F1=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    F1.append(temp_row) 
F2=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    F2.append(temp_row) 
F3=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    F3.append(temp_row)  
for i in range(len(F1)):  
    concatenated_row1 = F1[i] + F2[i] + F3[i] 
    W5.append(concatenated_row1)                
# psi nodes as identity map
F4=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    F4.append(temp_row) 
F5=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    F5.append(temp_row) 
F6=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    F6.append(temp_row)  
for i in range(len(F4)):  
    concatenated_row2 = F4[i] + F5[i] + F6[i] 
    W5.append(concatenated_row2)   
# eta nodes 
F7=[]
for j in range(1,5*d+1):
    for q in range(2):
       temp_row = []
       for k in range(1,5*d+1):
          w=0
          temp_row.append(w)
       F7.append(temp_row) 
F8=[]
for j in range(1,5*d+1):
    for q in range(2):
       temp_row = []
       for k in range(1,5*d+1):
          w=0
          temp_row.append(w)
       F8.append(temp_row)  
F9=[]
for j in range(1,5*d+1):
    for q in range(2):
       temp_row = []
       for k in range(1,5*d+1):
          w=0
          if k<=j:
              w=1 / eps
          temp_row.append(w)
       F9.append(temp_row)   
for i in range(len(F7)):  
    concatenated_row3 = F7[i] + F8[i] + F9[i] 
    W5.append(concatenated_row3)    
# print('weight matrix of sixth layer (fifth hidden layer')    
# print(W5) 
#Bias matrix for hidden layer 5

B5 = []
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B5.append(temp_row) 
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B5.append(temp_row)
for j in range(1,5*d+1):
    for q in range(2):
       temp_row = []
       for k in range(1):
          b=0
          if q==0:
              b=(-(d+1) / eps)  +1 
          else:
              b=-(d+1) / eps
          temp_row.append(b)
       B5.append(temp_row)
# print(B5)    
L5 = [] # eta nodes
for i in range(len(W5)):
    L5_i_entry =np.maximum( (np.dot(W5[i], L4)+B5[i]),0)   
    L5.append(L5_i_entry)
    
# print('Eta nodes')
# print(L5)
################## 
#To construct the weight matrix for seventh layer (sixth hidden layer L6=W6*L5+B6)  
W6=[]               
# psi nodes as identity map
G1=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    G1.append(temp_row) 
G2=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    G2.append(temp_row) 
G3=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        for q in range(2):
          w=0
          temp_row.append(w)
    G3.append(temp_row)  
for i in range(len(G1)):  
    concatenated_row1 = G1[i] + G2[i] + G3[i] 
    W6.append(concatenated_row1)   
# zeta nodes 
G4=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    G4.append(temp_row) 
G5=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    G5.append(temp_row) 
G6=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        for q in range(2):
          w=0
          if j==k:
              if q==0:
                  w=-C
              else:
                  w=C
          temp_row.append(w)
    G6.append(temp_row)  
for i in range(len(G4)):  
    concatenated_row2 = G4[i] + G5[i] + G6[i] 
    W6.append(concatenated_row2)     
# print('weight matrix of seventh layer/sixth hidden layer')    
# print(W6) 
#Bias matrix for hidden layer 6
B6 = []
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B6.append(temp_row) 
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B6.append(temp_row)
# print(B6)    
L6 = [] # zeta nodes
for i in range(len(W6)):
    L6_i_entry =np.maximum( (np.dot(W6[i], L5)+B6[i]),0)   
    L6.append(L6_i_entry)    
# print('Zeta nodes')
# print(L6)
#To construct the weight matrix for eighth layer (seventh hidden layer L7=W7*L6+B7)
W7=[]               
# psi nodes as identity map
H1=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    H1.append(temp_row) 
H2=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    H2.append(temp_row)   
for i in range(len(H1)):  
    concatenated_row1 = H1[i] + H2[i] 
    W7.append(concatenated_row1) 
# zeta nodes as identity map
H3=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    H3.append(temp_row) 
H4=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    H4.append(temp_row)   
for i in range(len(H3)):  
    concatenated_row2 = H3[i] + H4[i] 
    W7.append(concatenated_row2)    
# mu 31,32 nodes 
H5=[]
for j in range(3*d+1,4*d+1):
    for l in range(1):
        for q in range(2):
           temp_row = []
           for k in range(1,5*d+1):
              w=0
              temp_row.append(w)
           H5.append(temp_row) 
H6=[]# mu 31,32 nodes and eta nodes
for j in range(3*d+1,4*d+1):
    for l in range(1):
        for q in range(2):
           temp_row = []
           for k in range(1,5*d+1):
              w=0
              if j==k:
                  w=1 / eps 
              temp_row.append(w)
           H6.append(temp_row)          
for i in range(len(H5)):  
    concatenated_row3 = H5[i] + H6[i] 
    W7.append(concatenated_row3) 
# lambda 31,32 nodes 
H7=[]
for j in range(3*d+1,4*d+1):
    for l in range(1):
        for q in range(2):
           temp_row = []
           for k in range(1,5*d+1):
              w=0
              temp_row.append(w)
           H7.append(temp_row) 
H8=[]
for j in range(3*d+1,4*d+1):
    for l in range(1):
        for q in range(2):
           temp_row = []
           for k in range(1,5*d+1):
              w=0
              if j==k:
                  w=-1 / eps 
              temp_row.append(w)
           H8.append(temp_row)  
for i in range(len(H7)):  
    concatenated_row4 = H7[i] + H8[i] 
    W7.append(concatenated_row4)      
# print('weight matrix for eighth layer/seventh hidden layer)')    
# print(W7) 
#Bias matrix for hidden layer 7
B7 = []
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B7.append(temp_row) 
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B7.append(temp_row)
for j in range(3*d+1,4*d+1):
    for l in range(1):
        for q in range(2):
           temp_row = []
           for k in range(1):
               b=0
               if q==0:
                   b=1
               temp_row.append(b)
           B7.append(temp_row) 
for j in range(3*d+1,4*d+1):
    for l in range(1):
        for q in range(2):
           temp_row = []
           for k in range(1):
               b=0
               if q==0:
                   b=1
               temp_row.append(b)
           B7.append(temp_row)           
#print(B7)    
L7 = [] # Mu 31,32 and Lambda 31,32 nodes
for i in range(len(W7)):
    L7_i_entry =np.maximum( (np.dot(W7[i], L6)+B7[i]),0)   
    L7.append(L7_i_entry)    
# print('Mu 31,32 and Lambda 31,32 nodes')
# print(L7)
#To construct the weight matrix for ninth layer (eighth hidden layer L8=W8*L7+B8)
W8=[]               
# psi nodes as identity map
I1=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    I1.append(temp_row) 
I2=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    I2.append(temp_row) 
I3=[]
for j in range(1,5*d+1):
    temp_row = []
    for j in range(3*d+1,4*d+1):
        for l in range(1):
            for q in range(2):
              w=0
              temp_row.append(w)
    I3.append(temp_row)
I4=[]
for j in range(1,5*d+1):
    temp_row = []
    for j in range(3*d+1,4*d+1):
        for l in range(1):
            for q in range(2):
              w=0
              temp_row.append(w)
    I4.append(temp_row)    
for i in range(len(I1)):  
    concatenated_row1 = I1[i] + I2[i] + I3[i] + I4[i]
    W8.append(concatenated_row1)   
#print(W8)    
# varroh nodes
I5=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        temp_row.append(w)
    I5.append(temp_row) 
I6=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if k==j:
            w=1
        temp_row.append(w)
    I6.append(temp_row) 
I7=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(3*d+1,4*d+1):
        for l in range(1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                   w=(n+1)
                else:
                   w=-(n+1)
              temp_row.append(w)
    I7.append(temp_row)
I8=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(3*d+1,4*d+1):
        for l in range(1):
            for q in range(2):
              w=0
              if j==k:
                if q==0:
                   w=(n+1)
                else:
                   w=-(n+1)
              temp_row.append(w)
    I8.append(temp_row)    
for i in range(len(I5)):  
    concatenated_row2 = I5[i] + I6[i] + I7[i] + I8[i]
    W8.append(concatenated_row2)   
# print('weight matrix for ninth layer/eighth hidden layer)')    
# print(W8) 
#Bias matrix for hidden layer 8
B8 = []
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B8.append(temp_row) 
for j in range(1,3*d+1):
           temp_row = []
           for k in range(1):
               b=0
               temp_row.append(b)
           B8.append(temp_row) 
for j in range(3*d+1,4*d+1):
           temp_row = []
           for k in range(1):
                 b=-(n+1)
                 temp_row.append(b)
           B8.append(temp_row)   
for j in range(4*d+1,5*d+1):
           temp_row = []
           for k in range(1):
               b=0
               temp_row.append(b)
           B8.append(temp_row) 
# print('Bias matrix for ninth layer/eighth hidden layer')           
# print(B8)    
L8 = [] # Varrho nodes
for i in range(len(W8)):
    L8_i_entry =np.maximum( (np.dot(W8[i], L7)+B8[i]),0)   
    L8.append(L8_i_entry)    
# print('Varrho nodes')
# print(L8)
#To construct the weight matrix for tenth layer (ninth hidden layer L9=W9*L8+B9)
W9=[]               
# chi nodes and psi nodes
J1=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    J1.append(temp_row) 
J2=[]
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1,5*d+1):
        w=0
        if j==k:
            w=1
        temp_row.append(w)
    J2.append(temp_row)     
for i in range(len(J1)):  
    concatenated_row1 = J1[i] + J2[i] 
    W9.append(concatenated_row1)   
# print('weight matrix for tenth layer/ninth hidden layer)')    
#print(W9) 
#Bias matrix for tenth layer (ninth hidden layer)
B9 = []
for j in range(1,5*d+1):
    temp_row = []
    for k in range(1):
        b=0
        temp_row.append(b)
    B9.append(temp_row) 
# print('Bias matrix for tenth layer')           
# print(B9)    
L9 = [] # Chi nodes
for i in range(len(W9)):
    L9_i_entry =np.maximum( (np.dot(W9[i], L8)+B9[i]),0)   
    L9.append(L9_i_entry)    
# print('Input nodes in integer form')
# for i in L9:  
#         print(i)
Intx = [int(array[0]) for array in L9]
print("x in Int:", Intx)
###################################################################################       
###################################################################################
#                            Construction of e prime
###################################################################################
###################################################################################
# Pad three zeros to the end of the list
e.extend([0] * d)

#print("e_prime:", e)

#Therefore the number of input for substitution and deletion is
n1=n+d
#################################################################################################

#To construct the weight matrix for tenth hidden layer is L10=W10*L9+B10
W10 = []
# For substitution part
K1=[]      
for k in range(1,d+1):  #(psi nodes)
    for l in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,2 * d+1):
                w = 0
                if l == j and k != l:
                    w = 1 / eps
                if k == j and k != l:
                    w = -1 / eps    
                temp_row.append(w)
            K1.append(temp_row)
K2=[]      
for k in range(1,d+1):  #(psi nodes)
    for l in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(2 * d+1, 3*d+1):
                w = 0    
                temp_row.append(w)
            K2.append(temp_row)
K3=[]      
for k in range(1,d+1):  #(psi nodes)
    for l in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(3*d+1, 5*d+1):
                w = 0    
                temp_row.append(w)
            K3.append(temp_row) 
for i in range(len(K1)):  
    concatenated_row1 = K1[i] + K2[i] + K3[i]
    W10.append(concatenated_row1)             
###
K4=[]
for k in range(1,d+1):  #(rho nodes)
    for l in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,2 * d+1):
                w = 0
                if l == j and k != l:
                    w = -1 / eps
                if k == j and k != l:
                    w = 1 / eps    
                temp_row.append(w)
            K4.append(temp_row)
K5=[]      
for k in range(1,d+1):  #(psi nodes)
    for l in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(2 * d+1, 3*d+1):
                w = 0    
                temp_row.append(w)
            K5.append(temp_row)
K6=[]      
for k in range(1,d+1):  #(psi nodes)
    for l in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(3*d+1, 5*d+1):
                w = 0    
                temp_row.append(w)
            K6.append(temp_row) 
for i in range(len(K4)):  
    concatenated_row2 = K4[i] + K5[i] + K6[i]
    W10.append(concatenated_row2)             
#for identity map of x_j
K7=[] 
for k in range(1,2 * d+1):
    temp_row = []
    for j in range(1,2 * d+1):
        w = 0
        if k == j:
            w = 1
        temp_row.append(w)
    K7.append(temp_row)
K8=[] 
for k in range(1,2 * d+1):
    temp_row = []
    for j in range(2 * d+1, 3*d+1):
        w = 0
        temp_row.append(w)
    K8.append(temp_row)
K9=[] 
for k in range(1,2 * d+1):
    temp_row = []
    for j in range(3 * d+1, 5*d+1):
        w = 0
        temp_row.append(w)
    K9.append(temp_row) 
for i in range(len(K7)):  
    concatenated_row3 = K7[i] + K8[i] + K9[i]
    W10.append(concatenated_row3) 
# print(W10) 
# num_rows = len(W10)
# print("Number of rows:", num_rows)     
##########################################
#for deletion
K10=[]
for l in range(1,n+d+1):
    for k in range(2*d+1,3*d+1):
        for m in range(2):
            temp_row = []
            for j in range(1,2*d+1):
                w = 0
                temp_row.append(w)
            K10.append(temp_row)
K11=[]
for l in range(1,n+d+1):
    for k in range(2*d+1,3*d+1):
        for m in range(2):
            temp_row = []
            for j in range(2*d+1,3*d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            K11.append(temp_row)
K12=[]
for l in range(1,n+d+1):
    for k in range(2*d+1,3*d+1):
        for m in range(2):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                w = 0
                temp_row.append(w)
            K12.append(temp_row) 
for i in range(len(K10)):  
    concatenated_row4 = K10[i] + K11[i] + K12[i]
    W10.append(concatenated_row4)
# num_rows = len(W10)
# print("Number of rows:", num_rows)      
K13=[]
for l in range(1,n+d+1):
    for k in range(2*d+1,3*d+1):
        for m in range(2):
            temp_row = []
            for j in range(1,2*d+1):
                w = 0
                temp_row.append(w)
            K13.append(temp_row)
K14=[]           
for l in range(1,n+d+1):
    for k in range(2*d+1,3*d+1):
        for m in range(2):
            temp_row = []
            for j in range(2*d+1,3*d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            K14.append(temp_row)
K15=[]
for l in range(1,n+d+1):
    for k in range(2*d+1,3*d+1):
        for m in range(2):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                w = 0
                temp_row.append(w)
            K15.append(temp_row) 
for i in range(len(K13)):  
    concatenated_row5 = K13[i] + K14[i] + K15[i]
    W10.append(concatenated_row5) 
# num_rows = len(W10)
# print("Number of rows:", num_rows)      
##################################################
# for Insertion
J16 = []
for k in range(3*d+1,4*d+1):  # eta nodes
   for j in range(3*d+1,4*d+1):
      for q in range(2):
         temp_row = []  
         for l in range (1,(3 * d)+1):  
            w = 0
            temp_row.append(w)
         J16.append(temp_row)
J17 = []
for k in range(3*d+1,4*d+1):  # eta nodes
   for j in range(3*d+1,4*d+1):
      for q in range(2):
         temp_row = []  
         for l in range ((3 * d)+1,(5 * d)+1):  
            w = 0
            if k == l and k!=j:
               w = -1 / eps
            if j==l and k!=j: 
               w=1 / eps
            temp_row.append(w)
         J17.append(temp_row)  
for i in range(len(J16)):  
    concatenated_row6 = J16[i] + J17[i] 
    W10.append(concatenated_row6)          
##
J18 = []
for k in range(3*d+1,4*d+1):  #(psi^11,psi^12 nodes)
   for j in range(3*d+1,4*d+1):
      for q in range(2):
         temp_row = []  
         for l in range (1,(3 * d)+1):  
            w = 0
            temp_row.append(w)
         J18.append(temp_row)
J19 = []
for k in range(3*d+1,4*d+1):  #(psi^11,psi^12 nodes)
   for j in range(3*d+1,4*d+1):
      for q in range(2):
         temp_row = []  
         for l in range ((3 * d)+1,(5 * d)+1):  
            w = 0
            if k == l and k!=j:
               w = -1 / eps
            if j==l and k!=j: 
               w=1 / eps
            temp_row.append(w)
         J19.append(temp_row)         
for i in range(len(J18)):  
    concatenated_row7 = J18[i] + J19[i] 
    W10.append(concatenated_row7)
##
J20 = []
for k in range(3*d+1,4*d+1):  #(rho^11,rho^12 nodes)
   for j in range(3*d+1,4*d+1):
      for q in range(2):
         temp_row = []  
         for l in range (1,(3 * d)+1):  
            w = 0
            temp_row.append(w)
         J20.append(temp_row)
J21 = []
for k in range(3*d+1,4*d+1):  #(rho^11,rho^12 nodes)
   for j in range(3*d+1,4*d+1):
      for q in range(2):
         temp_row = []  
         for l in range ((3 * d)+1,(5 * d)+1):  
            w = 0
            if k == l and k!=j:
               w = 1 / eps
            if j==l and k!=j: 
               w=-1 / eps
            temp_row.append(w)
         J21.append(temp_row)         
for i in range(len(J20)):  
    concatenated_row8 = J20[i] + J21[i] 
    W10.append(concatenated_row8)
#
J22=[]
for i in range(3*d+1,(5 * d)+1):#(x_{j} nodes as identity map)
   temp_row = []
   for l in range(1,(3 * d)+1):
       w = 0
       temp_row.append(w)
   J22.append(temp_row)
J23=[]
for i in range(3*d+1,(5 * d)+1):#(x_{j} nodes as identity map)
   temp_row = []
   for l in range((3 * d)+1,(5 * d)+1):
       w = 0
       if i == l:
           w = 1 
       temp_row.append(w)
   J23.append(temp_row)   
for i in range(len(J22)):  
    concatenated_row9 = J22[i] + J23[i] 
    W10.append(concatenated_row9)
# print('weight matrix of Tenth hidden layer')    
# for i in W10:
#     print(i)
    
#Bias matrix for layer 10

B10 = []
# (bias of psi nodes)

for k in range(1,d+1):
    for l in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if q==0:
                    b = 1
                else:
                    b=0
                temp_row.append(b)
            B10.append(temp_row)

# (bias of rho nodes)

for k in range(1,d+1):
    for l in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if q==0:
                    b = 1
                else:
                    b=0
                temp_row.append(b)
            B10.append(temp_row)

#(bias of x_j)

for l in range(1, 2 * d+1):
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B10.append(temp_row)
###################################
#for deletion
###################################
# top(bias matrix for alphas)

for i in range(1,n+d+1):
    for k in range(2*d+1, 3*d+1):
        for m in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if m==0:
                    b = (-i / eps)+1
                else:
                    b= -i / eps
                temp_row.append(b)
            B10.append(temp_row)

# bottom(bias matrix for beta)

for i in range(1,n+d+1):
    for k in range(2*d+1, 3*d+1):
        for m in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if m==0:
                    b = i / eps+1
                else:
                    b=i / eps
                temp_row.append(b)
            B10.append(temp_row)
###################################
#for insertion
################################### 
#bias of eta 1 and eta 2 nodes

for k in range(3*d+1,4*d+1):
    for j in range (3*d+1,4*d+1):
        for q in range(2):
          temp_row = []
          for l in range(1):
                b = 0
                if q==0:
                    b = 1
                temp_row.append(b)
          B10.append(temp_row)     
###
# bias of psi 11 and psi 12

for j in range(3*d+1,4*d+1):
    for k in range(3*d+1,4*d+1):
        for q in range(2):
            temp_row = []
            for l in range(1):
                b = 0
                if q==0:
                    b = 1
                temp_row.append(b)
            B10.append(temp_row)

# bias of rho 21 and rho 22

for j in range(3*d+1,4*d+1):
    for k in range(3*d+1,4*d+1):
        for q in range(2):
            temp_row = []
            for l in range(1):
                b = 0
                if q==0:
                    b = 1
                temp_row.append(b)
            B10.append(temp_row)
##            
#bias of x_{j} as identity function)

for k in range(3*d+1,5*d+1):
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B10.append(temp_row) 
#print(B10) 
# num_rows = len(W10)
# print("Number of rows:", num_rows)         
L10 = [] # psi and rho nodes
for i in range(len(W10)):
    L10_i_entry =np.maximum( (np.dot(W10[i], L9)+B10[i]),0)  
    L10.append(L10_i_entry)
    # print('this is index i:', i)
    # print('this is the value L10[i]:', L10_i_entry)
    
# print('Nodes of tenth layer')
# for i in L10:
#     print(i)
##################
#To construct the weight matrix for eleventh hidden layer is L11=W11*L10+B11
W11 = [] 
M1=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for k in range(1,d+1):  #(psi nodes)
        for l in range(1,d+1):
            for q in range(2):
                w = 0
                if l == j and k < l:
                  if q==0:
                    w = -C 
                  else:
                    w= C     
                temp_row.append(w)
    M1.append(temp_row)
##
M2=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for k in range(1,d+1):  #(rho nodes)
        for l in range(1,d+1):
            for q in range(2):
                w = 0
                if l == j and k < l:
                  if q==0:
                    w = -C 
                  else:
                    w= C 
                temp_row.append(w)
    M2.append(temp_row)
##
M3=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for k in range(1,d+1):  #(x_j nodes)
      w = 0
      if k == j:
          w = 1 
      temp_row.append(w)
    M3.append(temp_row)  
#   
M4=[]
for j in range(1,d+1):#(x'_j nodes)
    temp_row = []
    for k in range(d+1,2*d+1):#(x_j+d nodes)
        w = 0
        temp_row.append(w)
    M4.append(temp_row)
##
M5=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for l in range(1,n+d+1):
        for k in range(2*d+1,3*d+1):#(DELETION nodes)
            for q in range(2):
                w = 0    
                temp_row.append(w)
    M5.append(temp_row)
##
M6=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for l in range(1,n+d+1):
        for k in range(2*d+1,3*d+1):#(DELETION nodes)
            for q in range(2):
                w = 0    
                temp_row.append(w)
    M6.append(temp_row)
##
M7=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for k in range(3*d+1,4*d+1):  # INSERTION nodes
        for j in range(3*d+1,4*d+1):
          for q in range(2):
                w = 0    
                temp_row.append(w)
    M7.append(temp_row)
##
M8=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for k in range(3*d+1,4*d+1):  
        for j in range(3*d+1,4*d+1):
          for q in range(2):
                w = 0
                temp_row.append(w)
    M8.append(temp_row)
##
M9=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for k in range(3*d+1,4*d+1):  
        for j in range(3*d+1,4*d+1):
          for q in range(2):
            w = 0
            temp_row.append(w)
    M9.append(temp_row)
##
M10=[]    
for j in range(1,d+1):  #(x'_j nodes)
    temp_row = []
    for i in range(3*d+1,(5 * d)+1):
            w = 0
            temp_row.append(w)
    M10.append(temp_row) 
#print(M10)    
for i in range(len(M1)):
    concatenated_row1 = M1[i] + M2[i] + M3[i] + M4[i]+M5[i] + M6[i] + M7[i] + M8[i]+M9[i] + M10[i] 
    W11.append(concatenated_row1) 
#print(W11)     
# num_rows = len(W11)
# num_columns = len(W11[0])  # Assumes all rows have the same number of columns

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)   
##########################
M11=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for k in range(1,d+1):  #substitution(psi nodes)
        for l in range(1,d+1):
            for q in range(2):
                w = 0     
                temp_row.append(w)
    M11.append(temp_row)
##
M12=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for k in range(1,d+1):  #substitution(rho nodes)
        for l in range(1,d+1):
            for q in range(2):
                w = 0
                temp_row.append(w)
    M12.append(temp_row)
##
M13=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for k in range(1,d+1):  #substitution(x_j nodes)
      w = 0 
      temp_row.append(w)
    M13.append(temp_row)      
M14=[]#(for identity map of x_j+d)
for j in range(d+1,2*d+1):#substitution(x'_j+d nodes)
    temp_row = []
    for k in range(d+1,2*d+1):
        w = 0
        if j==k:
            w=1
        temp_row.append(w)
    M14.append(temp_row)
##
##
M15=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for l in range(1,n+d+1):
        for k in range(2*d+1,3*d+1):#(DELETION nodes)
            for q in range(2):
                w = 0    
                temp_row.append(w)
    M15.append(temp_row)
##
M16=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for l in range(1,n+d+1):
        for k in range(2*d+1,3*d+1):
            for q in range(2):
                w = 0
                temp_row.append(w)
    M16.append(temp_row)
##
M17=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for k in range(3*d+1,4*d+1):  # INSERTION nodes
        for j in range(3*d+1,4*d+1):
          for q in range(2):
                w = 0    
                temp_row.append(w)
    M17.append(temp_row)
##
M18=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for k in range(3*d+1,4*d+1):  
        for j in range(3*d+1,4*d+1):
          for q in range(2):
                w = 0
                temp_row.append(w)
    M18.append(temp_row)
##
M19=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for k in range(3*d+1,4*d+1):  
        for j in range(3*d+1,4*d+1):
          for q in range(2):
            w = 0
            temp_row.append(w)
    M19.append(temp_row)
##
M20=[]    
for j in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for i in range(3*d+1,(5 * d)+1):
                w = 0
                temp_row.append(w)
    M20.append(temp_row)
##   
for i in range(len(M11)):
    concatenated_row2 = M11[i] + M12[i] + M13[i] + M14[i]+M15[i] + M16[i] + M17[i] + M18[i]+M19[i] + M20[i] 
    W11.append(concatenated_row2) 
# num_rows = len(W11)
# num_columns = len(W11[0])  # Assumes all rows have the same number of columns

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)     
##############    ############ 
# deletion
##############################
M21 = []
for i in range(1,n+d+1): # eta nodes
    for m in range(2):
        temp_row = []
        for k in range(1,d+1):  #(psi nodes of substitution)
            for l in range(1,d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M21.append(temp_row)  
M22 = []
for i in range(1,n+d+1):# eta nodes
    for m in range(2):
        temp_row = []
        for k in range(1,d+1):  #(rho nodes of substitution)
            for l in range(1,d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M22.append(temp_row) 
M23 = []
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for k in range(1,d+1):  #(x_j nodes of substitution)
                    w = 0
                    temp_row.append(w)
        M23.append(temp_row)  
M24 = []
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for k in range(d+1,2*d+1):#(x_j+d nodes of substitution)
                    w = 0
                    temp_row.append(w)
        M24.append(temp_row)  
M25 = []
#  eta and alphas
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for l in range(1,n+d+1): # deletion nodes
            for k in range(2*d+1,3*d+1):
                for q in range(2):
                    w = 0
                    if i == l:
                        if q == 0:
                          w = -1 / eps
                        else: # q = 1
                            w = 1 / eps
                    temp_row.append(w)
        M25.append(temp_row) 
M26 = []  #  eta and beta       
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for l in range(1,n+d+1): # deletion nodes
            for k in range(2*d+1,3*d+1):
                for q in range(2):
                    w = 0
                    if i == l:
                        if q == 0:
                          w = -1 / eps
                        else: # q = 1
                            w = 1 / eps
                    temp_row.append(w)
        M26.append(temp_row) 
M27 = []
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for k in range(3*d+1,4*d+1):  # insertion nodes
            for j in range(3*d+1,4*d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
        M27.append(temp_row)  
M28 = []
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for k in range(3*d+1,4*d+1):  #(insertion nodes)
            for j in range(3*d+1,4*d+1):
              for q in range(2):
                  w = 0
                  temp_row.append(w)
        M28.append(temp_row)  
M29 = []
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for k in range(3*d+1,4*d+1):  # insertion nodes
            for j in range(3*d+1,4*d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
        M29.append(temp_row)  
M30 = []
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
        M30.append(temp_row) 
for i in range(len(M21)):
    concatenated_row3 = M21[i] + M22[i] + M23[i] + M24[i]+M25[i] + M26[i] + M27[i] + M28[i]+M29[i] + M30[i]  
    W11.append(concatenated_row3)
####################
# insertion
M31 = []    
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for k in range(1,d+1):  #(psi nodes of substitution)
            for l in range(1,d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M31.append(temp_row)  
M32 = []
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for k in range(1,d+1):  #(rho nodes of substitution)
            for l in range(1,d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M32.append(temp_row) 
M33 = []
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for k in range(1,d+1):  #(x_j nodes of substitution)
                    w = 0
                    temp_row.append(w)
        M33.append(temp_row)  
M34 = []
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for k in range(d+1,2*d+1):#(x_j+d nodes of substitution)
                    w = 0
                    temp_row.append(w)
        M34.append(temp_row)  
M35 = []
#  eta and alphas
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for l in range(1,n+d+1): # deletion nodes
            for k in range(2*d+1,3*d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M35.append(temp_row) 
M36 = []  #  eta and beta       
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for l in range(1,n+d+1): # deletion nodes
            for k in range(2*d+1,3*d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M36.append(temp_row) 
M37 = []
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for k in range(3*d+1,4*d+1):  # insertion nodes
            for j in range(3*d+1,4*d+1):
              for q in range(2):
                w = 0
                if j == i:
                    if q == 0:
                        w = 1
                    else: # q = 1
                        w = -1
                temp_row.append(w)
        M37.append(temp_row)  
M38 = []
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for k in range(3*d+1,4*d+1):  #(insertion nodes)
            for j in range(3*d+1,4*d+1):
              for q in range(2):
                  w = 0
                  if j == i and k>=j:
                      if q == 0:
                          w = -1
                      else: # q = 1
                          w = 1
                  temp_row.append(w)
        M38.append(temp_row)  
M39 = []
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for k in range(3*d+1,4*d+1):  # insertion nodes
            for j in range(3*d+1,4*d+1):
              for q in range(2):
               w = 0
               if j == i and k>=j:
                   if q == 0:
                       w = -1
                   else: # q = 1
                       w = 1                
               temp_row.append(w)
        M39.append(temp_row)  
M40 = []
for i in range(3*d+1,4*d+1): # verroh_j nodes
        temp_row = []
        for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
        M40.append(temp_row) 
for i in range(len(M31)):
    concatenated_row4 = M31[i] + M32[i] + M33[i] + M34[i]+M35[i] + M36[i] + M37[i] + M38[i]+M39[i] + M40[i]  
    W11.append(concatenated_row4)
####################
M41 = []    
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for k in range(1,d+1):  #(psi nodes of substitution)
            for l in range(1,d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M41.append(temp_row)  
M42 = []
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for k in range(1,d+1):  #(rho nodes of substitution)
            for l in range(1,d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M42.append(temp_row) 
M43 = []
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for k in range(1,d+1):  #(x_j nodes of substitution)
                    w = 0
                    temp_row.append(w)
        M43.append(temp_row)  
M44 = []
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for k in range(d+1,2*d+1):#(x_j+d nodes of substitution)
                    w = 0
                    temp_row.append(w)
        M44.append(temp_row)  
M45 = []
#  eta and alphas
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for l in range(1,n+d+1): # deletion nodes
            for k in range(2*d+1,3*d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M45.append(temp_row) 
M46 = []  #  eta and beta       
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for l in range(1,n+d+1): # deletion nodes
            for k in range(2*d+1,3*d+1):
                for q in range(2):
                    w = 0
                    temp_row.append(w)
        M46.append(temp_row) 
M47 = []
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for k in range(3*d+1,4*d+1):  # insertion nodes
            for j in range(3*d+1,4*d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
        M47.append(temp_row)  
M48 = []
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for k in range(3*d+1,4*d+1):  #(insertion nodes)
            for j in range(3*d+1,4*d+1):
              for q in range(2):
                  w = 0
                  temp_row.append(w)
        M48.append(temp_row)  
M49 = []
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for k in range(3*d+1,4*d+1):  # insertion nodes
            for j in range(3*d+1,4*d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
        M49.append(temp_row)  
M50 = []
for i in range(3*d+1,5*d+1): # x_j nodes
        temp_row = []
        for j in range(3*d+1,5*d+1):
                  w = 0
                  if j==i:
                    w=1
                  temp_row.append(w)
        M50.append(temp_row) 
for i in range(len(M41)):
    concatenated_row5 = M41[i] + M42[i] + M43[i] + M44[i]+M45[i] + M46[i] + M47[i] + M48[i]+M49[i] + M50[i]  
    W11.append(concatenated_row5)               
# print('weight matrix of eleventh hidden layer')    
# for i in W11:
#       print(i)         
    
#Bias matrix for hidden layer 11

B11 = []
# for substitution nodes
# (bias of x' nodes)

for j in range(1,d+1):
    temp_row = []
    for k in range(1):
        b = C*(j-1)
        temp_row.append(b)
    B11.append(temp_row)

# (bias of x_j+d nodes)

for j in range(1,d+1):
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B11.append(temp_row)
####
# for deletion nodes
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for j in range(1):
            b = 0
            if m==0:
                b = (d/ eps)+1
            else:
                b = d / eps
            temp_row.append(b)
        B11.append(temp_row)    
####
# for insertion nodes
for j in range(1, d+1): #(corresponding to varrho nodes)
    temp_row = []
    for l in range(1):
        b = d-j+1
        temp_row.append(b)
    B11.append(temp_row)           
           
for k in range(3*d+1, (5*d)+1):#(corresponding to x_{j} nodes)
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B11.append(temp_row)
# num_rows = len(L10)
# print("Number of rows:", num_rows) 
# num_columns = len(W11)  # Assumes all rows have the same number of columns
# print("Number of columns:", num_columns)    
# print(B11)    
L11 = [] # x' nodes
for i in range(len(W11)):
    L11_i_entry =np.maximum( (np.dot(W11[i], L10)+B11[i]),0)   
    L11.append(L11_i_entry)
    # print('this is index i:', i)
    # print('this is the value L11[i]:', L11_i_entry)
    
# print('eleventh hidden layer')
# for i in L11:
#     print(i)
# # ##################
#To construct the weight matrix for thirteenth layer /twelveth hidden layer is L12=W12*L11+B12
W12 = []
#
N1=[]
for l in range(1,n+d+1):  #(alpha nodes)
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,d+1):
                w = 0
                if k == j:
                    w = 1 / eps
                temp_row.append(w)
            N1.append(temp_row)
##
N2=[]       
for l in range(1,n+d+1):  
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                temp_row.append(w)
            N2.append(temp_row)
##
N3=[]
for l in range(1,n+d+1):  #(alpha nodes)
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  temp_row.append(w)
            N3.append(temp_row)
##
N4=[]
for l in range(1,n+d+1):  #(alpha nodes)
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(3*d+1,4*d+1): # insertion nodes
                  w = 0
                  temp_row.append(w)
            N4.append(temp_row)
##
N5=[]
for l in range(1,n+d+1):  #(alpha nodes)
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
            N5.append(temp_row)            
for i in range(len(N1)):
    concatenated_row1 = N1[i] + N2[i] + N3[i] + N4[i]+N5[i]  
    W12.append(concatenated_row1)
#print(W12)    
N6=[]       
for l in range(1,n+d+1):  #(beta nodes)
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,d+1):
                w = 0
                if k == j:
                    w = -1 / eps
                temp_row.append(w)
            N6.append(temp_row)
N7=[]       
for l in range(1,n+d+1):  
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                temp_row.append(w)
            N7.append(temp_row)
##
N8=[]
for l in range(1,n+d+1):  #(beta nodes)
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  temp_row.append(w)
            N8.append(temp_row)
##
N9=[]
for l in range(1,n+d+1):  #(beta nodes)
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(3*d+1,4*d+1):
                  w = 0
                  temp_row.append(w)
            N9.append(temp_row)
##
N10=[]
for l in range(1,n+d+1):  #(beta nodes)
    for k in range(1,d+1):
        for q in range(2):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
            N10.append(temp_row)            
for i in range(len(N6)):
    concatenated_row2 = N6[i] + N7[i] + N8[i] + N9[i]+N10[i]  
    W12.append(concatenated_row2) 
###
N11=[]
for l in range(d+1,2*d+1):  #(x_j+d nodes)
    temp_row = []
    for j in range(1,d+1):
        w = 0
        temp_row.append(w)
    N11.append(temp_row)
##
N12=[]       
for l in range(d+1,2*d+1):  #(x_j+d nodes identity map)
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                if l==j:
                    w=1
                temp_row.append(w)
            N12.append(temp_row)
##
N13=[]
for l in range(d+1,2*d+1):  #(x_j+d nodes)
            temp_row = []
            for j in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  temp_row.append(w)
            N13.append(temp_row)
##
N14=[]
for l in range(d+1,2*d+1):  #(x_j+d nodes)
            temp_row = []
            for j in range(3*d+1,4*d+1): # insertion nodes
                  w = 0
                  temp_row.append(w)
            N14.append(temp_row)
##
N15=[]
for l in range(d+1,2*d+1):  #(x_j+d nodes)
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
            N15.append(temp_row)            
for i in range(len(N11)):
    concatenated_row3 = N11[i] + N12[i] + N13[i] + N14[i] + N15[i]  
    W12.append(concatenated_row3)
#####################################
# deletion 
#####################################    
N16=[]       
for l in range(1,n+d+1):  #(mu nodes)
    for q in range(2):
        temp_row = []
        for j in range(1,d+1):
                w = 0
                temp_row.append(w)
        N16.append(temp_row)
N17=[]       
for l in range(1,n+d+1):  #(mu nodes)
    for q in range(2):
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                temp_row.append(w)
            N17.append(temp_row)
##
N18=[]
for l in range(1,n+d+1):  #(mu nodes)
    for q in range(2):
            temp_row = []
            for j in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  if l==j:
                      if m==0:
                        w = 1 / eps
                      else:
                        w = -1 / eps
                  temp_row.append(w)
            N18.append(temp_row)
##
N19=[]
for l in range(1,n+d+1):  #(mu nodes)
    for q in range(2):
            temp_row = []
            for j in range(3*d+1,4*d+1):# insertion nodes
                  w = 0
                  temp_row.append(w)
            N19.append(temp_row)
##
N20=[]
for l in range(1,n+d+1):  #(mu nodes)
    for q in range(2):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
            N20.append(temp_row)            
for i in range(len(N16)):
    concatenated_row4 = N16[i] + N17[i] + N18[i] + N19[i]+N20[i]  
    W12.append(concatenated_row4)            
N21=[]       
for l in range(1,n+d+1):  #(lambda nodes)
    for q in range(2):
        temp_row = []
        for j in range(1,d+1):
                w = 0
                temp_row.append(w)
        N21.append(temp_row)
N22=[]       
for l in range(1,n+d+1):  #(lambda nodes)
    for q in range(2):
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                temp_row.append(w)
            N22.append(temp_row)
##
N23=[]
for l in range(1,n+d+1):  #(lambda nodes)
    for q in range(2):
            temp_row = []
            for j in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  if l==j:
                      if m==0:
                        w = -1 / eps
                      else:
                        w = 1 / eps
                  temp_row.append(w)
            N23.append(temp_row)
##
N24=[]
for l in range(1,n+d+1):  #(lambda nodes)
    for q in range(2):
            temp_row = []
            for j in range(3*d+1,4*d+1):# insertion nodes
                  w = 0
                  temp_row.append(w)
            N24.append(temp_row)
##
N25=[]
for l in range(1,n+d+1):  #(lambda nodes)
    for q in range(2):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
            N25.append(temp_row)            
for i in range(len(N21)):
    concatenated_row5 = N21[i] + N22[i] + N23[i] + N24[i]+N25[i]  
    W12.append(concatenated_row5)   
###
N26=[]       
for l in range(1,n+d+1):  #(gamma nodes):
        temp_row = []
        for j in range(1,d+1):
                w = 0
                temp_row.append(w)
        N26.append(temp_row)
N27=[]       
for l in range(1,n+d+1):  #(gamma nodes):
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                temp_row.append(w)
            N27.append(temp_row)
##
N28=[]
for i in range(1,n+d+1):  #(gamma nodes):
            temp_row = []
            for l in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  if l <= i:
                      if m==0:
                        w = 1
                      else:
                        w = -1
                  temp_row.append(w)
            N28.append(temp_row)
##
N29=[]
for l in range(1,n+d+1):  #(gamma nodes):
            temp_row = []
            for j in range(3*d+1,4*d+1):# insertion nodes
                  w = 0
                  temp_row.append(w)
            N29.append(temp_row)
##
N30=[]
for l in range(1,n+d+1):  #(gamma nodes):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
            N30.append(temp_row)            
for i in range(len(N26)):
    concatenated_row6 = N26[i] + N27[i] + N28[i] + N29[i]+N30[i]  
    W12.append(concatenated_row6)    
#####################################
# insertion 
#####################################    
N31=[]       
for l in range(3*d+1,4*d+1):  #(sai nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
          temp_row = []
          for j in range(1,d+1):
                w = 0
                temp_row.append(w)
          N31.append(temp_row)
N32=[]       
for l in range(3*d+1,4*d+1):  #(sai nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                temp_row.append(w)
            N32.append(temp_row)
##
N33=[]       
for l in range(3*d+1,4*d+1):  #(sai nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
            temp_row = []
            for j in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  temp_row.append(w)
            N33.append(temp_row)
##
N34=[]       
for l in range(3*d+1,4*d+1):  #(sai nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
            temp_row = []
            for j in range(3*d+1,4*d+1):# insertion nodes
                  w = 0
                  if k==j:
                      w= 1 / eps
                  temp_row.append(w)
            N34.append(temp_row)
##
N35=[]       
for l in range(3*d+1,4*d+1):  #(sai nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
            N35.append(temp_row)            
for i in range(len(N31)):
    concatenated_row7 = N31[i] + N32[i] + N33[i] + N34[i]+N35[i]  
    W12.append(concatenated_row7)            
N36=[]       
for l in range(3*d+1,4*d+1):  #(rho nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
          temp_row = []
          for j in range(1,d+1):
                w = 0
                temp_row.append(w)
          N36.append(temp_row)
N37=[]       
for l in range(3*d+1,4*d+1):  #(rho nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                temp_row.append(w)
            N37.append(temp_row)
##
N38=[]       
for l in range(3*d+1,4*d+1):  #(rho nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
            temp_row = []
            for j in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  temp_row.append(w)
            N38.append(temp_row)
##
N39=[]       
for l in range(3*d+1,4*d+1):  #(rho nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
            temp_row = []
            for j in range(3*d+1,4*d+1):# insertion nodes
                  w = 0
                  if k==j:
                      w= -1 / eps
                  temp_row.append(w)
            N39.append(temp_row)
##
N40=[]       
for l in range(3*d+1,4*d+1):  #(rho nodes)
    for k in range(3*d+1,4*d+1):
      for q in range(2):
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  temp_row.append(w)
            N40.append(temp_row)            
for i in range(len(N36)):
    concatenated_row8 = N36[i] + N37[i] + N38[i] + N39[i]+N40[i]  
    W12.append(concatenated_row8)  
###
N41=[]       
for l in range(3*d+1,5*d+1):  #(x_j nodes)
          temp_row = []
          for j in range(1,d+1):
                w = 0
                temp_row.append(w)
          N41.append(temp_row)
N42=[]       
for l in range(3*d+1,5*d+1):  #(x_j nodes)
            temp_row = []
            for j in range(d+1,2*d+1):
                w = 0
                temp_row.append(w)
            N42.append(temp_row)
##
N43=[]       
for l in range(3*d+1,5*d+1):  #(x_j nodes)
            temp_row = []
            for j in range(1,n+d+1):#deletion nodes
                for m in range(2):
                  w = 0
                  temp_row.append(w)
            N43.append(temp_row)
##
N44=[]       
for l in range(3*d+1,5*d+1):  #(x_j nodes)
            temp_row = []
            for j in range(3*d+1,4*d+1):# insertion nodes
                  w = 0
                  temp_row.append(w)
            N44.append(temp_row)
##
N45=[]       
for l in range(3*d+1,5*d+1):  #(x_j nodes)
            temp_row = []
            for j in range(3*d+1,5*d+1):
                  w = 0
                  if l==j:
                      w=1
                  temp_row.append(w)
            N45.append(temp_row)            
for i in range(len(N41)):
    concatenated_row9 = N41[i] + N42[i] + N43[i] + N44[i]+N45[i]  
    W12.append(concatenated_row9)      
#print(W12)

#Bias matrix for twelveth hidden layer

B12 = []
# base for substitution nodes

for l in range(1,n+d+1):
    for k in range(1,d+1):
        for m in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if m==0:
                    b = -l / eps +1
                else:
                    b= -l / eps
                temp_row.append(b)
            B12.append(temp_row)

for l in range(1,n+d+1):
    for k in range(1,d+1):
        for m in range(2):
            temp_row = []
            for j in range(1):
                b = 0
                if m==0:
                    b = l / eps +1
                else:
                    b= l / eps
                temp_row.append(b)
            B12.append(temp_row)

for l in range(d+1, 2 * d+1):
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B12.append(temp_row)
###
# base for deletion nodes
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for l in range(1):
            b = 0
            if m == 0:
                b = 1
            temp_row.append(b)
        B12.append(temp_row)
##
for i in range(1,n+d+1):
    for m in range(2):
        temp_row = []
        for l in range(1):
            b = 0
            if m == 0:
                b = 1
            temp_row.append(b)
        B12.append(temp_row)
##
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1):
        b = 0
        temp_row.append(b)
    B12.append(temp_row)  
######
# bias for insertion nodes

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
            B12.append(temp_row)

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
            B12.append(temp_row)           

#(bias of x_{j} as identity function)

for k in range(3*d+1, (5*d)+1):
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B12.append(temp_row)      
# for i in B12:
#     print(i)      
    
L12 = [] 
for i in range(len(W12)):
    L12_i_entry =np.maximum( (np.dot(W12[i], L11)+B12[i]),0)   
    L12.append(L12_i_entry)
    # print('this is index i:', i)
    # print('this is the value L12[i]:', L12_i_entry)
    
# print('twelveth hidden layer')
# for i in L12:
#     print(i)
    
#To construct the weight matrix for thirteenth hidden layer process is L13=W13*L12+B13
W13 = []
# Substitution nodes
P1 = []# calculate lambda and Alpha nodes
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1):
        for k in range(1,d+1):
          for q in range(2):
              w = 0
              if i == l:
                  if q == 0:
                    w = -C
                  else: # q = 1
                    w = C
              temp_row.append(w)
    P1.append(temp_row)
#print(P1)    
##
P2 = []# calculate lambda and beta nodes
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1):
        for k in range(1,d+1):
          for q in range(2):
              w = 0
              if i == l:
                  if q == 0:
                    w = -C
                  else: # q = 1
                    w = C
              temp_row.append(w)
    P2.append(temp_row)  
##
P3 = []# calculate lambda and x_j+d nodes
for i in range(1,n+d+1):
    temp_row = []
    for k in range(d+1, 2 * d+1):
        w = 0
        temp_row.append(w)
    P3.append(temp_row)          
##
P4 = []# lambda nodes
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1):# Deletion nodes
        for q in range(2):
              w = 0
              temp_row.append(w)
    P4.append(temp_row)
##
P5 = []# lambda nodes
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1):# Deletion nodes
        for q in range(2):
              w = 0
              temp_row.append(w)
    P5.append(temp_row)  
##
P6 = []# lambda nodes
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1):# Deletion nodes
              w = 0
              temp_row.append(w)
    P6.append(temp_row)    
##
P7 = []
for i in range(1,n+d+1):
    temp_row = []
    for l in range(3*d+1,4*d+1):# insertion nodes
        for k in range(3*d+1,4*d+1):
            for q in range(2):
              w = 0
              temp_row.append(w)
    P7.append(temp_row)  
##
P8 = []
for i in range(1,n+d+1):
    temp_row = []
    for l in range(3*d+1,4*d+1):# insertion nodes
        for k in range(3*d+1,4*d+1):
            for q in range(2):
              w = 0
              temp_row.append(w)
    P8.append(temp_row)    
# num_rows = len(P1)
# num_columns = len(P1[0])  # Assumes all rows have the same number of columns

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)      
#
P9 = []
for i in range(1,n+d+1):
    temp_row = []
    for k in range(3*d+1, 5*d+1):
        w = 0
        temp_row.append(w)
    P9.append(temp_row) 
for i in range(len(P1)):
    concatenated_row1 = P1[i] + P2[i] + P3[i]+P4[i] + P5[i] + P6[i]+ P7[i]+ P8[i]+ P9[i]
    W13.append(concatenated_row1)
# num_rows = len(W13)
# num_columns = len(W13[0])  # Assumes all rows have the same number of columns

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)    
##
P10 = []# calculate mu and Alpha nodes
for i in range(1,n+d+1):
    for j in range(1,d+1):
      temp_row = []
      for l in range(1,n+d+1):
        for k in range(1,d+1):
          for q in range(2):
              w = 0
              if i == l and j==k:
                  if q == 0:
                    w = C
                  else: # q = 1
                    w = -C
              temp_row.append(w)
      P10.append(temp_row)
#print(P10)    
##
P11 = []# calculate mu and beta nodes
for i in range(1,n+d+1):
    for j in range(1,d+1):
      temp_row = []
      for l in range(1,n+d+1):
        for k in range(1,d+1):
          for q in range(2):
              w = 0
              if i == l and j==k:
                  if q == 0:
                    w = C
                  else: # q = 1
                    w =-C
              temp_row.append(w)
      P11.append(temp_row)  
##
P12 = []# calculate mu and x_j+d nodes
for i in range(1,n+d+1):
    for j in range(1,d+1):
          temp_row = []
          for k in range(d+1, 2 * d+1):
              w = 0
              if k==j+d:
                 w=1
              temp_row.append(w)
          P12.append(temp_row)          
##
P13 = []#mu nodes
for l in range(1,n+d+1):# Deletion nodes
    for j in range(1,d+1):
        temp_row = []
        for j in range(1,n+d+1):# Deletion nodes
                w = 0
                temp_row.append(w)
        P13.append(temp_row)
##
P14 = []# mu nodes
for l in range(1,n+d+1):# mu nodes
    for j in range(1,d+1):
        temp_row = []
        for j in range(1,n+d+1):# Deletion nodes
          for k in range (2):
              w = 0
              temp_row.append(w)
        P14.append(temp_row)  
##
P15 = []# mu nodes
for l in range(1,n+d+1):# mu nodes
    for j in range(1,d+1):
        temp_row = []
        for j in range(1,n+d+1):# Deletion nodes
          for k in range (2):
              w = 0
              temp_row.append(w)
        P15.append(temp_row)    
##
P16 = []# mu nodes
for l in range(1,n+d+1):
    for j in range(1,d+1):
        temp_row = []
        for l in range(3*d+1,4*d+1):# insertion nodes
          for k in range(3*d+1,4*d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
        P16.append(temp_row)  
##
P17 = []# mu nodes
for l in range(1,n+d+1):
    for j in range(1,d+1):
        temp_row = []
        for j in range(3*d+1,4*d+1):# insertion nodes
          for k in range(3*d+1,4*d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
        P17.append(temp_row)         
##
P18 = []# mu nodes
for l in range(1,n+d+1):
    for j in range(1,d+1):
        temp_row = []
        for j in range(3*d+1,5*d+1):# insertion nodes
                w = 0
                temp_row.append(w)
        P18.append(temp_row) 
# num_rows = len(P18)
# num_columns = len(P18[0])  # Assumes all rows have the same number of columns

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)       
for i in range(len(P10)):
    concatenated_row2 = P10[i] + P11[i] + P12[i]+P13[i] + P14[i] + P15[i]+ P16[i] + P17[i]+ P18[i]
    W13.append(concatenated_row2)    
#####################
#deletion nodes
#####################
P19 = []
for i in range(1,n+d+1):# tau nodes
      temp_row = []
      for l in range(1,n+d+1):# alpha nodes
          for k in range(1,d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
      P19.append(temp_row)
##
P20 = []
for i in range(1,n+d+1):# tau nodes
      temp_row = []
      for l in range(1,n+d+1):# beta nodes
          for k in range(1,d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
      P20.append(temp_row)  
##
P21 = []
for i in range(1,n+d+1):# tau nodes
      temp_row = []
      for l in range(d+1,2*d+1):# x_j+d nodes
                w = 0
                temp_row.append(w)
      P21.append(temp_row)         
##
P22 = []
for i in range(1,n+d+1):# tau nodes
          temp_row = []
          for l in range(1,n+d+1):# Deletion nodes
              for q in range(2):
                  w = 0
                  if i==l:
                      if q==0:
                          w=-C
                      else:
                          w=C 
                  temp_row.append(w)
          P22.append(temp_row)

##
P23 = []
for i in range(1,n+d+1):# tau nodes
          temp_row = []
          for l in range(1,n+d+1):# Deletion nodes
              for q in range(2):
                  w = 0
                  if i==l:
                      if q==0:
                          w=-C
                      else:
                          w=C 
                  temp_row.append(w)
          P23.append(temp_row)  
##
P24 = []
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1):# Deletion nodes
              w = 0
              if i==l:
                  w=B
              temp_row.append(w)
    P24.append(temp_row) 
##   
P25 = []
for i in range(1,n+d+1):
      temp_row = []
      for l in range(3*d+1,4*d+1):# insertion nodes
          for k in range(3*d+1,4*d+1):
            for q in range(2):
              w = 0
              temp_row.append(w)
      P25.append(temp_row)  
##
P26 = []
for i in range(1,n+d+1):# tau nodes
      temp_row = []
      for l in range(3*d+1,4*d+1):# insertion nodes
          for k in range(3*d+1,4*d+1):
            for q in range(2):
                w = 0
                temp_row.append(w)
      P26.append(temp_row)    
##
P27 = []
for i in range(1,n+d+1):# tau nodes
      temp_row = []
      for k in range(3*d+1, 5*d+1):# insertion nodes
          w = 0
          temp_row.append(w)
      P27.append(temp_row) 
for i in range(len(P19)):
    concatenated_row3 = P19[i] + P20[i] + P21[i]+P22[i] + P23[i] + P24[i]+ P25[i] + P26[i]+ P27[i]
    W13.append(concatenated_row3) 
#####################
#  insertion nodes  #
#####################
P28 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
      temp_row = []
      for l in range(1,n+d+1):# alpha nodes
          for k in range(1,d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
      P28.append(temp_row)
##
P29 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
      temp_row = []
      for l in range(1,n+d+1):# beta nodes
          for k in range(1,d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
      P29.append(temp_row)  
##
P30 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
      temp_row = []
      for l in range(d+1,2*d+1):# x_j+d nodes
                w = 0
                temp_row.append(w)
      P30.append(temp_row)         
##
P31 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
          temp_row = []
          for l in range(1,n+d+1):# Deletion nodes
              for q in range(2):
                  w = 0
                  temp_row.append(w)
          P31.append(temp_row)

##
P32 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
          temp_row = []
          for l in range(1,n+d+1):# Deletion nodes
              for q in range(2):
                  w = 0
                  temp_row.append(w)
          P32.append(temp_row)  
##
P33 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
      temp_row = []
      for l in range(1,n+d+1):# Deletion nodes
              w = 0
              temp_row.append(w)
      P33.append(temp_row) 
##   
P34 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
      temp_row = []
      for l in range(3*d+1,4*d+1):# insertion nodes
          for k in range(3*d+1,4*d+1):
            for q in range(2):
              w = 0
              if i==l and j==k:
                  if q==0:
                      w=C
                  else:
                      w=-C
              temp_row.append(w)
      P34.append(temp_row) 
P35 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
      temp_row = []
      for l in range(3*d+1,4*d+1):# insertion nodes
          for k in range(3*d+1,4*d+1):
            for q in range(2):
              w = 0
              if i==l and j==k:
                  if q==0:
                      w=C
                  else:
                      w=-C
              temp_row.append(w)
      P35.append(temp_row)       
##
P36 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
      temp_row = []
      for l in range(3*d+1,4*d+1):# insertion nodes
              w = 0
              if j==l:
                  w=1
              temp_row.append(w)
      P36.append(temp_row)   
##
P37 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(3*d+1,4*d+1):
      temp_row = []
      for k in range(4*d+1, 5*d+1):# insertion nodes
          w = 0
          temp_row.append(w)
      P37.append(temp_row) 
for i in range(len(P28)):
    concatenated_row4 = P28[i] + P29[i] + P30[i]+P31[i] + P32[i] + P33[i]+ P34[i] + P35[i]+ P36[i]+ P37[i]
    W13.append(concatenated_row4)   
########
P38 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
      temp_row = []
      for l in range(1,n+d+1):# alpha nodes
          for k in range(1,d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
      P38.append(temp_row)
##
P39 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
      temp_row = []
      for l in range(1,n+d+1):# beta nodes
          for k in range(1,d+1):
              for q in range(2):
                w = 0
                temp_row.append(w)
      P39.append(temp_row)  
##
P40 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
      temp_row = []
      for l in range(d+1,2*d+1):# x_j+d nodes
                w = 0
                temp_row.append(w)
      P40.append(temp_row)         
##
P41 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
          temp_row = []
          for l in range(1,n+d+1):# Deletion nodes
              for q in range(2):
                  w = 0
                  temp_row.append(w)
          P41.append(temp_row)

##
P42 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
          temp_row = []
          for l in range(1,n+d+1):# Deletion nodes
              for q in range(2):
                  w = 0
                  temp_row.append(w)
          P42.append(temp_row)  
##
P43 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
      temp_row = []
      for l in range(1,n+d+1):# Deletion nodes
              w = 0
              temp_row.append(w)
      P43.append(temp_row) 
##   
P44 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
      temp_row = []
      for l in range(3*d+1,4*d+1):# insertion nodes
          for k in range(3*d+1,4*d+1):
            for q in range(2):
              w = 0
              if i==l and j==k+d:
                  if q==0:
                      w=C
                  else:
                      w=-C
              temp_row.append(w)
      P44.append(temp_row)  
##
P45 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
      temp_row = []
      for l in range(3*d+1,4*d+1):# insertion nodes
          for k in range(3*d+1,4*d+1):
            for q in range(2):
              w = 0
              if i==l and j==k+d:
                  if q==0:
                      w=C
                  else:
                      w=-C
              temp_row.append(w)
      P45.append(temp_row)   
##
P46 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
      temp_row = []
      for k in range(3*d+1, 4*d+1):# insertion nodes
          w = 0
          temp_row.append(w)
      P46.append(temp_row) 
##
P47 = []
for i in range(3*d+1,4*d+1):# chi nodes
    for j in range(4*d+1,5*d+1):
      temp_row = []
      for k in range(4*d+1, 5*d+1):# insertion nodes
          w = 0
          if j==k:
              w=1
          temp_row.append(w)
      P47.append(temp_row)       
for i in range(len(P38)):
    concatenated_row5 = P38[i] + P39[i]+P40[i] + P41[i] + P42[i]+ P43[i] + P44[i]+ P45[i]+ P46[i]+ P47[i]
    W13.append(concatenated_row5)       
# # print("weight matrix for thirteenth hidden layer")
#print(W13)      
#
##
# Bias matrix for thirteenth hidden layer        
B13 = [] 
#for substitution nodes
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1):
        b = e[i-1]+d*C
        temp_row.append(b)
    B13.append(temp_row) 
##
for i in range(1,n+d+1):
    for j in range(1,d+1): 
      temp_row = []
      for l in range(1):
          b = -2*C
          temp_row.append(b)
      B13.append(temp_row) 
##for deletion nodes
for i in range(1,n+d+1):
      temp_row = []
      for l in range(1):
          b = C
          temp_row.append(b)
      B13.append(temp_row) 
#for insertion nodes
for i in range(3*d+1,4*d+1):
    for j in range(3*d+1,4*d+1): 
      temp_row = []
      for l in range(1):
          b = -2*C
          temp_row.append(b)
      B13.append(temp_row)  
##
for i in range(3*d+1,4*d+1):
    for j in range(4*d+1,5*d+1): 
      temp_row = []
      for l in range(1):
          b = -2*C
          temp_row.append(b)
      B13.append(temp_row)      
# print("bias of layer hidden 4")
# for i in B13:
#     print (i)        

L13 = [] # Lambda and Mu nodes
for i in range(len(W13)):
    L13_i_entry =np.maximum( (np.dot(W13[i], L12)+B13[i]),0)   
    L13.append(L13_i_entry)
    #print('this is index i:', i)
    #print('this is the value L13[i]:', L13_i_entry)    
# print('nodes of thirteenth hidden layer')
# for i in L13:
#     print(i)
# num_rows = len(W13)
# num_columns = len(W13[0])  # Assumes all rows have the same number of columns

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns) 
################
#To construct the weight matrix for fourteenth hidden layer L14=W14*L13+B14
W14 = []
# Substitution nodes
Q1 = []
for i in range(1,n+d+1):#lambda nodes
    temp_row = []
    for l in range(1,n+d+1):#lambda nodes
              w = 0
              if i == l:
                  w=1
              temp_row.append(w)
    Q1.append(temp_row)
#print(Q1)     
##
Q2 = []
for i in range(1,n+d+1):#lambda nodes
    temp_row = []
    for l in range(1, n+d+1): # mu nodes
        for k in range(1,d+1):
          w = 0
          temp_row.append(w)
    Q2.append(temp_row)          
##
Q3 = []
for i in range(1,n+d+1):# lambda nodes
    temp_row = []
    for l in range(1,n+d+1):# Tau nodes(Deletion)
              w = 0
              temp_row.append(w)
    Q3.append(temp_row)  
##
Q4 = []# lambda nodes
for i in range(1,n+d+1):
    temp_row = []
    for l in range(3*d+1,4*d+1):# chi nodes (insertion)
        for k in range(3*d+1,4*d+1):
              w = 0
              temp_row.append(w)
    Q4.append(temp_row)  
##
Q5 = []
for i in range(1,n+d+1):# lambda nodes
    temp_row = []
    for l in range(3*d+1,4*d+1):# chi nodes (insertion)
        for k in range(4*d+1,5*d+1):
              w = 0
              temp_row.append(w)
    Q5.append(temp_row)        
##
for i in range(len(Q1)):
    concatenated_row1 = Q1[i] + Q2[i]+ Q3[i]+ Q4[i]+ Q5[i]
    W14.append(concatenated_row1)
# num_rows = len(W14)
# num_columns = len(W14[0])  # Assumes all rows have the same number of columns

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)      
# ###############
Q6 = []
for i in range(1,n+d+1):#gamma nodes
    temp_row = []
    for l in range(1,n+d+1):#lambda nodes
              w = 0
              temp_row.append(w)
    Q6.append(temp_row)
#print(Q6)     
##
Q7 = []
for i in range(1,n+d+1):#gamma nodes
    temp_row = []
    for l in range(1, n+d+1): # mu nodes
        for k in range(1,d+1):
          w = 0
          if i==l:
              w=1
          temp_row.append(w)
    Q7.append(temp_row)          
##
Q8 = []
for i in range(1,n+d+1):# gamma nodes
    temp_row = []
    for l in range(1,n+d+1):# Tau nodes(Deletion)
              w = 0
              temp_row.append(w)
    Q8.append(temp_row)  
##
Q9 = []
for i in range(1,n+d+1):#gamma nodes
    temp_row = []
    for l in range(3*d+1,4*d+1):# chi nodes (insertion)
        for k in range(3*d+1,4*d+1):
              w = 0
              temp_row.append(w)
    Q9.append(temp_row)  
##
Q10 = []
for i in range(1,n+d+1):# gamma nodes
    temp_row = []
    for l in range(3*d+1,4*d+1):# chi nodes (insertion)
        for k in range(4*d+1,5*d+1):
              w = 0
              temp_row.append(w)
    Q10.append(temp_row)        
##
for i in range(len(Q6)):
    concatenated_row2 = Q6[i] + Q7[i]+ Q8[i]+ Q9[i]+ Q10[i]
    W14.append(concatenated_row2)  
###################
# deletion nodes
####################
Q11 = []
for i in range(1,n+d+1-d):#sai nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(1,n+d+1):#lambda nodes
              w = 0
              temp_row.append(w)
          Q11.append(temp_row)
#print(Q11)     
##
Q12 = []
for i in range(1,n+d+1-d):#sai nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(1, n+d+1): # mu nodes
              for k in range(1,d+1):
                w = 0
                temp_row.append(w)
          Q12.append(temp_row)          
##
Q13 = []
for i in range(1,n+d+1-d):#sai nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(1,n+d+1):# Tau nodes(Deletion)
              w = 0
              if i+j-1==l:
                  w=1 / eps
              temp_row.append(w)
          Q13.append(temp_row)  
##
Q14 = []
for i in range(1,n+d+1-d):#sai nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(3*d+1,4*d+1):# chi nodes (insertion)
            for k in range(3*d+1,4*d+1):
                w = 0
                temp_row.append(w)
          Q14.append(temp_row)  
##
Q15 = []
for i in range(1,n+d+1-d):#sai nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(3*d+1,4*d+1):# chi nodes (insertion)
            for k in range(4*d+1,5*d+1):
                w = 0
                temp_row.append(w)
          Q15.append(temp_row)        
##
for i in range(len(Q11)):
    concatenated_row3 = Q11[i] + Q12[i]+ Q13[i]+ Q14[i]+ Q15[i]
    W14.append(concatenated_row3)   
###
Q16 = []
for i in range(1,n+d+1-d):#rho nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(1,n+d+1):#lambda nodes
              w = 0
              temp_row.append(w)
          Q16.append(temp_row)
#print(Q16)     
##
Q17 = []
for i in range(1,n+d+1-d):#rho nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(1, n+d+1): # mu nodes
              for k in range(1,d+1):
                w = 0
                temp_row.append(w)
          Q17.append(temp_row)          
##
Q18 = []
for i in range(1,n+d+1-d):#rho nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(1,n+d+1):# Tau nodes(Deletion)
              w = 0
              if i+j-1==l:
                  w= -1 / eps
              temp_row.append(w)
          Q18.append(temp_row)  
##
Q19 = []
for i in range(1,n+d+1-d):#rho nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(3*d+1,4*d+1):# chi nodes (insertion)
            for k in range(3*d+1,4*d+1):
                w = 0
                temp_row.append(w)
          Q19.append(temp_row)  
##
Q20 = []
for i in range(1,n+d+1-d):#rho nodes
    for j in range(1,d+2):
        for q in range(2):
          temp_row = []
          for l in range(3*d+1,4*d+1):# chi nodes (insertion)
            for k in range(4*d+1,5*d+1):
                w = 0
                temp_row.append(w)
          Q20.append(temp_row)        
##
for i in range(len(Q16)):
    concatenated_row4 = Q16[i] + Q17[i]+ Q18[i]+ Q19[i]+ Q20[i]
    W14.append(concatenated_row4)  
###################
# Insertion nodes
####################
Q21 = []
for i in range(3*d+1,4*d+1):#x_j prime nodes
          temp_row = []
          for l in range(1,n+d+1):#lambda nodes
              w = 0
              temp_row.append(w)
          Q21.append(temp_row)
#print(Q21)     
##
Q22 = []
for i in range(3*d+1,4*d+1):#x_j prime nodes
          temp_row = []
          for l in range(1, n+d+1): # mu nodes
              for k in range(1,d+1):
                w = 0
                temp_row.append(w)
          Q22.append(temp_row)          
##
Q23 = []
for i in range(3*d+1,4*d+1):#x_j prime nodes
          temp_row = []
          for l in range(1,n+d+1):# Tau nodes(Deletion)
              w = 0
              temp_row.append(w)
          Q23.append(temp_row)  
##
Q24 = []
for i in range(3*d+1,4*d+1):#x_j prime nodes
          temp_row = []
          for l in range(3*d+1,4*d+1):# chi nodes (insertion)
            for k in range(3*d+1,4*d+1):
                w = 0
                if i==l:
                    w=1
                temp_row.append(w)
          Q24.append(temp_row)  
##
Q25 = []
for i in range(3*d+1,4*d+1):#x_j prime nodes
          temp_row = []
          for l in range(3*d+1,4*d+1):# chi nodes (insertion)
            for k in range(4*d+1,5*d+1):
                w = 0
                temp_row.append(w)
          Q25.append(temp_row)        
##
for i in range(len(Q21)):
    concatenated_row4 = Q21[i] + Q22[i]+ Q23[i]+ Q24[i]+ Q25[i]
    W14.append(concatenated_row4)   
###
Q26 = []
for i in range(4*d+1,5*d+1):#x_j+d prime nodes
          temp_row = []
          for l in range(1,n+d+1):#lambda nodes
              w = 0
              temp_row.append(w)
          Q26.append(temp_row)
#print(Q26)     
##
Q27 = []
for i in range(4*d+1,5*d+1):#x_j+d prime nodes
          temp_row = []
          for l in range(1, n+d+1): # mu nodes
              for k in range(1,d+1):
                w = 0
                temp_row.append(w)
          Q27.append(temp_row)          
##
Q28 = []
for i in range(4*d+1,5*d+1):#x_j+d prime nodes
          temp_row = []
          for l in range(1,n+d+1):# Tau nodes(Deletion)
              w = 0
              temp_row.append(w)
          Q28.append(temp_row)  
##
Q29 = []
for i in range(4*d+1,5*d+1):#x_j+d prime nodes
          temp_row = []
          for l in range(3*d+1,4*d+1):# chi nodes (insertion)
            for k in range(3*d+1,4*d+1):
                w = 0
                temp_row.append(w)
          Q29.append(temp_row)  
##
Q30 = []
for i in range(4*d+1,5*d+1):#x_j+d prime nodes
          temp_row = []
          for l in range(3*d+1,4*d+1):# chi nodes (insertion)
            for k in range(4*d+1,5*d+1):
                w = 0
                if i==l+d:
                    w=1              
                temp_row.append(w)
          Q30.append(temp_row)
##
for i in range(len(Q26)):
    concatenated_row5 = Q26[i]+ Q27[i]+ Q28[i]+ Q29[i]+ Q30[i]
    W14.append(concatenated_row5)     
# print("weight matrix for  fourteenth hidden layer")
# print(W14)
# ##
# #Bias matrix for fourteenth hidden layer
B14 = []

for i in range(1,n+d+1):
    temp_row = []
    for l in range(1):
        b = 0
        temp_row.append(b)
    B14.append(temp_row)
##
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1):
        b = 0
        temp_row.append(b)
    B14.append(temp_row)    

  ## for deletion nodes
for i in range(1,n+d+1-d):#sai nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2):
          temp_row = []
          for l in range(1):
            b = 0
            if q==0:
                b = -i*B / eps+1
            else:    
                b = -i*B / eps 
            temp_row.append(b)
          B14.append(temp_row) 
##
for i in range(1,n+d+1-d):#rho nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2):
          temp_row = []
          for l in range(1):
              b = 0
              if q==0:
                    b = (i*B+1) / eps+1
              else:    
                    b = (i*B+1) / eps 
              temp_row.append(b)
          B14.append(temp_row) 
## for insertion nodes
for i in range(3*d+1,4*d+1):
    temp_row = []
    for l in range(1):
        b = 0
        temp_row.append(b)
    B14.append(temp_row)
##
for i in range(4*d+1,5*d+1):
    temp_row = []
    for l in range(1):
        b = 0
        temp_row.append(b)
    B14.append(temp_row)       

# #print("bias of fourteenth hidden layer")
# #for i in B5:
# #    print(i) 
    
L14 = [] 
for i in range(len(W14)):
    L14_i_entry = np.maximum( (np.dot(W14[i], L13)+B14[i]),0)     
    L14.append(L14_i_entry)
#     #print('this is index i:', i)
# #    print('this is the value L14[i]:', L14_i_entry)
# print("nodes of fourteenth hidden layer")  
# for i in L14:
#     print(i)   
#To construct the weight matrix for fifteenth hidden layer is L15=W15*L14+B15  
W15 = [] 
## substitution nodes
R1=[]
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1):
        w = 0
        if l==i:
          w = 1
        temp_row.append(w)
    R1.append(temp_row)
##
R2=[]
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1):
        w = 0
        if l==i:
          w = 1
        temp_row.append(w)
    R2.append(temp_row)
    
##
R3=[]
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1-d):# deletion nodes(sai nodes)
        for k in range(2*d+1,3*d+2):
            for m in range (2):
                w = 0
                temp_row.append(w)
    R3.append(temp_row)
##
R4=[]
for i in range(1,n+d+1):
    temp_row = []
    for l in range(1,n+d+1-d):#deletion nodes(rho nodes)
        for k in range(2*d+1,3*d+2):
            for m in range (2):
                w = 0
                temp_row.append(w)
    R4.append(temp_row)    
##
R5=[]
for i in range(1,n+d+1):
    temp_row = []
    for l in range(3*d+1,4*d+1):#insertion nodes(x'_j nodes)
                w = 0
                temp_row.append(w)
    R5.append(temp_row) 
##
R6=[]
for i in range(1,n+d+1):
    temp_row = []
    for l in range(4*d+1,5*d+1):#insertion nodes(x'_j+d nodes)
                w = 0
                temp_row.append(w)
    R6.append(temp_row)
for i in range(len(R1)):
    concatenated_row1 = R1[i] + R2[i] + R3[i] + R4[i] + R5[i] + R6[i]
    W15.append(concatenated_row1)
# num_rows = len(W14)
# num_columns = len(W14[0])  # Assumes all rows have the same number of columns

# print("Number of rows:", num_rows)
# print("Number of columns:", num_columns)           
## Deletion nodes(identity map)
R7=[]
for i in range(1,n+d+1-d):# sai nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1,n+d+1): #substitution nodes(lambda nodes)
            w = 0
            temp_row.append(w)
          R7.append(temp_row)
##
R8=[]
for i in range(1,n+d+1-d):
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1,n+d+1): #substitution nodes(lambda nodes)
            w = 0
            temp_row.append(w)
          R8.append(temp_row)        
##
R9=[]
for i in range(1,n+d+1-d):# sai nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1,n+d+1-d):# deletion nodes(sai nodes)
            for k in range(2*d+1,3*d+2):
                for m in range (2):
                  w = 0
                  if i==l and j==k and q==m:
                        w=1
                  temp_row.append(w)
          R9.append(temp_row)
##
R10=[]
for i in range(1,n+d+1-d):# sai nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1,n+d+1-d):# deletion nodes(rho nodes)
            for k in range(2*d+1,3*d+2):
                for m in range (2):
                  w = 0
                  temp_row.append(w)
          R10.append(temp_row) 
##
R11=[]
for i in range(1,n+d+1-d):# sai nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2):
          temp_row = []
          for l in range(3*d+1,4*d+1):#insertion nodes(x'_j nodes)
                w = 0
                temp_row.append(w)
          R11.append(temp_row) 
##
R12=[]
for i in range(1,n+d+1-d):# sai nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2):
          temp_row = []
          for l in range(4*d+1,5*d+1):#insertion nodes(x'_j nodes)
                w = 0
                temp_row.append(w)
          R12.append(temp_row)
for i in range(len(R7)):
    concatenated_row2 = R7[i] + R8[i] + R9[i] + R10[i] + R11[i] + R12[i]
    W15.append(concatenated_row2) 
#######
R13=[]
for i in range(1,n+d+1-d):# roh nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1,n+d+1): #substitution nodes(lambda nodes)
            w = 0
            temp_row.append(w)
          R13.append(temp_row)
##
R14=[]
for i in range(1,n+d+1-d):
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1,n+d+1): #substitution nodes(lambda nodes)
            w = 0
            temp_row.append(w)
          R14.append(temp_row)        
##
R15=[]
for i in range(1,n+d+1-d):# rho nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1,n+d+1-d):# deletion nodes(sai nodes)
            for k in range(2*d+1,3*d+2):
                for m in range (2):
                  w = 0
                  temp_row.append(w)
          R15.append(temp_row)
##
R16=[]
for i in range(1,n+d+1-d):# rho nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1,n+d+1-d):# deletion nodes(rho nodes)
            for k in range(2*d+1,3*d+2):
                for m in range (2):
                  w = 0
                  
                  if i==l and j==k and q==m:
                        w=1
                  temp_row.append(w)
          R16.append(temp_row) 
##
R17=[]
for i in range(1,n+d+1-d):# rho nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2):
          temp_row = []
          for l in range(3*d+1,4*d+1):#insertion nodes(x'_j nodes)
                w = 0
                temp_row.append(w)
          R17.append(temp_row) 
##
R18=[]
for i in range(1,n+d+1-d):# rho nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2):
          temp_row = []
          for l in range(4*d+1,5*d+1):#insertion nodes(x'_j nodes)
                w = 0
                temp_row.append(w)
          R18.append(temp_row)
for i in range(len(R13)):
    concatenated_row3 = R13[i] + R14[i] + R15[i] + R16[i] + R17[i] + R18[i]
    W15.append(concatenated_row3)     
## insertion nodes
R19=[]
for i in range(1,n+2):
    for j in range(3*d+1,4*d+1):
      for q in range(2):
          temp_row = []
          for l in range(1,n+d+1): #substitution nodes(lambda nodes)
            w = 0
            temp_row.append(w)
          R19.append(temp_row)
##
R20=[]
for i in range(1,n+2): # alpha 1 and alpha 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
        temp_row = []
        for l in range(1,n+d+1):#substitution nodes(gamma nodes)
            w = 0
            temp_row.append(w)
        R20.append(temp_row)        
##
R21=[]
for i in range(1,n+2): # alpha 1 and alpha 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
        temp_row = []
        for l in range(1,n+d+1-d):# deletion nodes(sai nodes)
          for k in range(2*d+1,3*d+2):
            for m in range (2):
                w = 0
                temp_row.append(w)
        R21.append(temp_row)
##
R22=[]
for i in range(1,n+2): # alpha 1 and alpha 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
          temp_row = []
          for l in range(1,n+d+1-d):# deletion nodes(rho nodes)
            for k in range(2*d+1,3*d+2):
              for m in range (2):
                w = 0
                temp_row.append(w)
          R22.append(temp_row)  
##
R23=[]
for i in range(1,n+2): # alpha 1 and alpha 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
          temp_row = []
          for l in range(3*d+1,4*d+1):#insertion nodes(x'_j nodes)
                w = 0
                if j==l:
                        w=1 / eps
                temp_row.append(w)
          R23.append(temp_row) 
##
R24=[]
for i in range(1,n+2): # alpha 1 and alpha 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
        temp_row = []
        for l in range(4*d+1,5*d+1):#insertion nodes(x'_j+d nodes)
                w = 0
                temp_row.append(w)
        R24.append(temp_row)
for i in range(len(R19)):
    concatenated_row3 =  R19[i] + R20[i] + R21[i] + R22[i] + R23[i]+ R24[i]
    W15.append(concatenated_row3)    
###
R25=[]
for i in range(1,n+2):# beta1 and beta2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
          temp_row = []
          for l in range(1,n+d+1): #substitution nodes(lambda nodes)
            w = 0
            temp_row.append(w)
          R25.append(temp_row)
##
R26=[]
for i in range(1,n+2):
    for j in range(3*d+1,4*d+1):
      for q in range(2):
        temp_row = []
        for l in range(1,n+d+1):#substitution nodes(gamma nodes)
            w = 0
            temp_row.append(w)
        R26.append(temp_row)        
##
R27=[]
for i in range(1,n+2): # beta 1 and beta 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
        temp_row = []
        for l in range(1,n+d+1-d):# deletion nodes(sai nodes)
          for k in range(2*d+1,3*d+2):
            for m in range (2):
                w = 0
                temp_row.append(w)
        R27.append(temp_row)
##
R28=[]
for i in range(1,n+2): # beta 1 and beta 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
          temp_row = []
          for l in range(1,n+d+1-d):# deletion nodes(rho nodes)
            for k in range(2*d+1,3*d+2):
              for m in range (2):
                w = 0
                temp_row.append(w)
          R28.append(temp_row)  
##
R29=[]
for i in range(1,n+2): # beta 1 and beta 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
          temp_row = []
          for l in range(3*d+1,4*d+1):#insertion nodes(x'_j nodes)
                w = 0
                if j==l:
                        w=-1 / eps
                temp_row.append(w)
          R29.append(temp_row) 
##
R30=[]
for i in range(1,n+2): # beta 1 and beta 2 nodes
    for j in range(3*d+1,4*d+1):
      for q in range(2):
        temp_row = []
        for l in range(4*d+1,5*d+1):#insertion nodes(x'_j+d nodes)
                w = 0
                temp_row.append(w)
        R30.append(temp_row)
for i in range(len(R25)):
    concatenated_row4 = R25[i] + R26[i] + R27[i] + R28[i] + R29[i] + R30[i]
    W15.append(concatenated_row4) 
R31=[]
for i in range(3*d+1,4*d+1):#gamma nodes
          temp_row = []
          for l in range(1,n+d+1): #substitution nodes(lambda nodes)
            w = 0
            temp_row.append(w)
          R31.append(temp_row)
##
R32=[]
for i in range(3*d+1,4*d+1):#gamma nodes
        temp_row = []
        for l in range(1,n+d+1):#substitution nodes(gamma nodes)
            w = 0
            temp_row.append(w)
        R32.append(temp_row)        
##
R33=[]
for i in range(3*d+1,4*d+1):#gamma nodes
        temp_row = []
        for l in range(1,n+d+1-d):# deletion nodes(sai nodes)
          for k in range(2*d+1,3*d+2):
            for m in range (2):
                w = 0
                temp_row.append(w)
        R33.append(temp_row)
##
R34=[]
for i in range(3*d+1,4*d+1):#gamma nodes
          temp_row = []
          for l in range(1,n+d+1-d):# deletion nodes(rho nodes)
            for k in range(2*d+1,3*d+2):
              for m in range (2):
                w = 0
                temp_row.append(w)
          R34.append(temp_row)  
##
R35=[]
for i in range(3*d+1,4*d+1):#gamma nodes
          temp_row = []
          for l in range(3*d+1,4*d+1):#insertion nodes(x'_j nodes)
                w = 0
                if i==l:
                    w=1 
                temp_row.append(w)
          R35.append(temp_row) 
##
R36=[]
for i in range(3*d+1,4*d+1):#gamma nodes
        temp_row = []
        for l in range(4*d+1,5*d+1):#insertion nodes(x'_j+d nodes)
                w = 0
                temp_row.append(w)
        R36.append(temp_row)
for i in range(len(R31)):
    concatenated_row5 = R31[i] + R32[i] + R33[i] + R34[i] + R35[i] + R36[i]
    W15.append(concatenated_row5)  
R37=[]
for i in range(4*d+1,5*d+1):#x_j+d nodes
          temp_row = []
          for l in range(1,n+d+1): #substitution nodes(lambda nodes)
            w = 0
            temp_row.append(w)
          R37.append(temp_row)
##
R38=[]
for i in range(4*d+1,5*d+1):#x_j+d nodes
        temp_row = []
        for l in range(1,n+d+1):#substitution nodes(gamma nodes)
            w = 0
            temp_row.append(w)
        R38.append(temp_row)        
##
R39=[]
for i in range(4*d+1,5*d+1):#x_j+d nodes
        temp_row = []
        for l in range(1,n+d+1-d):# deletion nodes(sai nodes)
          for k in range(2*d+1,3*d+2):
            for m in range (2):
                w = 0
                temp_row.append(w)
        R39.append(temp_row)
##
R40=[]
for i in range(4*d+1,5*d+1):#x_j+d nodes
          temp_row = []
          for l in range(1,n+d+1-d):# deletion nodes(rho nodes)
            for k in range(2*d+1,3*d+2):
              for m in range (2):
                w = 0
                temp_row.append(w)
          R40.append(temp_row)  
##
R41=[]
for i in range(4*d+1,5*d+1):#x_j+d nodes
          temp_row = []
          for l in range(3*d+1,4*d+1):#insertion nodes(x'_j nodes)
                w = 0
                temp_row.append(w)
          R41.append(temp_row) 
##
R42=[]
for i in range(4*d+1,5*d+1):#x_j+d nodesa nodes
        temp_row = []
        for l in range(4*d+1,5*d+1):#insertion nodes(x'_j+d nodes)
                w = 0
                if i==l:
                    w=1
                temp_row.append(w)
        R42.append(temp_row)
for i in range(len(R37)):
    concatenated_row6 = R37[i] + R38[i] + R39[i] + R40[i] + R41[i] + R42[i]
    W15.append(concatenated_row6)     
# print("weight for fifteenth hidden layer")
#print(W15)

#Bias matrix for fifteenth hidden layer
# Substitution nodes
B15 = []
for i in range(1,n+d+1):
    temp_row = []
    for l in range (1):
        b = 0
        temp_row.append(b)
    B15.append(temp_row)
#deletion nodes
for i in range(1,n+d+1-d):# sai nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1): 
            b = 0
            temp_row.append(b)
          B15.append(temp_row)    
##
for i in range(1,n+d+1-d):# rho nodes
    for j in range(2*d+1,3*d+2):
        for q in range(2): 
          temp_row = []
          for l in range(1): 
            b = 0
            temp_row.append(b)
          B15.append(temp_row)    
##
#insertion nodes
for i in range(1,n+2): # alpha 1 and alpha 2 nodes
    for j in range(1,d+1):
      for q in range(2):
          temp_row = []
          for l in range(1):
                  b = 0
                  if q==0:
                      b=-i/eps+1
                  else:
                      b=-i/eps
                  temp_row.append(b)
          B15.append(temp_row)
for i in range(1,n+2): # beta 1 and beta 2 nodes
    for j in range(1,d+1):
      for q in range(2):
          temp_row = []
          for l in range(1):
                  b = 0
                  if q==0:
                      b=i/eps+1
                  else:
                      b=i/eps
                  temp_row.append(b)
          B15.append(temp_row)          
for j in range(1,d+1):#gamma nodes
        temp_row = []
        for l in range(1):
                b = j-1
                temp_row.append(b)
        B15.append(temp_row)
##
for i in range(4*d+1,5*d+1):#x'_j+d nodes
        temp_row = []
        for l in range(1):
                b = 0
                temp_row.append(b)
        B15.append(temp_row)       
e_S = [] # string obtained after the substitution process
for i in range(len(W15)):
    e_S_i_entry = np.maximum((np.dot(W15[i], L14) +B15[i]),0)   
    e_S.append(e_S_i_entry)
    # print('this is index i:', i)
    # print('this is the value e_S[i]:', e_S_i_entry)
# print("Printing e_S nodes after substitution") 
# for i in e_S:  
#         print(i)  
####################################################################################

##To construct the weight matrix for sixteenth hidden layer L16=W16*e_S+B16
W16 = []
#
S1=[]
for i in range(1,n+d+1-d): #Deletion(zeta nodes)
    for j in range(1,d+2):
            temp_row = []
            for l in range(1,n+d+1):#e_S nodes
               w = 0
               if i+j-1 == l:
                   w = 1
               temp_row.append(w)
            S1.append(temp_row)
#
S2=[]
for l in range(1,n+d+1-d): #Deletion(zeta nodes)
    for k in range(2*d+1,3*d+2):
            temp_row = []
            for i in range(1,n+d+1-d):#Deletion nodes
                for j in range(2*d+1,3*d+2):
                    for q in range(2):
                       w = 0
                       if i == l and j==k:
                          if q==0:
                            w = C
                          else:
                            w=-C 
                       temp_row.append(w)
            S2.append(temp_row)
S3=[]
for l in range(1,n+d+1-d):#Deletion(zeta nodes)
    for k in range(2*d+1,3*d+2):
            temp_row = []
            for i in range(1,n+d+1-d):#Deletion nodes
                for j in range(2*d+1,3*d+2):
                    for q in range(2):
                       w = 0
                       if i == l and j==k:
                          if q==0:
                            w = C
                          else:
                            w=-C 
                       temp_row.append(w)
            S3.append(temp_row)
S4=[]
for l in range(1,n+d+1-d):#Deletion(zeta nodes)
    for k in range(2*d+1,3*d+2):
            temp_row = []
            for l in range(1, n+2):#insertion
                for k in range(3*d+1,4*d+1):
                  for q in range(2):
                       w = 0
                       temp_row.append(w)
            S4.append(temp_row)
S5=[]
for l in range(1,n+d+1-d):#Deletion(zeta nodes)
    for k in range(2*d+1,3*d+2):
            temp_row = []
            for l in range(1, n+2):#insertion
                for k in range(3*d+1,4*d+1):
                  for q in range(2):
                       w = 0
                       temp_row.append(w)
            S5.append(temp_row)   
S6=[]
for l in range(1,n+d+1-d):#Deletion(zeta nodes)
    for k in range(2*d+1,3*d+2):
            temp_row = []
            for i in range(3*d+1,4*d+1):
                       w = 0
                       temp_row.append(w)
            S6.append(temp_row)            
S7=[]
for l in range(1,n+d+1-d):#Deletion(zeta nodes)
    for k in range(2*d+1,3*d+2):
            temp_row = []
            for i in range(4*d+1,5*d+1):
                       w = 0
                       temp_row.append(w)
            S7.append(temp_row)
for i in range(len(S1)):
    concatenated_row1 = S1[i] + S2[i] + S3[i] + S4[i] + S5[i] + S6[i]+ S7[i]
    W16.append(concatenated_row1) 
    
##Insertion nodes
S8=[]
for l in range(1,n+2): #Insertion(Tau nodes)
   temp_row = []
   for i in range(1,n+d+1):#e_S nodes
             w = 0
             temp_row.append(w)
   S8.append(temp_row)
S9=[]
for l in range(1,n+2): #Insertion(Tau nodes)
   temp_row = []
   for i in range(1,n+d+1-d):#Deletion nodes
      for j in range(2*d+1,3*d+2):
          for q in range(2):
             w = 0
             temp_row.append(w)
   S9.append(temp_row)
S10=[]
for l in range(1,n+2): #Insertion(Tau nodes)
   temp_row = []
   for i in range(1,n+d+1-d):#Deletion nodes
      for j in range(2*d+1,3*d+2):
          for q in range(2):
             w = 0
             temp_row.append(w)
   S10.append(temp_row)
S11=[]
for i in range(1,n+2): #Insertion(Tau nodes)
         temp_row = []
         for l in range(1, n+2):
             for k in range(3*d+1,4*d+1):
               for q in range(2):
                   w = 0
                   if i == l:
                     if q == 0:
                       w = 1
                     else: # q = 1
                       w = -1
                   temp_row.append(w)
         S11.append(temp_row)
S12=[]
for i in range(1,n+2): #Insertion(Tau nodes)
         temp_row = []
         for l in range(1, n+2):
             for k in range(3*d+1,4*d+1):
               for q in range(2):
                   w = 0
                   if i == l:
                     if q == 0:
                       w = 1
                     else: # q = 1
                       w = -1
                   temp_row.append(w)
         S12.append(temp_row)  
S13=[]
for i in range(1,n+2): #Insertion(Tau nodes)
            temp_row = []
            for i in range(3*d+1,4*d+1):
                       w = 0
                       temp_row.append(w)
            S13.append(temp_row)            
S14=[]
for i in range(1,n+2): #Insertion(Tau nodes)
            temp_row = []
            for i in range(4*d+1,5*d+1):
                       w = 0
                       temp_row.append(w)
            S14.append(temp_row)
for i in range(len(S8)):
    concatenated_row2 = S8[i] + S9[i] + S10[i] + S11[i] + S12[i]+ S13[i] + S14[i]
    W16.append(concatenated_row2)

#####
S15=[]
for l in range(1,n+2): #Insertion(mu nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
          temp_row = []
          for i in range(1,n+d+1):#e_S nodes
                  w = 0
                  temp_row.append(w)
          S15.append(temp_row)  
S16=[]
for l in range(1,n+2): #Insertion(mu nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
          temp_row = []
          for i in range(1,n+d+1-d):#Deletion nodes
             for j in range(2*d+1,3*d+2):
                for q in range(2):
                  w = 0
                  temp_row.append(w)
          S16.append(temp_row)
S17=[]
for l in range(1,n+2): #Insertion(mu nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
          temp_row = []
          for i in range(1,n+d+1-d):#Deletion nodes
             for j in range(2*d+1,3*d+2):
                for q in range(2):
                  w = 0
                  temp_row.append(w)
          S17.append(temp_row)
S18=[]
for l in range(1,n+2): #Insertion(mu nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
         temp_row = []
         for l in range(1, n+2):
             for k in range(3*d+1,4*d+1):
               for q in range(2):
                   w = 0
                   temp_row.append(w)
         S18.append(temp_row)
S19=[]
for l in range(1,n+2): #Insertion(mu nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
         temp_row = []
         for l in range(1, n+2):
             for k in range(3*d+1,4*d+1):
               for q in range(2):
                   w = 0
                   temp_row.append(w)
         S19.append(temp_row)  
S20=[]
for l in range(1,n+2): #Insertion(mu nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
            temp_row = []
            for i in range(3*d+1,4*d+1):
                       w = 0
                       if k==i:
                           w=1/eps
                       temp_row.append(w)
            S20.append(temp_row)            
S21=[]
for l in range(1,n+2): #Insertion(mu nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
            temp_row = []
            for i in range(4*d+1,5*d+1):
                       w = 0
                       temp_row.append(w)
            S21.append(temp_row) 
for i in range(len(S15)):
    concatenated_row3 = S15[i] + S16[i] + S17[i] + S18[i]+S19[i] + S20[i] + S21[i] 
    W16.append(concatenated_row3)   
###
S22=[]
for l in range(1,n+2): #Insertion(lambda nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
          temp_row = []
          for i in range(1,n+d+1):#e_S nodes
                  w = 0
                  temp_row.append(w)
          S22.append(temp_row)
S23=[]
for l in range(1,n+2): #Insertion(lambda nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
          temp_row = []
          for i in range(1,n+d+1-d):#Deletion nodes
             for j in range(2*d+1,3*d+2):
                for q in range(2):
                  w = 0
                  temp_row.append(w)
          S23.append(temp_row)
S24=[]
for l in range(1,n+2): #Insertion(lambda nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
          temp_row = []
          for i in range(1,n+d+1-d):#Deletion nodes
             for j in range(2*d+1,3*d+2):
                for q in range(2):
                  w = 0
                  temp_row.append(w)
          S24.append(temp_row)
S25=[]
for l in range(1,n+2): #Insertion(lambda nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
         temp_row = []
         for l in range(1, n+2):#insertion(alpha nodes)
             for k in range(3*d+1,4*d+1):
               for q in range(2):
                   w = 0
                   temp_row.append(w)
         S25.append(temp_row)
S26=[]
for l in range(1,n+2): #Insertion(lambda nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
         temp_row = []
         for l in range(1, n+2):
             for k in range(3*d+1,4*d+1):
               for q in range(2):
                   w = 0
                   temp_row.append(w)
         S26.append(temp_row)  
S27=[]
for l in range(1,n+2): #Insertion(lambda nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
            temp_row = []
            for i in range(3*d+1,4*d+1):
                       w = 0
                       if k==i:
                           w=-1/eps
                       temp_row.append(w)
            S27.append(temp_row)            
S28=[]
for l in range(1,n+2): #Insertion(lambda nodes)
   for k in range(3*d+1,4*d+1):
       for q in range(2):
            temp_row = []
            for i in range(4*d+1,5*d+1):
                       w = 0
                       temp_row.append(w)
            S28.append(temp_row) 
for i in range(len(S22)):
    concatenated_row4 = S22[i] + S23[i] + S24[i] + S25[i] + S26[i] + S27[i] + S28[i]
    W16.append(concatenated_row4)      
###
S29=[]
for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
          temp_row = []
          for i in range(1,n+d+1):#e_S nodes
                  w = 0
                  temp_row.append(w)
          S29.append(temp_row)
S30=[]
for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
          temp_row = []
          for i in range(1,n+d+1-d):#Deletion nodes
             for j in range(2*d+1,3*d+2):
                for q in range(2):
                  w = 0
                  temp_row.append(w)
          S30.append(temp_row)
S31=[]
for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
          temp_row = []
          for i in range(1,n+d+1-d):#Deletion nodes
             for j in range(2*d+1,3*d+2):
                for q in range(2):
                  w = 0
                  temp_row.append(w)
          S31.append(temp_row)
S32=[]
for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
         temp_row = []
         for l in range(1, n+2):#insertion(alpha nodes)
             for k in range(3*d+1,4*d+1):
               for q in range(2):
                   w = 0
                   temp_row.append(w)
         S32.append(temp_row)
S33=[]
for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
         temp_row = []
         for l in range(1, n+2):
             for k in range(3*d+1,4*d+1):
               for q in range(2):
                   w = 0
                   temp_row.append(w)
         S33.append(temp_row)  
S34=[]
for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
            temp_row = []
            for i in range(3*d+1,4*d+1):
                       w = 0
                       temp_row.append(w)
            S34.append(temp_row)            
S35=[]
for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
            temp_row = []
            for i in range(4*d+1,5*d+1):
                       w = 0
                       if l==i:
                           w=1
                       temp_row.append(w)
            S35.append(temp_row) 
for i in range(len(S29)):
    concatenated_row5 = S29[i] + S30[i] + S31[i] + S32[i] + S33[i] + S34[i] + S35[i]
    W16.append(concatenated_row5) 
# for i in W16:
#     print(i)
###########     
#Bias matrix for sixteenth hidden layer
B16 = []
## (bias of deletion nodes) ##
for i in range(1,n+d+1 - d):# zeta nodes
    for j in range(1,d + 2):
        temp_row = []
        for l in range(1):
            b = -2 * C 
            temp_row.append(np.array(b))
        B16.append(temp_row)
# bias of insertion nodes 
for l in range(1, n+2):#(corresponding to tau nodes)
    temp_row = []
    for k in range(1):
        b = (-d)
        temp_row.append(b)
    B16.append(temp_row)

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
            B16.append(temp_row)
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
            B16.append(temp_row)            
            
for k in range(4*d+1, (5*d)+1):#(corresponding to x'_{l+d} nodes)
    temp_row = []
    for j in range(1):
        b = 0
        temp_row.append(b)
    B16.append(temp_row)
# print(B16)    
L16 = [] 
for i in range(len(W16)):
    temp_row = []
    L16_i_entry =np.maximum( (np.dot(W16[i], e_S)+B16[i]),0)    
    L16.append(L16_i_entry)
    # print('this is index i:', i)
    # print('this is the value L16[i]:', L16_i_entry)   
    
# print('Printing nodes for sixteenth hidden layer')
# for i in L16:
#     print(i)    

# #To construct the weight matrix for seventeenth hidden layer L17=W17*L16+B17
W17 = []

T1=[]
for i in range(1,n+d+1-d):# output layer of deletion
      temp_row = []
      for l in range(1,n+d+1-d):# zeta nodes of deletion
          for j in range (1,d+2):
            w = 0
            if l == i:
              w = 1
            temp_row.append(w)
      T1.append(temp_row)
T2=[]
for i in range(1,n+d+1-d):# output layer of deletion
      temp_row = []
      for l in range(1,n+2):#tau nodes
            w = 0
            temp_row.append(w)
      T2.append(temp_row) 
T3=[]
for i in range(1,n+d+1-d):# output layer of deletion
      temp_row = []
      for l in range(1,n+2): #Insertion(mu nodes)
         for k in range(3*d+1,4*d+1):
             for q in range(2):
               w = 0
               temp_row.append(w)
      T3.append(temp_row) 
T4=[]
for i in range(1,n+d+1-d):# output layer of deletion
      temp_row = []
      for l in range(1,n+2): #Insertion(lambda nodes)
         for k in range(3*d+1,4*d+1):
             for q in range(2):
               w = 0
               temp_row.append(w)
      T4.append(temp_row)  
T5=[]
for i in range(1,n+d+1-d):# output layer of deletion
      temp_row = []
      for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
               w = 0
               temp_row.append(w)
      T5.append(temp_row)      
for i in range(len(T1)):
    concatenated_row1 = T1[i] + T2[i] + T3[i] + T4[i] + T5[i] 
    W17.append(concatenated_row1)     
#######
# for insertion nodes
T6=[]
for i in range(1,n+1):# tau' nodes of insertion
      temp_row = []
      for l in range(1,n+d+1-d):# zeta nodes of deletion
          for j in range (1,d+2):
            w = 0
            temp_row.append(w)
      T6.append(temp_row)
T7=[]
for i in range(1,n+1):# tau' nodes of insertion
      temp_row = []
      for l in range(1,n+2):#tau nodes
            w = 0
            if l <= i:
              w = 1
            temp_row.append(w)
      T7.append(temp_row) 
T8=[]
for i in range(1,n+1):# tau' nodes of insertion
      temp_row = []
      for l in range(1,n+2): #Insertion(mu nodes)
         for k in range(3*d+1,4*d+1):
             for q in range(2):
               w = 0
               temp_row.append(w)
      T8.append(temp_row) 
T9=[]
for i in range(1,n+1):# tau' nodes of insertion
      temp_row = []
      for l in range(1,n+2): #Insertion(lambda nodes)
         for k in range(3*d+1,4*d+1):
             for q in range(2):
               w = 0
               temp_row.append(w)
      T9.append(temp_row)  
T10=[]
for i in range(1,n+1):# tau' nodes of insertion
      temp_row = []
      for l in range(4*d+1,5*d+1): #Insertion(x_j+d nodes)
               w = 0
               temp_row.append(w)
      T10.append(temp_row)      
for i in range(len(T6)):
    concatenated_row2 = T6[i] + T7[i] + T8[i] + T9[i] + T10[i] 
    W17.append(concatenated_row2)
##
T11=[]
for i in range(1, n+2): #omega nodes
    for j in range(1,d+1):
        temp_row = []
        for l in range(1,n+d+1-d):# zeta nodes of deletion
          for j in range (1,d+2):
            w = 0
            temp_row.append(w)
        T11.append(temp_row)
T12=[]
for i in range(1, n+2): #omega nodes
    for j in range(1,d+1):
       temp_row = []
       for l in range(1,n+2):#tau nodes
            w = 0
            temp_row.append(w)
       T12.append(temp_row)      
T13=[]
for i in range(1, n+2): #omega nodes
    for j in range(1,d+1):
       temp_row = []
       for l in range(1,n+2): #Insertion(mu nodes)
          for k in range(1,d+1):
             for q in range(2):
               w = 0
               if i == l and j==k:
                   if q == 0:
                       w = C
                   else: # q = 1
                       w = - C  
               temp_row.append(w)
       T13.append(temp_row) 
T14=[]
for i in range(1, n+2): #omega nodes
    for j in range(1,d+1):
       temp_row = []
       for l in range(1,n+2): #Insertion(lambda nodes)
          for k in range(1,d+1):
             for q in range(2):
               w = 0
               if i == l and j==k:
                   if q == 0:
                       w = C
                   else: # q = 1
                       w = - C  
               temp_row.append(w)
       T14.append(temp_row)   
T15=[]
for i in range(1, n+2):#omega nodes
    for j in range(1,d+1):
        temp_row = []
        for k in range(d+1, (2*d)+1):
            w = 0
            if j+d==k:
              w = 1
            temp_row.append(w)
        T15.append(temp_row)       
for i in range(len(T11)):
    concatenated_row3 = T11[i] + T12[i] + T13[i] + T14[i] + T15[i] 
    W17.append(concatenated_row3)    
##Bias matrix for output layer of deletion process   

B17 = []
for i in range(1,n+1):
      temp_row = []
      for l in range(1):
        b=0
        temp_row.append(b)
      B17.append(temp_row)
# for insertion nodes
for i in range(1, n+1):#(corresponding to tau' nodes)
    temp_row = []
    for l in range(1):
        w = i
        temp_row.append(w)
    B17.append(temp_row)

for i in range(1, n+2):#(corresponding to omega nodes)
    for j in range(1,d+1):
        temp_row = []
        for l in range(1):
            w = -2*C
            temp_row.append(w)
        B17.append(temp_row)
# print("Bias for output layer of deletion process")
# print(B17)  

e_D = [] # Output nodes after deletion
for i in range(len(W17)):
    temp_row = []
    e_D_i_entry =np.maximum( (np.dot(W17[i], L16)+B17[i]),0)   
    e_D.append(e_D_i_entry)
    
# #print('Printing e_D nodes after deletion') 
# for i in e_D:
#     print(i) 
#####################################################################################  

##To construct the weight matrix for eighteenth hidden layer L18=W18*e_D+B18
W18 = []
U1 = []  
for l in range(1, n+1):# e_D nodes as identity map
   temp_row = []
   for i in range(1, n+1):
       w = 0
       if l==i:
           w=1
       temp_row.append(w)
   U1.append(temp_row)
##
U2 = []  
for l in range(1, n+1):# e_D nodes
   temp_row = []
   for i in range(1, n+1):
       w = 0
       temp_row.append(w)
   U2.append(temp_row)
#
U3 = []  
for l in range(1, n+1):# e_D nodes
   temp_row = []
   for i in range(1, n+2):
       for j in range(1,d+1):
         w = 0
         temp_row.append(w)
   U3.append(temp_row)
for i in range(len(U1)):
    concatenated_row1 = U1[i] + U2[i] + U3[i] 
    W18.append(concatenated_row1)   
# 
U4 = []  
for l in range(1, n+1):# (mu 21 and mu 22 nodes ) 
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+1):#e_S nodes
                w = 0
                temp_row.append(w)
            U4.append(temp_row)
U5 = []  
for l in range(1, n+1):#mu 21 and mu 22 nodes
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+1):#tau' nodes
                  w = 0
                  if l==i:
                      w=1/eps 
                  temp_row.append(w)
            U5.append(temp_row)             
U6 = []  
for l in range(1, n+1):#mu 21 and mu 22 nodes
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+2):#omega nodes
                for k in range (1, d+1):
                  w = 0
                  temp_row.append(w)
            U6.append(temp_row)   
# 
for i in range(len(U4)):
    concatenated_row2 = U4[i] + U5[i]  + U6[i]
    W18.append(concatenated_row2)  
#  
U7 = []  
for l in range(1, n+1):# lambda 21, lambda 22 nodes
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+1):#e_D nodes
                w = 0
                temp_row.append(w)
            U7.append(temp_row)
#   
U8 = []  
for l in range(1, n+1):# lambda 21, lambda 22 nodes
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+1):#tau' nodes
                w = 0
                if l==i:
                    w=-1/eps
                temp_row.append(w)
            U8.append(temp_row)   
#print(H3)  
#    
U9 = []  
for l in range(1, n+1):# lambda 21, lambda 22 nodes
    for j in range(1, d+2):
        for q in range (2):
            temp_row = []
            for i in range(1, n+2): #omega nodes
                for k in range (1, d+1):
                      w = 0
                      temp_row.append(w)
            U9.append(temp_row)   
for i in range(len(U7)):
    concatenated_row3 = U7[i] + U8[i] + U9[i]
    W18.append(concatenated_row3)  
##
U10 = []  
for h in range(1, n+d+1):# zeta nodes
  temp_row = []
  for i in range(1, n+1):#e_D nodes
      w = 0
      temp_row.append(w)
  U10.append(temp_row)
U11 = [] 
for h in range(1, n+d+1):# zeta nodes
  temp_row = []
  for i in range(1, n+1): #tau' nodes
      w = 0
      temp_row.append(w)
  U11.append(temp_row)  
  
U12 = []  
for h in range(1, n+d+1):# zeta nodes
    temp_row = []
    for i in range(1, n+2):#omega nodes
        for j in range (1, d+1):
          w = 0
          if h==i+j-1:
              w = 1
          temp_row.append(w)
    U12.append(temp_row)
#####          
for i in range(len(U10)):
      concatenated_row4 = U10[i] + U11[i] + U12[i]
      W18.append(concatenated_row4)     
#print('Printing weight matrix for tenth layer/ninth hidden layer')     
#print(W18) 

# Bias matrix for eighteenth hidden layer     
B18 = [] 

for i in range(1,n+1):# corresponding to e_D nodes
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B18.append(temp_row)
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
            B18.append(temp_row) 
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
            B18.append(temp_row)  
 
for h in range(1, n+d+1):#(corresponding to zeta nodes)
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B18.append(temp_row)            
#print('Printing Bias matrix for eighteenth hidden layer')               
#print(B18)
      
L18 = [] # mu 21 , mu 22,lambda 21 , lambda 22 and zeta nodes
for i in range(len(W18)):
    L18_i_entry = np.maximum((np.dot(W18[i], e_D) +B18[i]),0)   
    L18.append(L18_i_entry)
# print('Printing nodes for eighteenth hidden layer')
# for i in L18:
#     print(i) 
# ###
# #To construct the weight matrix for ninteenth hidden layer L19=W19*L18+B19.
W19=[]
## 
V1 = [] 
for i in range(1, n+1): #(corresponding to omega')
    for j in range(1, d+2):  
      temp_row = []  
      for l in range(1, n+1):#e_D nodes
                w = 0    
                if i == l :
                  w=1
                temp_row.append(w)
      V1.append(temp_row) 
V2 = [] 
for i in range(1, n+1): #(corresponding to omega')
    for j in range(1, d+2):  
      temp_row = []  
      for l in range(1, n+1):#mu nodes
          for k in range(1, d+2):
            for q in range(2):
                w = 0    
                if i == l and j==k:
                    if q==0:
                        w=C
                    else:       
                          w =-C
                temp_row.append(w)
      V2.append(temp_row)
#print(V2)            
V3 = [] 
for i in range(1, n+1): #(corresponding to omega')
    for j in range(1, d+2):  
      temp_row = []  
      for l in range(1, n+1):# lambda nodes
          for k in range(1, d+2):
            for q in range(2):
                w = 0    
                if i == l and j==k:
                    if q==0:
                        w=C
                    else:       
                        w =-C
                temp_row.append(w)
      V3.append(temp_row)
#
V4 = [] 
for i in range(1, n+1): #(corresponding to omaga')
    for j in range(1, d+2):
      temp_row = []  
      for h in range(1, n+d+1):# zeta nodes
          w = 0
          temp_row.append(w)
      V4.append(temp_row)
#
for i in range(len(V1)):
    concatenated_row1 = V1[i] + V2[i] + V3[i]+ V4[i]
    W19.append(concatenated_row1) 
#
V5 = [] 
for h in range(1, n+d+1): #(corresponding to zeta)
    temp_row = []  
    for i in range(1, n+1):#e_D nodes
                w = 0    
                temp_row.append(w)
    V5.append(temp_row)
V6 = [] 
for h in range(1, n+d+1): #(corresponding to zeta)
    temp_row = []  
    for i in range(1, n+1):# mu nodes
        for j in range(1, d+2):
            for q in range(2):
                w = 0    
                temp_row.append(w)
    V6.append(temp_row)
#            
V7 = [] 
for h in range(1, n+d+1): #(corresponding to zeta)
    temp_row = []  
    for i in range(1, n+1):# lambda nodes
        for j in range(1, d+2):
            for q in range(2):
                w = 0    
                temp_row.append(w)
    V7.append(temp_row)
#
V8 = [] 
for h in range(1, n+d+1): #(corresponding to zeta)
    temp_row = []  
    for p in range(1, n+d+1):# zeta nodes
        w = 0 
        if h==p:
            w=1
        temp_row.append(w)
    V8.append(temp_row)
#
for i in range(len(V5)):
    concatenated_row2 = V5[i] + V6[i] + V7[i]+ V8[i]
    W19.append(concatenated_row2) 
#print('Printing weight matrix for ninteenth hidden layer')     
#print(W19)     

# # Bias matrix for ninteenth hidden layer       
B19 = [] 
for i in range(1, n+1):#(corresponding to omega' nodes)
    for j in range (1, d+2):
      temp_row = []
      for l in range(1):
          w=-2*C
          temp_row.append(w)
      B19.append(temp_row) 

for i in range(1, n+d+1):#(corresponding to zeta nodes)
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B19.append(temp_row)
   
#print('Printing Bias matrix for ninteenth hidden layer')              
#print(B19)
      
L19 = [] 
for i in range(len(W19)):
    L19_i_entry = np.maximum((np.dot(W19[i], L18) +B19[i]),0)   
    L19.append(L19_i_entry)
#print('nodes for ninteenth hidden layer')
#print('this is index i:', i)
# for i in L19:
#     print(i) 
W20=[]  
#To construct weight matrix for twenteeth hidden layer L20=W20*L19+B20.   

V9 = [] 
for h in range(1, n+d+1): #(corresponding to zeta' and omega' nodes)
    temp_row = []  
    for i in range(1, n+1):
        for j in range(1, d+2):
          w = 0 
          if h==i+j-1:
            w=1
          temp_row.append(w)
    V9.append(temp_row)
##
V10 = [] 
for h in range(1, n+d+1): #(corresponding to zeta' and zeta nodes)
    temp_row = []  
    for p in range(1, n+d+1):
        w = 0
        temp_row.append(w)
    V10.append(temp_row) 
## 
for i in range(len(V9)):
    concatenated_row1 = V9[i] + V10[i]
    W20.append(concatenated_row1)    
###
V11 = [] 
for h in range(1, n+d+1): #(corresponding to zeta and omega' nodes)
    temp_row = []  
    for i in range(1, n+1):
        for j in range(1, d+2):
          w = 0 
          temp_row.append(w)
    V11.append(temp_row)
##
V12 = [] 
for h in range(1, n+d+1): #(corresponding to zeta' and zeta nodes)
    temp_row = []  
    for p in range(1, n+d+1):
        w = 0
        if h==p:
            w=1
        temp_row.append(w)
    V12.append(temp_row)
#print(V12)    
## 
for i in range(len(V11)):
    concatenated_row2 = V11[i] + V12[i]
    W20.append(concatenated_row2) 
#print('Printing weight matrix for twenteeth hidden layer')     
#print(W20)    

#Bias matrix for twenteeth hidden layer      
B20 = [] 
for h in range(1, n+d+1):#(corresponding to zeta' nodes)
    temp_row = []
    for l in range(1):
      w=0
      temp_row.append(w)
    B20.append(temp_row) 

for i in range(1, n+d+1):#(corresponding to zeta nodes)
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B20.append(temp_row)
#print('Printing Bias matrix for twenteeth hidden layerr')               
#print(B20) 
L20 = [] # zeta prime nodes
for i in range(len(W20)):
    L20_i_entry = np.maximum((np.dot(W20[i], L19) +B20[i]),0)   
    L20.append(L20_i_entry)
#print('nodes for twenteeth hidden layer')
#print('this is index i:', i)
#for i in L20:
#    print(i) 
#
###
#To construct weight matrix for twenty first hidden layer L21=W21*L20+B20
W21=[]        
V13 = []      
for i in range(1,n+d+1):  
    temp_row = []
    for l in range(1,n+d+1):
        w = 0
        if i==l:
            w = 1
        temp_row.append(w)
    V13.append(temp_row) 
# # 
V14 = []     
for i in range(1,n+d+1):  
    temp_row = []
    for l in range(1,n+d+1):
        w = 0
        if i==l:
            w = 1
        temp_row.append(w)
    V14.append(temp_row) 
#
for i in range(len(V13)):
    concatenated_row1 = V13[i] + V14[i] 
    W21.append(concatenated_row1)
    
# # Bias matrix for output layer  
B21 = [] 

for h in range(1, n+d+1):  #(Zeta nodes)
    temp_row = []
    for l in range(1):
        w = 0
        temp_row.append(w)
    B21.append(temp_row)       
            
# print('Printing Bias matrix for output layer')               
# print(B21)
      
e_I = [] # Out put of neural network
for i in range(len(W21)):
    e_I_i_entry =np.maximum((np.dot(W21[i], L20) +B21[i]), 0)
    e_I.append(e_I_i_entry)  
#print('Printing e_I')
#for i in e_I:
#    print(i)  
#################################################################################
  # Now to get required Y we have to trim e_I to remove extra values.
#################################################################################

#################################################################################
#################################################################################
  #                       TRIMMING THE EXTRA VALUES                            #
#by keeping only the number of values (n−n_D)+ n_I  from e_I, 
#where n_D is the number of distinct non-zero values or positions in X_D that is less than d+1,
#n_I is the number of values or positions in x_I that lies in the interval (0, (n+1 − n_D)/(n+1)] with index less than d+1  
#################################################################################
#################################################################################
# Divede input X into 5 equal parts
portion_length = len(X) // 5

# Split the list into 5 equal parts
X_d = [X[i * portion_length: (i + 1) * portion_length] for i in range(5)]

# Print the result
#for i, portion in enumerate(X_d, start=1):
#    print(f"X {i}: {portion}")
#Where X 1=X_d[0] and X 2=X_d[1] are portions of input that is responsible for Substitution    
#Where X 3=X_d[2] is portion of input that is responsible for Deletion  
#Where X 4=X_d[3] and X 5=X_d[4] is portion of input that is responsible for Insertion 
#################################################################################
#################################################################################
#print(X_d[0])
# portion of X_S that contains indices or positions where we have to substitute is X 1=X[0]
X_1 = X_d[0]

# Use a set to store unique non-zero values
distinct_non_zero_indices_in_X_S = set()

# Iterate through the sublist and add non-zero values to the set
for value in X_1:
    if value != 0:
        distinct_non_zero_indices_in_X_S.add(value)

# Count the number of distinct non-zero values
n_S = len(distinct_non_zero_indices_in_X_S)

# Print the result
#print(f"n_S=Number of distinct non-zero indices or positions in X_1= {n_S}")
####################################################################################
####################################################################################
#print(X_d[2])
# portion of X that will responsible to perform deletion i.e X_D operation is given as
X_3 = X_d[2]

# Filter out non-zero values and keep only distinct values
distinct_non_zero_values_X_3 = set(value for value in X_3 if value != 0)
#print(distinct_non_zero_values_X_3)

# Initialize the set T with values from n_S
T = set(distinct_non_zero_values_X_3)

# Sum of values in set T
sum_T = len(T)

# Calculate the maximum number of distinct nonzero values in X_D, so that the sum of these number of values and n_S less than d+1 
n_D = min(d - n_S, sum_T)

#print(f"n_D=number of distinct nonzero values in X_D, so that the sum of these number of values and n_S less than d+1= {n_D}")
###################################################################################
##################################################################################
X_4 = X_d[3]

# Filter out non-zero values from X_4
non_zero_values_X_4 = [value for value in X_4 if value != 0]
# print("nonzero values in X_4")
# print(non_zero_values_X_4)

# Initialize the set U with values from X_4
U = set(non_zero_values_X_4)
# Sum of values in set U
sum_U = len(U)

# Calculate the maximum number of nonzero values in X_4, so that the sum of these values, n_S and n_D is less than d + 1
p_I = min(d - n_S - n_D, sum_U)

#print(f"p_I = number of nonzero values in X_4, so that the sum of these values, n_S and n_D is less than d + 1= {p_I}")

# Initialize a list to store the first p_I non-zero values
q_I = non_zero_values_X_4[:p_I]

# Print or use the list of the first m non-zero values
#print("First", p_I, "non-zero values in X_4 are:", q_I)
##################################################################################
##################################################################################
# Calculate the maximum number of nonzero values in X_4, so that the sum of these values, n_S and n_D is less than d + 1 and lies in ( 0,   (n+1 − n_D)/(n+1)  ]
# Calculate the maximum number of nonzero values in q_I that lies in interval ( 0,   (n+1 − n_D)/(n+1)  ]

# Calculate the threshold value
threshold_value = (n + 1 - n_D) / (n + 1)

# Count the number of positions that meet the criteria
n_I = sum(1 for i, value in enumerate(q_I) if 0 < value <= threshold_value)

# Print the result
#print(f"n_I=Number of positions in X_4 with index less than {d + 1} and value in (0, {(n + 1 - n_D) / (n + 1)}]: {n_I}")
###################################################################################
###################################################################################
#print('Final output')
# Calculate the number of values to keep
num_values_to_keep = (n - n_D) + n_I

# Keep only the first (n − n_D) + n_I values
e_I = e_I[:num_values_to_keep]

# print("Printing Y:")
# for item in e_I:
#     print(item)
    
values = [int(array[0]) for array in e_I]
print("Output:", values)