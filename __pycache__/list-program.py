elist = []
list1 = [1 , 2 , 3]
list2 = list("Python is Easy language")
list3 = list(range(1,5))

print("Empty List :",elist)
print("List with number:",list1)
print("List from string:",list2)
print("List using Range:",list3)




lst = [10 , 20 , 30 , 40]
print("Original List :" , lst)                  #Original List : [10, 20, 30, 40]
print("Length :" , len(lst))                    #Length : 4

print("Count of 20:",lst.count(20))             #Count of 20: 1
print("Index of 30:",lst.index(30))             #Index of 30: 2

lst.append(50)
print("Appended List :" , lst)                  #Appended List : [10, 20, 30, 40, 50]

lst.insert(1 , 15)                              #After insert : [10, 15, 20, 30, 40, 50] 15 added at index 1
print("After insert :",lst)

lst.extend([60 , 70])                           #After extend : [10, 15, 20, 30, 40, 50, 60, 70]
print("After extend :",lst)

lst.append([80 , 90])                           #After append : [10, 15, 20, 30, 40, 50, 60, 70, [80, 90]]
print("After append :",lst)

lst.remove(15)                                  #After Removal : [10, 20, 30, 40, 50, 60, 70, [80, 90]]
print("After Removal :",lst)

lst.remove([80 , 90])                           #After Removal : [10, 20, 30, 40, 50, 60, 70]
print("After Removal :",lst)

lst.pop()                                       #After pop : [10, 20, 30, 40, 50, 60]
print("After pop :",lst)

lst.reverse()                                   #Reverse : [60, 50, 40, 30, 20, 10]
print("Reverse :",lst)

lst.insert(1 , 90)                              #After insert : [10, 90, 20, 30, 40, 50, 60]
print("After insert :",lst)

lst.sort()                                      #Sort : [10, 20, 30, 40, 50, 60, 90]
print("Sort :",lst)

copy = lst.copy()                               #Copy : [10, 20, 30, 40, 50, 60, 90]
print("Copy :",copy)

lst.clear()                                     #After Clear : []
print("After Clear :",lst)                      #Copied : [10, 20, 30, 40, 50, 60, 90]
print("Copied :",copy)
