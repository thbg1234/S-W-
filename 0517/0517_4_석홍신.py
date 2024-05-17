'''
작성일:2024.5.17
작성자:컴퓨터공학부 202195056 석홍신
설명 :1~45 사이에 6개 번호
'''

import random

print("로또 번호 생성 - 리스트")

lotto = list()

i = 0
while True:
    lotto.append(random.randint(1,45))
    i +=1
    if len(lotto)==6:
        break

print("이번주 로또 번호:",sorted(lotto))

print()
print("로또 번호 생성 - 세트")

lotto = set()

i=0
while True:
    lotto.add(random.randint(1,45))
    i+=1
    if len(lotto) == 6:
        break
print("이번주 로또 번호:",sorted(lotto))