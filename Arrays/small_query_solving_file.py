def rotate(arr,k):
    n_arr=[]
    neg=[]
    neg2=[]
    for j in range(1,len(arr)+1):
        neg.append(j)
    neg=[x*-1 for x in neg]
    # print(neg)
    for i in range(k):
        neg2.append(neg[i])
    neg2.reverse()
    for i in neg2:
        n_arr.append(arr[i])
    for i in arr:
        if i not in n_arr:
            n_arr.append(i)
    print(n_arr)
    # for i in range(len(neg)):




rotate([1,2,3,4,5],2)