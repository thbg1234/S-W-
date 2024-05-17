'''
작성일:2024.5.17
작성자:컴퓨터공학부 202195056 석홍신
설명 :아레와 같이 두 개의 튜플을 생성하고,
    튜플로부터 하나의 리스트를 새성하는 프로그렘을 작성하시오
'''

fruit = ('사과','배','파인애플','포도')
price = (5000,7000,4500,6000)

fp_list = []
#fp_tuple=()
for i in range(len(fruit)):
    fp_list.append(fruit[i])
    fp_list.append(price[i])
    #fp_tuple.append(fruit[i])
    

print("과일 목록:",fruit)
print("과일 가겨:",price)
print("과일 별 가격 리스트",fp_list)