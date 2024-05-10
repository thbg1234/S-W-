'''
작성일:2024.5.10
작성자:컴퓨터공학부 202195056 석홍신
설명 :1~100정수형 난수 10개 생성하여 리스트에 저장하고
목록에 최대값과 최소값을 출력하고 목록의 총 오름차순으로 목록을 정렬합니다.

'''

import random

num = []
for i in range(10):
    num.append(random.randint(1,100))
    
print("생성된 리스트:",num)
print("최대값:",max(num))
print("최소값:",min(num))
print("합계:",sum(num))

num.sort()   #从小到大排序
print("오름차 정렬:",num)
