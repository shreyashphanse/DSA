def sec_largest(arr):
    large=arr[0]
    small=0
    if len(arr)<2:
        print('the size is too small to compare')
        return
    for i in arr:
        if i>large:
            large=i
    print('largest:',large)
    for i in arr:
        if small!=large:
            if i>small and i<large:
                small=i
    print('second largest:',small)
arr=[54,2]
sec_largest(arr)