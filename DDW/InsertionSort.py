numbers = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]

for i in range(1,len(numbers)):
    #start from 2nd element in array
    check = numbers[i]
    
    #previous element
    prev=i-1
    
    #pass through pervious cases, go backwards, push up one index if greater than check
    #escape if smaller than check since its already sorted, so current element will be right place
    while prev>=0 and check<numbers[prev]:
        numbers[prev+1]=numbers[prev]
        prev-=1
    numbers[prev+1]=check
    
print(numbers)
    