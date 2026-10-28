list1=[1,2,3,4,5]
list2=[2,4,6,8]
print("Element in list one is",list1)
print("Element in list two is",list2)
if len(list1)==len(list2):
    print("List have same length")
    else:
        print("List have different length")
    s1=0
    s2=0
    for i in range(len(list1)):
        s1=s1+list1[i]
    print("The sum of list is")