str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
word = []
bufferStr = ''
ans = []
for i in str:
    if(i != (' ' or ',' or '.')):
        bufferStr += i
    else:
        word.append(bufferStr)
        bufferStr = ''
for i in word:
    ans.append(len(list(i)))
print(ans)