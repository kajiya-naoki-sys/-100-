#selfはMorphのこと. [Morphクラス型の変数].surface などで呼び出せる.今回はmorphリストの要素それぞれ.
class Morph:
    def __init__(self, morph):
        surface= morph.split('\t')
        #print(surface)
        attr = surface[1].split(',')
        self.surface = surface[0]
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]

link = '/workspace/05_係り受け解析/ai.ja.txt.parsed'
with open(link) as f:
    text = f.read().split('EOS\n')
result = []
#[[print('\n') for i in '\n'] * j for j in range(0, 10) ]
for i in text:
    i = i.split('\n')
    if i[0] == '' or len(i) == 0:
        continue
    #print('i=', i)
    for j in i:
        #print('j=', j)
        if j == '' or j[0] == '*':
            #print('continue', j)
            continue
        #?resultにクラスMorphによって形態素解析をかけた結果を代入する.
        result.append(Morph(j).__dict__)
    #?形態素解析の結果がまとまっているmorphsをリストに保持する.
    #result.append(morphs)

#print(result) 
for i in result:
    #varsで辞書型を自動で作成.
    print(i)