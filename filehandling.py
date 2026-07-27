#These will open file new.txt
W = open("new.txt" , 'w')

#these is used to write into the new.txt
W.write('Hello\n')
W.write('czmg\n')
W.write('Student\n')
W.close()

#these is used to read from the new.txt
R = open("new.txt" , 'r')               #Hello
print(R.read())                         #czmg
R.close()                               #Student

#these is used to append(add) in the new.txt
A = open("new.txt" , 'a')               #Hello
A.write('in Lab')                       #czmg
A.close()                               #Student
                                        #in Lab


#these is used to open new.txt file in text file and in read mode
RT = open("new.txt" , 'rt')             
print(RT.read())
RT.close()

#these is used to open new.txt file in text file and in write mode
WT = open("new.txt" , 'wt')             #Nothing
WT.write("Nothing\n")
WT.close()

#these is used to open new.txt file in text file and in append mode
AT = open("new.txt" , 'at')             #Nothing    
AT.write("Nothing1\n")                  #Nothin1
AT.close()


#these is used to open new.txt file in binary file and in read mode
RB = open("new.txt" , 'rb')             #b'Nothing\r\nNothing1\r\n'
print(RB.read())
RB.close()

#these is used to open new.txt file in binary file and in write mode
WB = open("new.txt" , 'wb')             #Nothing3
WB.write(b'Nothing3')
WB.close()

#these is used to open new.txt file in binary file and in append mode
AB = open("new.txt" , 'at')             #b'Nothing3Nothing4\r\n'   
AB.write("Nothing4\n")                  
AB.close()


#these is used to open new.txt file for update and read
UR = open("new.txt" , 'r+')         #Nothing3Nothing4   
UR.write('Nothing5\n')
print(UR.read())                
UR.close()

#these is used to open new.txt file for update and write
UW = open("new.txt" , 'w+')             #Nothing6 
UW.write('Nothing6')               
UW.close()

#these is used to open new.txt file for update and append
UA = open("new.txt" , 'a+')             #Nothing6Nothing7   
UA.write("Nothing7\n")                  
UA.close()

# This will raise an error because 'x' creates a new file for writing. If the file already exists, Python raises a FileExistsError.
X = open("new.txt", "x")               


X = open("sample.txt", "x")             #These will work
X.write("Hello")
X.close()

XR = open("sample.txt" , 'r')             #Hello  
print(XR.read())                
XR.close()

#for Copy
R = open("new.txt" , 'r')              
C = open("Copy.txt" , 'w')
C.write(R.read())

R.close()
C.close()


R = open("new.txt" , 'r')              
for r in R:
    print(r.strip())

R.close()


R = open("new.txt" , 'r')              
content = R.read()
char = len(content)
words = len(content.split())
lines = len(content.splitlines())

print("Characters :" , char)
print("Words :" , words)
print("Lines :" , lines)

R.close()