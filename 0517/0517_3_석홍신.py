'''
작성일:2024.5.17
작성자:컴퓨터공학부 202195056 석홍신
설명 :세트:중복을 허용하지 않는다
'''

num = set()

num1 = {2,1,3}
print("num1 :",num1)

num2 = set([1,2,3,1,2])
print("num2:",num2)

text1 = set("abcda")
print("text1:",text1)

num3 = {2,1,3}

if 1 in num3:
    print("1이 세트에 있습니다.")
    
num4 = {9,1,2,5,4,1,3,7,6,5}
print("num4:",num4)

for num in num4:
    print(num,end = ' ')
    
print()
num4.add(100)
print("num3(100추가): ",num4)

for num in sorted(num4):
    print(num,end = ' ')
    
print()

num4.remove(100)
print("num4(100삭제)",num4)

print("num4의 길이:",len(num4))

print("num4의 최대값:",max(num4))
print("num4의 최소값:",min(num4))
print("num4의 합계:",sum(num4))

A = {1,2,3}
B = {3,4,5}

print("A | B = ",A | B)

print("A | B = ",A.union(B))

print("A & B = ",A & B)

print("A & B = ",A.intersection(B))

print("A - B = ",A - B)

print("A - B = ",A.difference(B))

print("A ^ B = ",A ^ B)