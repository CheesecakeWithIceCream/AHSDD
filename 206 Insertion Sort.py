myList = [3,4,9,7,1]

counter =0 
for index in range (1,len(myList)):
#store the value to be inserted into the array
 currentvalue = myList[index]
 position = index


  #shift the rest of the array one to the right
 while position > 0 and myList[position-1]<currentvalue:
   myList[position] = myList[position-1]
   counter+=1
   position -= 1


 #insert the value into the array
 myList[position] = currentvalue


print(myList)
print(counter)
