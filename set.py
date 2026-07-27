sets = set()
set1 = {10,20,30}
set2 = set([40,50,60])
set3 = {70, "Hello World", 80}

print("Empty Set : ",sets)                          #Empty Set :  set()
print("Set with Values : ",set1)                    #Set with Values :  {10, 20, 30}
print("Set with List : ",set2)                      #Set with List :  {40, 50, 60}
print("Mixed Set : ",set3)                          #Mixed Set :  {80, 'Hello World', 70}




s = {10 , 20 , 30}
print("Original Set :",s)                           #Original Set : {10, 20, 30}

s.add(40)
print("After add :",s)                              #After add : {40, 10, 20, 30}

s.update([50 , 60])
print("After Update :",s)                           #After Update : {40, 10, 50, 20, 60, 30}

s2 = s.copy()
print("Copies Set :",s2)                            #Copies Set : {50, 20, 40, 10, 60, 30}

s.pop()
print("Popped Element :",s)                         #Popped Element : {10, 50, 20, 60, 30}

s.discard(60)
print("Discarded Element :",s)                      #Discarded Element : {10, 50, 20, 30}

s.remove(20)
print("Removed Element :",s)                        #Removed Element : {10, 50, 30}

s.clear()
print("Cleared Set :",s)                            #Cleared Set : set()




a = {1 ,2 ,3}
b = {3 ,4 ,5}

print("Value of Set A :",a)                                          #Value of Set A : {1, 2, 3}
print("Value of Set B :",b)                                          #Value of Set B : {3, 4, 5}
print("Union of Both Set :",a.union(b))                              #Union of Both Set : {1, 2, 3, 4, 5}
print("Intersection of Both Set :",a.intersection(b))                #Intersection of Both Set : {3}
print("Difference of Set A :",a.difference(b))                       #Difference of Set A : {1, 2}
print("Difference of Set B :",b.difference(a))                       #Difference of Set B : {4, 5}