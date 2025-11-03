word_file = open('CROSSWD.txt', 'r')

#print(type(word_file))

#for i in dir(word_file):
#    if '__' not in i:
#        print (i)

#print([x for x in dir(word_file) if '_' != x [0]])

#for i in range(15):
#    print(word_file.readline())

# words = []
# for i in word_file:
#     words.append(i.strip())
# print(words)

def more_than_20(file):
    openF = open(file)
    longWords = []
    for i in openF:
        shorten = i.strip()
        if len(shorten) > 20:
            longWords.append(shorten)
    return longWords


def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True
    
def uses_only(word, letters):
    for i in word:
        if i not in letters:
            return False
    return True

def all_uses_only(file, letters):
    openF = open(file)
    correct_words = []
    for i in openF:
        test = uses_only(i.strip(),letters)
        if test == True:
            correct_words.append(i.strip())
            print(correct_words)
        else:
            continue
    return correct_words



print(uses_only("horse", "rhose"))
print(uses_only("horse", "three"))

print(more_than_20('CROSSWD.txt'))

print(all_uses_only('CROSSWD.txt','zymurgy'))