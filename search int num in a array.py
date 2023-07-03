#int search(int[]a,int number)
#search for the int number in array a. If found, return its position/index. Assume there are n numbers in the array

def search(a, number):
    for i in range(len(a)):
        if a[i] == number:
            return i
    return -1


arr = [2, 5, 8, 10, 15, 20]
num_to_find = 10
index = search(arr, num_to_find)
print(index)

num_not_found = 25
index_not_found = search(arr, num_not_found)
print(index_not_found)
