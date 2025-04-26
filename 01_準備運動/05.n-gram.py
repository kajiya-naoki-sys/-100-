#n-gramとは（https://zero2one.jp/ai-word/n-gram/#:~:text=n%2Dgram%E3%81%A8%E3%81%AF%E3%80%81%E5%8D%98%E8%AA%9E,n%2Dgram%E3%81%A8%E5%91%BC%E3%81%B3%E3%81%BE%E3%81%99%E3%80%82）
def nGram(n, str):
    l =[]
    for i in range(len(str)- n + 1):
        l.append(str[i:i+n])
    return l

str = 'I am an NLPer'
#spritで空白ごと（単語ごとに）カット.
print(nGram(2, str.split()))
print(nGram(2, str))