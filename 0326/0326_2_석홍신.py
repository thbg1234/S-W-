'''
작성일:2024.3.26
작성자:컴퓨터공학부 202195056 석홍신
설명:2개 정수를 입력받아 두 수의 크기를 비교하는
    프로그램을 작성하싱ㅅ
    
    두 수가 갈다
    천번째 수가크다
    두번째 수가크다

    두 개의 정수를 입력받는,num2,num2
    두 수가 같아요?만약 두 수가 갈다면
        2-1num1,num2,는 같습니다
        아니면,
        num1>num2?
        num>num1?
         
'''
num1 = int(input("첫번쩨 수 입력"))
num2 = int(input("두번쩨 수 입력"))
if num1==num2:
    print(f"첫번쩨 수{num1}과 두번째 수 {num2}는 같아")
elif num1>num2:
    print("num2>num1")
else :
    print("num1<num2")








