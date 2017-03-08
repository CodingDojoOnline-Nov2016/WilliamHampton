

array = [1,2,[3,4],5]

def flatten(arr):
    arr2 = []
    for i in range(0,len(arr)):
        if isinstance( arr[i], ( int, long ) ) == True:
            arr2.append(arr[i])
        else:
            for x in range(0, len(arr[i])):
                arr2.append[i][x]
    print arr2
    return arr2

flatten(array)
