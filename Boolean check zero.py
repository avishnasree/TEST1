#Check if the array number list has one and only one zero in it, only use a single for loop. Assume there are n numbers in the array
def single_zero(arr):
    count_zero = 0

    for num in arr:
        if num == 0:
            count_zero += 1
            if count_zero > 1:
                return False

    return count_zero == 1
arr1 = [1, 2, 0, 3, 4]
print(single_zero(arr1))

arr3 = [1, 2, 3, 4]
print(single_zero(arr3))

