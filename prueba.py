


def organizeNums(numString):
    numArray = [] 
    for i in numString.split(', '):
            numArray.append(int(i))
    
    numArray.sort()
    return numArray
    

print(organizeNums('3, 4, 1, 7, 9'))

# print(organizeNums([4,19,2,5,6]))


def organize(numsString):
    arr = list(map(int, numsString.split(',')))
    arr.sort()
    return arr 

# print(organize('3, 4, 1, 7, 9'))
    





    