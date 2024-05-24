'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :for반복문을 이용하여 읽어 오기
'''


with open("test2.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)