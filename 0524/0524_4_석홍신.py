'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :파일 입출력 writelines()메소드 사용법
'''


list1 = ['월요일\n','화요일\n','수요일\n','목요일\n','금요일\n','토요일\n','일요일\n',]
list2 = [1,2,3,4,5]


with open("test2.txt","w",encoding="UTF-8") as f:
    f.writelines(list1)
    f.writelines(list2)#리스트의 내용이 정수일 경우 오류가발생