'''
작성일:2024.4.12
작성자:컴퓨터공학부 202195056 석홍신
설명 :정수를 입력 받아 그 수가 소수인지 아닌지 판단하시오

'''


while True:
    num = int(input("수자를 입력하시오:"))
    a=True
    if num<1:
        print(f"{num}은 정수를 입력하시오.")
    elif num == 1:
        print(f"{num}은 소수가 아닙니다.")
    else:
        for i in range(2,num):
            if num%i == 0:
                a=False
                break
        if a==False:
            print(f"{num}은 소수가 아닙니다.")
        else:
            print(f"{num}은 소수입니다.")