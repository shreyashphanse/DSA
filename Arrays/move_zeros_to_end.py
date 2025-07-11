def move_zeros_to_end(arr):
    zeros=[]
    visited=[]
    for i in arr:
        if i==0:
            zeros.append(i)
        else:
            visited.append(i)
    for j in zeros:
        visited.append(j)
    print('original array:',arr)
    print('modified array:',visited)
arr=[12,0,12,0,56,98,45,32,0]
move_zeros_to_end(arr)