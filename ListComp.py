myStr = 'Hello'

myList = [letter for letter in myStr]
myList2 = list(myStr)

print(myList)
print(myList2)

numList = range(0,11)

eveList = [x for x in numList if x%2 ==0]

print(eveList)

newList = [x if x%2 ==0 else 'ODD' for x in numList]
print(newList)
