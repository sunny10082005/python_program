def student_detail():
    name = "Sunny"
    age = 21
    course = "BCA"
    return name , age , course

n,a,c = student_detail()

print("Name :",n)
print("Age :",a)
print("Course :",c)




x = 10


def show():
    x = 5
    print("Local X :",x)

def display():
    global x
    x = x + 6
    print("Modified X :",x)

show()
print("Global X before function call:",x)
display()

print("Global X after function call:",x)