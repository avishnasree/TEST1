#replace every space in the string sentence with "--" and return the string
def replaceSpace(sentence):
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            sentence[i] = '-'
    return ''.join(sentence)
sentence = "I am a doctor"
sentence_chars = list(sentence)
replaced_sentence = replaceSpace(sentence_chars)
print(replaced_sentence)
