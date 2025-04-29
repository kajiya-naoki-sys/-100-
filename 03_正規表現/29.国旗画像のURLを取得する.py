import requests
import pandas as pd
import re

link = '/workspace/03_正規表現/jawiki-country.json'
df = pd.read_json(link, lines=True)
uk = df[df['title'] == 'イギリス']['text'].values
r = uk[0]
#https://www.javadrive.jp/python/regex/index17.html#section5 を参照.
#re.MULTILINEで.を使って複数行拾える. re.DOTALLdeで[.]に改行を含めることができる.
pattern = re.compile('^\{\{基礎情報 国(.*?)\n\}\}$', re.MULTILINE+re.DOTALL)
r = re.findall(pattern, r)
ls = r[0].split('\n')
dec = {}
for i in ls:
    pattern = re.compile('\|(.+?)\s*=\s*(.+)')
    r = re.findall(pattern, i)
    if r:
        pattern = re.compile('\'{2,}(.+)\'{2,}')
        dec[r[0][0]] = re.sub(pattern, '\\1', r[0][1])
        pattern = re.compile('\[\[')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])
        pattern = re.compile('\]\]')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])
        pattern = re.compile('\[\[ファイル(.+)\]\]')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])
        pattern = re.compile('<.+?>')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])
        pattern = re.compile('[\{\[]+.*?[\}\]]+')
        dec[r[0][0]] = re.sub(pattern, '', dec[r[0][0]])

uk_flag = dec["国旗画像"]
uk_flag = uk_flag.replace(" ", "_")
print(uk_flag)
print()
#Cookieを取得するための変数.
S = requests.Session()
URL = "https://www.mediawiki.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop":"url",
    "titles": "File:"+uk_flag
}

#Cookieを取得する.paramsはクエリストリンクのこと.
#クエリストリンクとはより明確にアクセスを解析するのに必要.
R = S.get(url=URL, params=PARAMS)
#JSONデータの取得.
DATA = R.json()
print(DATA)
print()
#DATAのquery>pages>-1>imageinfo>0番目の配列>url にアクセスする.（imageinfoだけリストであることに注意）
uk_flag_url = DATA["query"]["pages"]["-1"]["imageinfo"][0]["url"]
print(uk_flag_url)