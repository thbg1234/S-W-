'''
작성일:2024.5.10
작성자:컴퓨터공학부 202195056 석홍신
설명 :튜플 =>한 번 생성되면 그 값을 고칠 수 없는 자료형
'''

colors1 = ('red','green','blue','orange')
print("colors1=",colors1)

print("생상 중 2,3,4번은?",colors1[1:4])
print("생상을 거꾸로 출력하면:",colors1[::-1])

colors = colors1+colors1
print("colors = ",colors)
print("colors1 * 10 = ",colors1*10)

colors2 = ('red','green','blue','orange','pink','white','white')
print("colors2 = ",colors2)

print("색상에서 'white' 개수는 ?",colors2.count('white'))

print("색상에서 'green'의 위치 ?",colors2.index('green'))

print("색상에서 'green'의 위치 ?",colors2.find('green'))

