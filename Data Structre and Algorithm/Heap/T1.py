
def sym_array(nums,n):
    l=len(nums)
    add=n-l
    count=0
    i=0
    temp=[]
    for j in nums:
        temp.append(j)
    ans=temp
    while count<add:
        front=nums[i]
        rear=nums[i]
        ans.insert(0,front)
        ans.append(rear)
        count=count+2
        i=i+1
    return ans
def sym(s,n):
    l=len(s)
    add=n-l
    count=0
    i=0
    ans=s
    while count<add:
        front=s[i]
        rear=s[i]
        ans=front+ans+rear
        count=count+2
        i=i+1
    return ans
f=open('data.txt')
number=int(f.readline())
Data=[]
for i in range(number):
    s=f.readline().split()
    N=int(s[0])
    M=int(s[1])
    temp=[]
    for j in range(N+1):
        temp.append(f.readline().split())
    temp.pop(-1)
    temp=sym_array(temp,M)
    for k in range(M):
        s=temp[k][0]
        s=sym(s,M)
        print(s)
    print("\n")

