# create a function to remove duplicates of numbers in an array

def remove(arr):
    arr2 = [arr[0]]
    for i in range(0,len(arr)):
        for x in range(0,len(arr2)):
            if arr2[x] == arr[i]:
                break
                
            if arr[x] == len(arr2):
                arr2.append(arr[i])

    print arr2
    return arr2
array = [1,2,3,1,2,5]

remove(array)
