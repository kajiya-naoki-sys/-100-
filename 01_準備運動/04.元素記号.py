str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
word = []
bufferStr = ''
for i in str:
    if(i != (' ' or '.')):
        bufferStr += i
    else:
        word.append(bufferStr)
        bufferStr = ''
count = 0
dict = {}
for i in word:
    count += 1
    if(count == 1 or count == 5 or count == 6 or count == 7 or count == 8 or count == 9 or count == 15 or count == 16 or count == 19):
        dict[i[:2]] = count
    else:
        dict[i[:1]] = count
print(dict)