str1 = 'パトカー'
str2 = 'タクシー'
newStr = ''
for i, j in zip(str1, str2):
    newStr += i + j
print(newStr)