'''
사용자가 입력한 문장에서 몇 개의 공백을 인쇄하십시오.
그런 다음 공백을 제거한 문장을 인쇄합니다.

[알고리즘]
1. 문장 입력
2. 몇 개의 공백 인쇄
3. 공백을 삭제한 글 인쇄
'''
text = input("문장을 입력하세요:")
print("문장에서 스페이스바가 몇 개 인가?",text.count(''))
print("문장에서 스페이스 삭제",text.replace(' ',''))