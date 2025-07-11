def remove_duplicate(arr):
    visited=[]
    for i in arr:
        if i not in visited:
            visited.append(i)
    print('original array:',arr)
    print('duplicates removed:',visited)
arr=[45,78,54,89,45,54,78,54,89,65,54,6,54,21,32,54,59,89,54]
remove_duplicate(arr)