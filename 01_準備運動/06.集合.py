def biGram(str):
    s = ''
    for i in range(len(str) - 2 + 1):
        s += str[i:i+2]
    return s

str1 = 'paraparaparadise'
str2 = 'paragraph'
X = biGram(str1)
Y = biGram(str2)

#集合に変換
X = set(X)
Y = set(Y)

#和集合
print(X | Y)

#積集合
print(X & Y)

#差集合
print(X - Y)

#検索
print('se' in X)
print('se' in Y)