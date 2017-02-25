# -*- coding: utf-8 -*-

#数字を入力として、その数字が偶数だったら文字列”even”, 奇数なら文字列”odd”を返す関数 judge_odd_even を作れ
def judge_odd_even(x):
    if x%2 == 0:
        print("even")
    else:
        print("odd")

'''
島田コメント

これは「文字列”odd”/"even"を返す関数」ではなく、「文字列"odd"/"even"をプリントする関数」です！
Pythonのコンソールだと、返されたものがプリントされるから紛らわしいですが

'''

#配列(リスト）list について、偶数の数字の数を返す関数 count_even を作れ
def count_even(list):
    count = 0
    for x in list:
        if x%2 == 0:
            count += 1
    return count

#第一引数に文字列、第二引数に文字列のリストをとって、リストの要素のいずれかに第一引数の文字が入っていたらTrue, そうでなければFalse を返す関数list_contains を作れ
def list_contains(string, list):
    if string in list:
        print("True")
    else:
        print("False")


'''
島田コメント

1と同様に、これは"True"/"False"という文字列をプリントする関数になってます
しかも True/Falseは 真偽値を表す bool型のリテラルなので、 "True" / "False"とも違います
以下例です。

>>> 10 > 0
True
>>> 10 < 0
False
>>> bool(1)
True
>>> bool(0)
False
>>> bool("False)
True
>>> 1 in [1,2,3]
True

'''
