'''
작성일:2024.5.17
작성자:컴퓨터공학부 202195056 석홍신
설명 :
'''

num = (4,1,3,4,6,5,7,8,5,1,4,6,0,1,2,7,8,9)
print("새성된 튜플:",num)

for i in range(len(num)):
    print(num[i],"의 개수:",num.count(num[i]))
    
print()
print("중복 제거하고 개수 찾기")

num_list = []

#튜플의 길이까지 반복하면서
#   1-1리스트에 숫자가 있는지 없는지 판단
#       만약에 숫자가 리스트에 있으면
#      1-1-1 페스
#   1-2 없으면
#       1-2-1. 개수 출력 하고 ,리스트에 추가.

for i in range(len(num)):
        if num[i] in num_list:
            continue
        else:
            print(num[i],"의 개수:",num.count(num[i]))
            num_list.append(num[i])

print()
print("없으면...")
num_list = []

for i in range(len(num)):
    if num[i] not in num_list:
        print(num[i],"의 개수",num.count(num[i]))
        num_list.append(num[i])