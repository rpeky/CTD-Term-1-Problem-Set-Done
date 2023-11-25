cases=int(input())
for i in range(cases):
    sumset=0
    linein=input()
    linein=list(linein.split())
    totalpeople=int(linein[0])
    for i in range(totalpeople):
        sumset+=int(linein[i+1])
    avg=sumset/totalpeople
    countaboveavg=0
    for i in range(totalpeople):
        if int(linein[i+1])>avg:
            countaboveavg+=1
    print('{:.3%}'.format(countaboveavg/totalpeople))
    
    