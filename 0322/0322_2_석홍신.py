'''
작성일:2024.3.22
작성자:컴퓨터공학부 202195056 석홍신
설명:단순 if 작성하기
    정수를 입력받아 양수인지 음수인지 판단하시오.
    입력 받은 정수가 양수이면 "00은 양수입니다."
    입력 받은 음수가 양수이면 "00은 음수입니다."
    상관없이 "프로그램 종료."출력한다.

'''

num = int(input("수자를 입력하세요:"))

if num>0:
    print("{}는 양수입니다".format(num))
if num<0:
    print("{}는 음수입니다".format(num))
print("프로그램 종료.")