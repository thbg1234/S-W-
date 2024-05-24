'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :readline()메소드 사용법
        주로 while 반복문을 함께 사용
'''

with open("test2.txt","r",encoding="UTf-8") as f:
    while True :
        line = f.readline()
        print(line)
        
        if line == "":
            break