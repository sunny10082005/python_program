dict1 = {}
dict2 = {"name":"Parth" , "age" : 21}
dict3 = dict([("X",1),("Y",2)])
dict4 = {1 : "One" , "Two" : 2}

print("Empty Dictionary :",dict1)
print("Proper Dictionary :",dict2)
print("Using Dict() :",dict3)
print("Mixed Keys :",dict4)




d = {"name" : "Parth" , "age" : 21 , "City" : "Jamnagar"}

print("Original Dictionary :",d)
print("Length :",len(d))
print("Name :",d.get("name"))
d.update({"Gender" : "Male"})
print("After Update :",d)
d.pop("City")
print("After Pop :",d)
d["Country"] = "India"
print("After adding Country :",d)
print("Keys :",d.keys)
print("Values :",d.values)
print("Items :",d.items)

d2 = d.copy()
print("Copied Dictionary :",d2)

d.clear()
print("After Clear :",d)