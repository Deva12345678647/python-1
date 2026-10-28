#a

num_list=[-5,10,30,-45,-3,33,-12,24]
print(num_list)
new_list=[x for x in num_list if x>0]
print("The positive number are:",new_list)

#b:

n=int(input("Enter the number of element:"))
num_list=[]
for i in range(n):
    a=int(input("Enter the numbers:"))
    num_list.append(a)
print("Entered list:",num_list)
sqr_list=[x**2 for x in num_list]
print("squared list:",sqr_list)

#c:

word=input("Enter a word:")
vowels=[x for x in word.lower() if x in['a','e','i','o','u']]
print("The vowels in this word are:",vowels)

#d:

w=input("enter a word:")
ord=[ord(x) for x in w]
print("The ordinal value is:",ord)