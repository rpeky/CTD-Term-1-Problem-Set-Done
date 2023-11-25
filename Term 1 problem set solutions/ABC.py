orddict={'A':0,'B':1,'C':2}

nums=input()
order=input()

ordnum=[]
nums=list(nums.split(' '))
for i in nums:
    ordnum.append(int(i))
ordnum.sort()

sol=''
for i in order:
    sol+=str(ordnum[orddict[i]]) + ' '
    
print(sol)
    
