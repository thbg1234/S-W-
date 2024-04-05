'''
작성일:2024.4.2
작성자:컴퓨터공학부 202195056 석홍신
    설명 :1~10합 출력하시오

    1.합계 sum = 0으로 초기화
    2.숫자는 1부터
    3.숫자는 10까지 반복
        3-1.sum = sum+num
        3-2.num = num+1
    4.print
'''
num = 1
sum = 0
while (num<=10):
    sum+=num
    num+=1
print("1부터 10까지 함은{}입니다.".format(sum))