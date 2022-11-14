my_list = [5, 6, 3, 4]
print(my_list)
my_list.sort()
print(my_list)
my_list.append(10)
print(my_list)
my_list.pop(0)
print(my_list)
list2 = ['sdf', 'agfa', 'jrj']
new_list = my_list + list2

print(new_list)
new_list = []
print(new_list)
fruits = ['Apple', 'Banana', 'Carrot', 'Dog']
for x in fruits:
    if 'a' in x.lower():
        new_list.append(x)
# Lambda function new_list = (x for x in fruits if 'a' in x)
print(new_list)

new_list.sort(reverse=True)

print(new_list)
list3 = [1, 2, 3, 4, 1, 3, 2, 4,34,45,49, 1226, 234, 345, 567]
print(list3)

def myfunc(n):
    return abs(n - 50)


list3.sort(key=myfunc)
print(list3)

x = (1,2,3,4)
z=(21,89)
print(x)
print(x)
print(type(x))
y = list(x)
y[0] = "abc"
x = tuple(y)
print(x)