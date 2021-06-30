# -*- coding: utf-8 -*-
print("モジア村へようこそ,今ではモンスター獣の領土です")
print("9人の死後，あなたはボスゲイルの巣に来ました")
hp_boss = 10
print("嵐の血液量：",hp_boss, ",戦う準備ができて!!")
for i in range(10):
    input_ni = int(input("すぐに番号1を入力して攻撃します!"))
    if input_ni == 1:
        hp_boss -= 1
        print("你击中了狂风,ゲイルの残りのHP:",hp_boss)
        if hp_boss == 0:
            print("リトルモー,おめでとう,風を打ち負かした")
