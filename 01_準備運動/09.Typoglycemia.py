import random

def temp(str):
    s = str.split()
    ans = []
    for i in s:
        if(len(i) > 4):
            top = i[1]
            end = i[-1]
            target = i[2:-2]
            changed = random.sample(target, len(target))
            #''.join()でlistの各要素を連結してstringに変換
            changed = ''.join(changed)
            ans.append(top + changed + end)
        else:
            ans.append(i)
    return ' '.join(ans)

str = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
print(temp(str))