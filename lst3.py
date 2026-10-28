word=input("enter the word:")
vowels=[x for x in word.lower() if x in['a','e','i','o','u']]
print("The vowels in th word are:",vowels)