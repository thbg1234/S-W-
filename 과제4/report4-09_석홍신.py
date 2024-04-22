user_input = int(input("사용자 입력: "))  
   
sum_of_multiples = 0  
n = 0   
   
while sum_of_multiples <= user_input:  
    n += 3  
    sum_of_multiples += n  
  
print(f"10을 넘었을 때의 값: {n - 3}")  
print(f"10을 넘었을 때까지의 총합계: {sum_of_multiples - n}")   
print(f"10을 넘었을 때까지 몇 번째 3의 배수인가: {n // 3}")  