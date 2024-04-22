# 初始化变量  
total_sum = 0  
even_count = 0  
  
while even_count < 2:  
    num = int(input("숫자를 입력하십시오: "))  
    total_sum += num  
      
    if num % 2 == 0:  
        even_count += 1  
          
        if even_count == 2:  
            total_sum -= 2 * num  
  
print("합은:", total_sum)