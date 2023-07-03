#Check if all characters in the string are unique
def unique_characters(string):
    seen_characters = set()

    for char in string:
        if char in seen_characters:
            return False
        seen_characters.add(char)

    return True
string1 = "mobile"
print(unique_characters(string1))

string2 = "calculator"
print(unique_characters(string2))

