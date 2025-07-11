def find_missing_element(arr):
    missing=[]
    small=large=arr[0]
    for i in arr:
        if i > large:
            large = i
        if i < small:
            small = i
    # print(small,large)
    for i in range(small,large):
        if i not in arr:
            missing.append(i)
    print('missing elements',missing)
arr=[1,3,5,8]
find_missing_element(arr)