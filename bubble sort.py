arr=[1,27,52,63,17,78,42,10,72,58]
print("\tBubble sort")
print("\nBefore sorted:",arr)
for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("\nAfter sorted:",arr)