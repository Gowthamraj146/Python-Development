qty = 2
price = 10
material = "Oranges"
myStr="I want to buy {2}  {1} for {0} Rupees"
print(myStr.format(qty,material,price))

myStr2= "Just for fun.. results today"
print(myStr2.split("."))

txt = "Hello World!"
print(txt)
txt2 = "apple , banana , cherry"
result = txt2.replace('apple','mango')
print(txt2)
print(result)


print(txt2[::-1])
x= txt2.rsplit(" , ")
print(x)
print(len(txt2))