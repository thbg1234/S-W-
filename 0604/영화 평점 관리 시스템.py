'''
[문제 분석]
    1. 함수를 만들어 사용자가 입력한 사용자 이름, 영화 이름, 평점을 기록한다
    2. 지정된 영화 찾기, 출력점수 및 평균점수
[알고리즘]
    1.  1.1.함수 만들기, 사용자가 입력한 이름, 영화 이름, 채점 받기
        1.2.사용자가 입력한 정보를 목록에 기록
    2.  2.1.사용자가 입력한 영화 이름을 찾는 함수를 만듭니다
        2.2.검색된 영화의 점수를 출력합니다
        2.3.평균점을 계산하다
'''


movies = []

def Movie_ratings():
    customer_name = input("고객의 이름을 입력하십시오: ")
    movie_name = input("영화 이름을 입력하십시오: ")
    score = int(input("점수(1~5)를 입력하십시오: "))
    if score < 1 or score > 5:
        print("에러, 점수(1~5)를 입력하십시오!")
        return
    else:
        movies.append((customer_name, movie_name, score))

def output_movies(o_movie):
    movie_scores = []
    for movie in movies:
        if movie[1] == o_movie:
            movie_scores.append(movie[2])
    
    if not movie_scores:
        print("해당 영화의 평점이 없습니다.")
    else:
        print(f"{o_movie} 영화의 모든 평점: {movie_scores}")
        average_score = sum(movie_scores) / len(movie_scores)
        print(f"{o_movie} 영화의 평균 평점: {average_score}")

while True:
    Movie_ratings()
    continue_input = input("추가 평가를 계속하시겠습니까? (y/n): ")
    if continue_input.lower() != 'y':
        break

print(movies)
o_movie = input("점수를 보려는 영화 이름을 입력하십시오: ")
output_movies(o_movie)
