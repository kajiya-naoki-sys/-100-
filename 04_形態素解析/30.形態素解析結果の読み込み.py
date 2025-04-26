path = '/Users/kajiyanaoki/Desktop/python/自然言語処理100本ノック/第4章_形態素解析/neko.txt.mecab'
#!with文は、ある作業を始める前と終わった後に自動的に何かを行うための便利な機能.
#?[with open() as [ファイルの変数名]]でファイルを開いた後自動的に閉じてくれる.
with open(path) as f:
    text = f.read().split('\n')
result = []
for i in text:
    #文末になったら.
    if i == 'EOS':
        #countinueで強制的に次のループに入る.
        continue
    if i == '':
        continue
    #!MeCubで解析するとで出力される.
    #そのためタブキーでsplitしてls[0]に表層系、ls[1]にタブ以降を入れる.
    ls = i.split('\t')
    #解析した品詞をさらに分解する.
    #?ls = [表層系,[tmp]], tmp = [[品詞],[品詞再分類1],[品詞再分類2],[品詞再分類3],[活用型],[活用形],[原形],[読み],[発音]]になっている.
    tmp = ls[0].split(',')
    d = {}
    #「各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納」より.
    d = {'surface': ls[0], 'base': tmp[6], 'pos': tmp[0], 'pos1': tmp[1]}
    result.append(d)

print(result)