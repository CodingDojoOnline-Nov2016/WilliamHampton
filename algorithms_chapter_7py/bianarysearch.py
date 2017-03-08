# given an aray return wether the array contains that value

array = [1,2,3,4,5,6]

def arrayfunction(arr, val):
    for i in range(0,len(arr)):
        if i == val:
            print 'True'
            return True
    print 'False'
    return False

arrayfunction(array, 9)
arrayfunction(array, 3)

    
