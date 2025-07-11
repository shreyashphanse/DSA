import array
def move_left(arr,k):
    move1=[]
    for i in range(k,len(arr)):
        move1.append(arr[i])
    for j in range(k):
        move1.append(arr[j])
    print('moved left:',move1)
def move_right(arr,k):
    move2=[]
    ran=[]
    x=[]
    for i in range(1,len(arr)+1):
        ran.append(i)
    rev_range=[x*-1 for x in ran]
    for i in range(k):
        x.append(rev_range[i])
    x.reverse()
    for i in x:
        move2.append(arr[i])
    for i in range(len(arr)-k):
        move2.append(arr[i])
    print('moved right:',move2)

arr=[78,56,12,32,1]
print(arr)
k=int(input('enter the value for k:'))
move_left(arr,k)
move_right(arr,k)