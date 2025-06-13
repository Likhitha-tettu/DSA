n = int(input())   #size of the array
a= list(map(int,input().split())) #input array
k=int(input()) #size of the window

sol = [] # list to print the solutions
for i in range(0,(n-k+1)):  #for every window in the array, copy the k elements into list b
    b=[]
    j=0
    l=i
    for m in range(0,k):
        b.append(a[l])
        l+=1
    b=sorted(b)   #sort the elements in list b and add it to the answer list 
    sol.append(b[k//2])
print(sol)