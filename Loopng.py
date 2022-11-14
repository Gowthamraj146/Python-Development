import random

i=0
while i <6:
    print(i)
    i = i+1
else:
    print("Loop completed")

myList = [(1,2,3),(4,5,6),(7,8,9)]

for a ,b,c in myList:
    print(a)
    print(b)
    print(c)

d = {'k1':1,'k2':2,'k3':3}

for key, value in d.items():
    print(f'Key:{key} and value:{value}')

for num in range(10):
    print(num)

for num in range(0,10):
    print(num)

for num in range(0,11,2):
    print(num)

# enumerate

word = 'asdasd'

for item in enumerate(word):
    print(item)

# zip fution to return tuples of list

myList = [1,2,3]
l2 = ['a','b','c']
l3 = ['abc','cde','vfr']
for item in zip(myList, l2, l3):
    print(item)

print(random.randint(0, 100))


