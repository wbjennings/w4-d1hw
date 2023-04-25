def even_or_odd(number):
    if number % 2 == 0: #O(1) time complex (constant)
        return 'Even'
    else:
        return 'Odd'
#even_or_odd(5)



def grow(arr):
    multiply = 1
    for number in arr: #O(n)
        multiply *= number
    return multiply
#grow([1,2,3,4])



def find_uniq(arr):
    unique_number = set(arr) #O(n)
    for number in unique_number:
        count = arr.count(number)
        if count == 1:
            return number
#find_uniq([1,1,1,1,2])