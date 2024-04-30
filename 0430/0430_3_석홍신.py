'''
작성일:2024.4.30
작성자:컴퓨터공학부 202195056 석홍신
설명 :사용자로부터 시작값과 끝값을 입력받아
3의 배수를 제외한 모든 숫자의 합을 출력하시오
    
[문제분석]
    3의 배수 = 3으로 나누어 나머지가 0인 수
    3의 배수가 아닌 수 = 3으로 나누어 나머지가 0인 수
    
    입력받은 두 수 사이를 반복
'''


num1 = int(input("시작값을 입력 하시오:"))
num2 = int(input("끝값을 입력 하시오:"))
sum = 0
if num1<num2:
    for num in range(num1,num2+1):
        if num%3 !=0:
            sum += num
            
else:
    for num in range(num2,num+1):
        if num%3 !=0:
            sum +=num
print(f"{num1}~{num2} 합은 {sum}입니다.")


sum = 0

if num1>num2:
    temp = num1 
    num1 = num2
    num2 = temp

for num in range(num1,num2+1):
    if num%3 != 0:
        sum +=num

print(f"{num1}~{num2} 합은 {sum}입니다.")