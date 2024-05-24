'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :파일 입출력 write()메소드 사용법
'''

#파일을 open()
f = open("test.txt", "w",encoding="utf-8")

f.write("주가 메세지입니다")
f.close()