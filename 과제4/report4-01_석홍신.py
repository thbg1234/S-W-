
rate_per_30_minutes = 2100  
time_given = 30  
  
target_time = 45  
  
characters_in_target_time = (rate_per_30_minutes / time_given) * target_time  
  
answer = int(characters_in_target_time)  
  
print(f"{target_time}분 내 {answer}자를 입력할 수 있습니다.")