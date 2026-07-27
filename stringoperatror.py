x = 10
y = "Hello World"
z = [1 , 2 , 3]
k = 3 + 4j
f = True
g = 3.14

print(type(x))
print(type(y))
print(type(z))
print(type(k))
print(type(f))
print(type(g))

print("ID of a :",id(x))

print("First Char :",y[0])
print("Last Char :",y[-1])
print(y[2:5])

print(y.upper())
print(y.lower())

c = "   Hello World!    "
print(y.strip())

print(y.replace("H" , "K"))

a = "TY"
b = y + a
print(b)

Name = "Chavda Parth"
age = 20
txt = f"My name is {Name} and age is {age}"
print(txt)




def reverse_str(s):
    return s[::-1]

print("Reversed String :",reverse_str("Hello"))

