'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :파일 입출력 write()메소드 사용법
'''

#파일을 open()
f = open("test.txt", "w",encoding="utf-8")

for i in range(1, 11):
    f.write(f"{i}번째 메시지입니다.\n")

f.close()