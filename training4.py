# -*- coding: utf-8 -*-
import re

#URL 文字列を受取、そのパラメータ（?から始まる文字列部分）を排除する 関数 eliminate_parameters をつくれ
def eliminate_parameters(url):
    return re.sub("\?.*$", "", url)

#パラメータつきのURLを受取、パラメータの辞書を作る関数 create_parameter_dict をつくれ★
def create_parameter_dict(url):
    dict = {}
    para =re.findall("(?<=\?).*$", url)
    split_and = re.split("&", para[0])
    for x in split_and:
        split_equal = re.split("=", x)
        dict[split_equal[0]] = split_equal[1]
    return dict

'''
細かい話かもですが、変数名が少しわかりにくいと感じました
split_and は 動詞っぽいので関数名に感じます

parameter_whole_string =re.findall("(?<=\?).*$", url)
parameter_string_list = re.split("&", para[0])

key_value_pair = re.split("=", x)

みたいな感じで、変数名から型（stringなのか、listなのか、tupleなのか）が連想できる名前がオススメです！
'''

#次のような意地悪メールアドレスを正しいメールアドレスになおして返す関数 correct_email_addres を作れ★★
def correct_email_addre(email):
    replace_at = re.sub("(\[at\]| at | \[at\] |\_at\_| \_at\_ |\_atmk\_| \_atmk\_ )", "@", email)
    replace_dot = re.sub("(\[dot\]| dot | \[dot\] |\_dot\_| \_dot\_ )", ".", replace_at)

    return replace_dot


'''

(\[at\]| at | \[at\] |\_at\_| \_at\_ |\_atmk\_| \_atmk\_ )
という書き方はわかりやすいのですが、

新たに@のダミーとしてatmarkやAT とかが出てきた場合、
その周りにつくパターン [ や スペースや ( や _などの数 だけ正規表現のパターンを足さなければいけないことになります

(\[|_| | _)(at|atmk|atmark|AT|ATMARK)(\]|_| |_ )
みたいに、組み合わせで書いたほうが効率的です（↑は動作未確認）

それと問題のテスト例には書いてはいませんでしたが、
hiroki_dot_com@gmail.com
みたいなアドレスはありえますが、誤変換されてしまいます

実際に使うには要修正ですが、問題的には合格です
'''
