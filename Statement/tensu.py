kor = int(input("국어 점수를 입력해주세요 : "))
eng = int(input("영어 점수를 입력해주세요 : "))
math = int(input("수학 점수를 입력해주세요 : "))

total = kor + eng + math
avg = total / 3.0

print("총점 : ", total)
print("평균 : ", avg)

if avg >= 90 : 
    print("수")
elif avg >= 80 :
    print("우")
elif avg >= 70 :
    print("미")
elif avg >= 60 :
    print("양")
else :
    print("가")
