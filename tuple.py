t1 = ()
t2 = (1,2,3)
t3 = (4,"Hello",5)
t4 = ([6,7,8])

print("Empty Tuple :",t1)
print("Tuple with Value :",t2)
print("Tuple with Mix Datatype :",t3)
print("Tuple with list :",t4)



t = (1,2,5,8,6,3)
print("Tuple :",t)
print("Length :",len(t))
print("Count of 3:",t.count(3))
print("Index of 5 :",t.index(5))
print("Mininum :",min(t))
print("Maximum:",max(t))
print("Reversed :",tuple(reversed(t)))

t5 = (1,2,5)
print("Comparision :",t==t5)