'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :파일 입출력 read()메소드 사용법

'''

f = open("test.txt", "r", encoding="UTF-8")
text = f.read() 
print(text)
f.close()