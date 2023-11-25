
num=input()

if(int(num)<149):
    print(99)
elif(int(num)>9999):
    print(9999)
else:
    adjusted=list(num)
    adjusted[-1]='9'
    adjusted[-2]='9'
    adjusted=''.join(adjusted)
    diff=int(adjusted)-int(num)
    if(diff<51):
        print(int(adjusted))
    else:
        print(int(adjusted)-100)