total_sum = 0    
start = 1   
end = 10  
  
while start <= 100:  
    for i in range(start, min(start + 10, 101)):  
        total_sum += i  
       
    if end <= 100:  
        print(f"{start}-{end} :{total_sum:04d}")  
      
    start += 10  
    end += 10  
  
print(f"1-100:{total_sum:04d}")