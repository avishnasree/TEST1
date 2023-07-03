#String removeDulicate(char[]a)
# Remove dulipicates character from the string and return a new string with no duplicate characters

def removeDuplicate(a):
    unique_chars = []

    for char in a:
        if char not in unique_chars:
            unique_chars.append(char)

    return ''.join(unique_chars)


a = "calculator"
result = removeDuplicate(a)
print(result)