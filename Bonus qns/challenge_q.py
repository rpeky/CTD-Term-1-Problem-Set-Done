q1=[]
q2=[]

customers = [('G', 6), ('F', 9), ('E', 6), ('D', 3), ('C', 4), ('B', 2), ('A', 7)]
check_len = len(customers)

#sort by time taken
for i in range(check_len):
    #exit early if no swaps found, means sorted
    check=False
    for j in range(check_len-i-1):
        if customers[j][1]>customers[j+1][1]:
            customers[j],customers[j+1]=customers[j+1],customers[j]
            check=True
    if check==False:
        break
        
print(customers)
#even case take alternatively append first and last value of list to minimise time
#odd case assign middle value to shorter time q
if(check_len%2==0):
    q1_total,q2_total=0,0
    for i in range(int(check_len/2)-1):
        if(i%2==0):
            q1.append(customers[i])
            q1.append(customers[check_len-1-i])
            q1_total+=customers[i][1]
            q1_total+=customers[check_len-1-i][1]
        else:
            q2.append(customers[i])
            q2.append(customers[check_len-1-i])
            q2_total+=customers[i][1]
            q2_total+=customers[check_len-1-i][1]
    if(q1_total<q2_total):
        q1.append(customers[int(check_len/2)-1])
        q1.append(customers[int(check_len/2)])
        q1_total+=customers[int(check_len/2)-1][1]
        q1_total+=customers[int(check_len/2)][1]
    else:
        q2.append(customers[int(check_len/2)-1])
        q2.append(customers[int(check_len/2)])
        q2_total+=customers[int(check_len/2)-1][1]
        q2_total+=customers[int(check_len/2)][1]

            
else:
    middle_val = int((check_len-1)/2)
    q1_total,q2_total=0,0
    for i in range(middle_val):
        if(i%2==0):
            q1.append(customers[i])
            q1.append(customers[check_len-1-i])
            q1_total+=customers[i][1]
            q1_total+=customers[check_len-1-i][1]
        else:
            q2.append(customers[i])
            q2.append(customers[check_len-1-i])
            q2_total+=customers[i][1]
            q2_total+=customers[check_len-1-i][1]
    if(q1_total<q2_total):
        q1.append(customers[middle_val])
    else:
        q2.append(customers[middle_val])

print(q1)
print(q2)
print(q1_total)
print(q2_total)