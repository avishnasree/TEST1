# int[] find _mismatch(int[]a,int[]b)
# if an array a list is [1,2,4,32,12,6,8]the biggest number b is [2,6,10,12,1417] return or print thw number which is present in a not b


a = [1, 2, 4, 32, 12, 6, 8]
b = [2, 6, 10, 12, 1417]
def find_mismatch(a, b):
    mismatch_numbers = []
    for num in a:
        if num not in b:
            mismatch_numbers.append(num)
    return mismatch_numbers


mismatches = find_mismatch(a, b)
print(mismatches)
