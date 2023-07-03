# boolean checkWrongOrWrite(char[]a)
# Check whether the string contains more or equal to three vowels(a,e,i,o,u)if yes then string is false, else true

def WrongOrWrite(a):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for char in a:
        if char.lower() in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                return False

    return True


string1 = "Hello"
result1 = WrongOrWrite(string1)
print(result1)

string2 = "Banana"
result2 = WrongOrWrite(string2)
print(result2)
