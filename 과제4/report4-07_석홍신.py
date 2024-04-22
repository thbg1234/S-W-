student_count = 0  
  
while True:  
    score1 = int(input("첫 번째 과목의 성적을 입력하십시오.: "))  
    score2 = int(input("두 번째 과목의 성적을 입력하십시오: "))  
    score3 = int(input("세 번째 과목의 성적을 입력하십시오: "))  
    if score1 == 0 and score2 == 0 and score3 == 0:  
        print(f"합계{student_count}합계 인 처리 성적")  
        break  
      
    total_score = score1 + score2 + score3  
    average_score = total_score / 3  
       
    student_count += 1  
    print(f"{student_count}명 학생:종점는 {total_score}，평균은{average_score:.2f}")