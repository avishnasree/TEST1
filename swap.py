#  int swap(int a, int b)
# swap two numbers without using 3rd number
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


a = 100
b = 555
a,b=swap(a,b)
print(a,b)

