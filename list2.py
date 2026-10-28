from math import sqrt

n=int(input("enter the number"))
num_list=[]
for i in range(n):
    a=int(input("enter the number"))
    num_list.append(a)
    print("entered list is ",num_list)
    sqr_1st=[x**2 for x in num_list]
    print("squared list:",sqr_1st)