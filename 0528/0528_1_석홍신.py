'''
작성일:2024.5.28
작성자:컴퓨터공학부 202195056 석홍신
설명 :함수의 정의 및 호출
'''

print("::함수의 정의 및 호출::")

def print_3_time():
    print("안녕하새요")
    print("석홍신입니다")
    print("오늘은 화요일입니다")
    
print("함수호출 1")
print_3_time()

'''
    함수의 매개 변수
    함수를 호출할 때 값을 가지고 호출하는 경우
        그 값이 저장된 변수를 실 매개 변수라고 한다.
    함수가 호출 당하면 그 함수가 전해 받은 값을
        저장하는 변수를 형식 메개 변수라고 한다.
'''
print("메개 변수로 값을 전달하여 함수에서 결과 출력")

def print_n_time(value,n):
    for i in range(n):
        print(i,":",value)
        
print("함수호출 2")
print_n_time("석홍신",5)
            
            
'''
    함수의 값 반환
    return 문을 사용 하여 함수를 종료하고,결과를 돌려준다
    return이 없으면 반환되는 값이 없다
    
    원의 면적을 구하는 절차
    원 면적을 계산하는 영역을 함수로 작성합니다.
    함수는 원의 면적을 계산하고 결과를 반환합니다.
'''
print("원의 넓이 구하기")
def Area(r):
    result=r**2*3.14
    return result  #결과를 둘려준다
    
r = int(input("반지름을 입력하시오:"))
result = Area(r)
print(f"반지름이 {r}인 원의 넓이:{result:.1f}")

print(f"반지름이 {r}인 원의 넓이:{Area(r):.1f}")

    

