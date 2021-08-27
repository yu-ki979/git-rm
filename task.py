# 1 変数の使い方
name1 = 'ねずこ'
name2 = 'ぜんいつ'
print(name1 + 'と' + name2 + 'は仲間です')

#２ if文の使い方
name2 = 'むざん'
if name2 == 'むざん':
    print(name1 + 'と' + name2 + 'は仲間ではありません')

#３ 配列の使い方
name=["たんじろう","ぎゆう","ねずこ","むざん"]
name.append("ぜんいつ")
print(name)

#４ for文の使い方
for cat in name:
    print(cat)

#５ 関数の使い方
def test():
    print("こんにちは")
test()

#５ 関数の使い方'
def color():
    print("red")
color()

#６ 引数を使う関数の使い方
def kimetu(name_list):
    
    if name_list in name:
        print(name_list + "は含まれます")
  
kimetu("ぎゆう")   
    


    

