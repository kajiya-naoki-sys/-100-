str = 'stressed'
list = list(str)
newList = []
for i in reversed(list):
    newList.append(i)

newStr = ''
for i in newList:
    newStr += i
print(newStr)