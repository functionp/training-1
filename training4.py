# -*- coding: utf-8 -*-
import re

#URL 文字列を受取、そのパラメータ（?から始まる文字列部分）を排除する 関数 eliminate_parameters をつくれ
def eliminate_parameters(url):
    print(re.sub("\?.*$", "", url))

#パラメータつきのURLを受取、パラメータの辞書を作る関数 create_parameter_dict をつくれ★
def create_parameter_dict(url):
    dict = {}
    para =re.findall("(?<=\?).*$", url)
    split_and = re.split("&", para[0])
    for x in split_and:
        split_equal = re.split("=", x)
        dict[split_equal[0]] = split_equal[1]
    print(dict)

#次のような意地悪メールアドレスを正しいメールアドレスになおして返す関数 correct_email_addres を作れ★★
def correct_email_address(email):
    replace_at = re.sub("(\[at\]| at | \[at\] |\_at\_| \_at\_ |\_atmk\_| \_atmk\_ )", "@", email)
    replace_dot = re.sub("(\[dot\]| dot | \[dot\] |\_dot\_| \_dot\_ )", ".", replace_at)

    print(replace_dot)
