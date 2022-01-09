import numpy as np
import pandas as pd
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'TeamPY4DS_Apyori.csv')
dataset = pd.read_csv(filename, sep=',')
dataset['items_buy']=(dataset['items_base']).str.split()
uni=[]
for i in dataset['items_buy']:
    for k in i:
        if k not in uni: uni.append(k)
uni=np.sort(uni)
res = {}
for i in range(0, len(uni)):
    res[i]=uni[i]

# def InputNumber(a, b):
#     n=input(" ")
#     if n.isnumeric():
#         if a<=int(n)<=b:
#             return int(n)
#         else:
#             print('Wrong input, try again: ')
#             InputNumber(a, b)
#     elif '-' in n:
#         print('Wrong input, try again: ')
#         InputNumber(a,b)
#     else:
#       t=n.strip(' ').rstrip(' ')
#       if a.isnumeric():
#         return int(t)
#       else:
#         print('Wrong input, try again: ')
#         InputNumber(a, b)

def Suggest(a):
    X=[]
    Y=[]
    a=list(np.sort(a))
    for i in range(1, len(dataset['items_buy'])):
        b=list(np.sort(dataset['items_buy'][i]))
        if a==b: 
          X.append(dataset['items_add'][i])
          Y.append(dataset['confidence'][i])
    if len(a)>=2:
        for i in range(0, len(a)):
          for j in range(0, len(dataset['items_buy'])):
            b=dataset['items_buy'][j]
            if a[i] in b: 
              X.append(dataset['items_add'][j])
              Y.append(dataset['confidence'][j])
    for i in range(0, len(a)):
      while a[i] in X: 
        X.remove(a[i])
        Y.remove(Y[i])
    Z = [x for _,x in sorted(zip(Y,X))]
    M = np.unique(Z, return_index=True)[1]
    return [Z[i] for i in sorted(M, reverse=True)]

#Infomation for in put:
# print('Input the product you want to buy: ')  
# for i,j in res.items():
#     print(i,j)
# print('Enter', len(uni) ,'if you want to stop')
# t=[]
# n=InputNumber(0, len(uni))
# while n!=len(uni):
#   t.append(n)
#   n=InputNumber(0, len(uni))
# print("So these are all products you want to buy: ")
# c=[]
# for i in range(0,len(t)):
#     b=t[i]
#     print(res[b])
#     c.append(res[b])
# print("Thanks for your buying, here is our suggest for you to select:")
# for i in range(0, len(Suggest(c))):
#   print(Suggest(c)[i], end=', ')
#   if i%5==0 and i>1: print('\n')