# int findsmallOrBig(int[]a)
#if an array is a=[1,2,4,32,12,6,8] the biggest number is 32 and the smallest number is 1


a = [1, 2, 4, 32, 12, 6, 8]
def findsmallOrBig(a):
    if not a:
        return None, None

    smallest = largest = a[0]

    for num in a:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest

smallest_num, largest_num = findsmallOrBig(a)
print("Smallest:", smallest_num)
print("Largest:",largest_num)