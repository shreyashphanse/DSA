#largest number in array
def find_largest(arr):
    max_num=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_num:
            max_num=arr[i]
    print("largest:",max_num)

def main():    
    length=5
    arr=[]
    print('enter Elements of array:')
    for i in range(length):
        element=int(input())
        arr.append(element)
    print(arr)
    find_largest(arr)

main()