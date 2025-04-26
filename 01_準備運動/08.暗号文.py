def cipher(str):
    s = ''
    for i in str:
        if('a' <= i and i <= 'z'):
            code = 219 - ord(i)
            s += chr(code)
        else:
            s += i
    return s

s1 = 'abcdefg'
s2 = cipher(s1)
s3 = cipher(s2)
print(s1 == s3)