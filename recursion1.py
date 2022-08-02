def list_sum(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return arr[0] + list_sum(arr[1:])


arr=[10]
print(list_sum(arr))