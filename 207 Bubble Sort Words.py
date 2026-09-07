# This program can be found in the AH Standard Algorithms - Bubble Sort presentation
# This variation uses two fixed loops


myList = ["G","X","b","P","z"]
counter = 0

#start from the right
for outer in range (len(myList)-1,0,-1):
 for inner in range(outer):
   #compare two adjacent values
   if ord(myList[inner])>ord(myList[inner+1]):
     #assign one of the values to a temp variable
     temp = myList[inner]
     #overwrite one of the values
     myList[inner] = myList[inner+1]
     #replace with the temp value
     myList[inner+1] = temp
     counter+=1
  
print("Bubble sort complete")
print(myList)
print(counter)