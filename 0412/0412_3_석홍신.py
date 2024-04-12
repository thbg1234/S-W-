'''
작성일:2024.4.12
작성자:컴퓨터공학부 202195056 석홍신
    설명 :단을 입력받아 해당 구구단을 출력하시오
'''


dan = int(input("알고싶은 단을 입력하시오:"))
print(f"--{dan}단--")
for su in range(1,10):
    print(f"{dan} X {su} = {dan*su}")