def main():
    # d=input("enter the direction[left(l),right(r)]:")
    n=int(input("enter the size of array:"))
    k=int(input("enter the no by which you want to rotate:"))
    arr=[]
    for i in range(n):
        a=int(input(f'element {i+1}:'))
        arr.append(a)
    print("Array:",arr)
    rotate(arr,k)

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
    print('Rotated Array:',n_arr)

if __name__=='__main__':
    main()

# just a trial
# s='06 7 25'
# arr1=[]
# for i in (s.split(' ')):
#     arr1.append(i)
# print(arr1)
