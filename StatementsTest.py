st = 'Print only the words that start with s in this sentence'
SList=[]
for word in st.split():
    if word[0].lower() == 's' and len(word)>1:
        SList.append(word)
    else:
        pass

print(SList)

numList = list (range(0,11,2))
print(numList)

Div3List = [num for num in range(1,50) if num%3==0]
print(Div3List)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 ==0:
        print(f'{word}: even')
    else:
        print(f'{word}: ODD')

for num in range(1,101):
    if num%3 == 0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5 ==0:
        print("Buzz")
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'

myList = [word for word in st.split()]
print(myList)

myList=[]
for word in st.split():
    myList.append(word[0])

print(myList)