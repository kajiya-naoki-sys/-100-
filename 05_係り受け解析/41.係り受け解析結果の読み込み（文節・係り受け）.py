class Morph:
    def __init__(self, morphs) -> None:
        surface = morphs.split('\t')
        # print(surface)
        attr = surface[1].split(',')
        self.surface = surface[0]
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]

# Chunkは文節を表すクラス
# 文節は,"*"が先頭(j[0])に入っているもの
class Chunk:
    def __init__(self, morphs, dst) -> None:
        #?作成する変数は,"morphs","dst","srcs"の3つ.
        self.morphs = morphs
        self.dst = dst
        self.srcs = []
        

link = '/workspace/05_係り受け解析/ai.ja.txt.parsed'
with open(link) as f:
    text = f.read().split('EOS\n')

morphs =[]
sentence_chunk=[]
chunk_list=[]
for i in text:
    i = i.split('\n')
    if(len(i) == 0 or i[0] == ''):
                continue
    for j in i:
        if j == '':
            continue
        elif j[0] == '*':
            if len(morphs) > 0:
                chunk_list.append(Chunk(morphs, dst))
            dep = j.split(' ')
            # print(dep)
            dst = dep[2][:-1]
            morphs = []
            continue
        morphs.append(Morph(j))
    chunk_list.append(Chunk(morphs, dst))
    for k, c in enumerate(chunk_list):
        print(k, c)
        if c.dst != "-1":
            chunk_list[int(c.dst)].srcs.append(k)
    sentence_chunk.append(chunk_list)
    chunk_list=[]
    morphs=[]
print(sentence_chunk)
print("\n-----------------------------------------------------------------\n")
for c in sentence_chunk[1]:
    print([m.surface for m in c.morphs], c.dst, c.srcs)