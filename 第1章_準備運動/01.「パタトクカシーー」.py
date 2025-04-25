str = 'パタトクカシーー'
#スライスのstepを使用して奇数のみを取得.
list = list(str)
newList = list[::2]
newStr = ''
for i in newList:
    newStr += i
print(newStr)