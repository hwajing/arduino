import requests
from os import getcwd

# https://github.com/hwajing/arduino/blob/master/helloworld.txt
# 上記URLからファイルをダウンロードする
# URL変更点　「raw.」の追加と、「blob/」を削除

# helloworld.txt
# hello world
#
# the end

# 取得した内容は以下ににある
# b'hello world\n\nthe end'
url = "https://raw.githubusercontent.com/hwajing/arduino/master/helloworld.txt"

r = requests.get(url)
print(r.content)

# directory = getcwd()
# filename = directory + 'somefile.txt'
# f = open(filename,'w')
# f.write(r.content)



