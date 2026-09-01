list =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

target = int(input("What number do you want to look for:"))
startpos = 0
endpos = len(list) - 1
found = False
counter = 0
while found == False and (startpos <= endpos):
    middle = (startpos+endpos)//2
    if list[middle] == target:
        found = True
        counter+=1
    elif list[middle] < target:
        startpos = middle + 1
        counter+=1
    else:
        endpos = middle-1
        counter+=1

