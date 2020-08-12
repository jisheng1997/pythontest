# num =[] # list
# for i in range(1,5): # range 的高位是不包括在内的
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i != k and  j!=k :
#                 print (i,j,k)
#                 print (k,j,i) # reverse num
#                 num.append([i,j,k])
# print ("how many num we have of the permutation and combination :",len(num))   # 24

# lists =[ (i*100+10*j+k) for i in range(1,5) for j in range(1,5) for k in range(1,5) if ( i!=j and i !=k and j!=k )]
# print (len(lists),":",lists)
#
#
# list1 = [0,0,0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9]

list2= [12,14,5,9,30,16]

#冒泡排序
for j in range(0,len(list2)):
    for i in range (0,len(list2)-1-j):
        if list2[i]>list2[i+1]:
            list2 [i],list2[i+1] = list2 [i+1],list2[i]
print(list2)




