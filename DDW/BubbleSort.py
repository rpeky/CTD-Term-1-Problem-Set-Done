#Bubble Sort


numbers = [7,2,3,4,5,7,7,6,9]
count=0
#loop through every element in the array
for i in range(len(numbers)):
    #since every pass will set the largest value at the end of array, 
    #we can reduce checks for the inner loop every round: hence len(array) - which big iteration (i) - 1
    for j in range(len(numbers)-i-1):
        #if number in wrong place, swap
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
        count+=1
                  
print(count,numbers)


#optimised bubble, added early exit condition
numbers = [1,2,3,4,5,7,7,6,9]
count=0
for i in range(len(numbers)):
    #exit early if no swaps found, means sorted
    check=False
    for j in range(len(numbers)-i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            check=True
        count+=1
    if check==False:
        break
                  
print(count,numbers)