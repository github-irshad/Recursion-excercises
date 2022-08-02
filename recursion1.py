def list_sum(arr):
    sum=sum+list_sum(arr[i])
    return sum

arr=[1,2,3,4,5]
print(list_sum(arr))