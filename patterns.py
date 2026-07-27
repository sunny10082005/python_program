for i in range(1,6):                    #1
    print(str(i)*i)                     #22
                                        #333
                                        #4444
                                        #55555
    

for i in range(1,6):                    #A
    for j in range(65,65+i):            #A B
        print(chr(j),end=" ")           #A B C
    print()                             #A B C D
                                        #A B C D E

    
for i in range(5 , 0 ,-1):              #*****
    print("*" * i)                      #****
                                        #***
                                        #**
                                        #*