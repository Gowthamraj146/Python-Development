d1 = {'k1': 123, 'k2': [1, 2, 3], 'k3': {'ik1': 'new'}}
print(d1['k3']['ik1'])

d1['k1']='234'
d1.update({'k1':'567'})
print(d1['k1'])


for  x,y in d1.items():
    print(x,y)

# copying a dict

d2 = d1.copy()
# because d2 = d1 will cause changes in d2 while we change in d1. Dict is reference type.

#Grab Hello
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2])
#A set is a collection which is unordered, unchangeable*, and unindexed. Do not accept duplicates

my_set = {'Apple','Banana','Carrot','Apple'}
print(my_set)
my_set.add('Apple')
print(my_set)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
thisset.add("Mango")
print(thisset)
thisset.update(my_set)
print(thisset)
# When you update a dict, only key values will be added inti the set
thisset.update(d1)
print(thisset)
thisset.add("Summa")
print(thisset)
thisset.clear()
set1 = {"Apple","banana", "cherry"}
set2= {"Google","Apple","Amazon"}
set3 = set1.difference(set2)
print(set3)