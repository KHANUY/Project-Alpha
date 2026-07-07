'''
# 1. if
age = 20

if age >= 20 :
    print("성인 입니다.")

if 조건 :
    실행할 코드

파이썬은 들여쓰기로 코드의 범위를 구분한다.

if True:
    print("안녕하세요")
    print("반갑습니다")

print("끝")


# 2. 비교 연산자 ==조건에는 대부분 비교 연산자가 들어간다.

print(10>5)  #true
print(10<5)  #false


=   대입
>   크다    
<   작다
>=  크거나 같다
<=  작거나 같다
==  같다
!=  다르다


# 3. else == 조건이 아니라면 실행

age = 17

if age >= 20 :
    print(" 성인")
else : 
    print("미성년자")

#4.elif == 조건이 여러개일 때 사용한다.

score = 85

if score >= 90 :
    print("A")

elif score >= 80 :
    print("B")

elif score >= 70 :
    print("C")
    
else :
    print("재시험")
#위에서부터 순서대로 검사하고, 처음 만족하는 조건 하나만 실행된다.

#5. 논리 연선자
# and == 둘 다 참이어야 한다.
age = 25
money = 10000

if age>= 20 and money >= 5000 :
    print("영화 보기")

# or == 하나만 참이어도 된다.

if age >= 20 or money >= 5000 :
    print("가능")

# not == 참과 거짓을 뒤집는다.
is_raining = False
if not is_raining :
    print("산책 가능")

#입력과 함께 사용하기
age = int(input("나이를 입력하세요 :"))

if age>= 20 :
    print("성인입니다.")
else :
    print("미성년자입니다.")


#연습 문제

human = int(input("나이를 입력해 주세요 : "))

if human >= 20 :
    print("성인입니다.")
else :
    print("미성년자입니다.")


#연습 2

user_score = int(input("점수 입력 :"))

if user_score >= 90 :
    print("A")

elif user_score >= 80 :
    print("B")

elif user_score >= 70 :
    print("C")

elif user_score >= 60 :
    print("D")

else :
    print("F")

print("학점입니다.")


'''
'''
if age >= 0 and age <= 13 :
    print("어린이입니다.")

elif age >= 14 and age <= 19 :
    print("청소년입니다.")

elif age >= 20 and age <= 64 :
    print("성인입니다.")

else :
    print("노인입니다.")
'''

'''

if 0 <= age <= 13:
    print("어린이입니다.")

elif 14 <= age <= 19:
    print("청소년입니다.")

elif 20 <= age <= 64:
    print("성인입니다.")

else:
    print("노인입니다.")
'''
'''
while True :
    age = int(input("나이를 입력하세요 : "))
    
    if age < 0:
        print("올바른 나이를 입력하세요.")
    else :
        break
if age <= 13:
    print("어린이입니다.")

elif age <= 19:
    print("청소년입니다.")

elif age <= 64:
    print("성인입니다.")

elif age >= 65:
    print("노인입니다.")
'''

#프로젝트 : BMI 계산기 + 운동 추천
'''
목표 
사용자에게 키(cm), 몸무게(kg)를 입력받는다.
BMI를 계산한 뒤
체중 상태와 운동 추천을 출력한다.
'''
height = (float(input("키를 입력하세요(cm) : ")))/100
weight = float(input("몸무게를 입력하세요(kg) : "))

bmi = weight / (height**2)

print(f"BMI : {bmi:.2f}") 
#print("BMI : ", round(bmi,2))


if bmi < 18.5:
    print("체중이 낮습니다.")
    print("운동 추천: 근력 운동 주 4회")
    print("식단 추천: 단백질 충분히 섭취 및 탄수화물 충분히 섭취.")
    print("특이사항 : 근력 운동 시 근비대를 위해 고중량 저반복 운동을 추천")
elif 18.5 <= bmi < 23:
    print("정상 체중입니다.")
    print("운동 추천: 근력 운동 주 4회, 유산소 운동 주 4회")
    print("식단 추천: 단백질 충분히 섭취 및 탄수화물 충분히 섭취")
    print("특이사항 : 정상 체중 유지에는 근력 운동과 유산소 운동을 병행하는 것이 좋습니다.")
elif 23 <= bmi < 25:
    print("과체중입니다.")
    print("운동 추천: 유산소 운동")
    print("식단 추천: 탄수화물 섭취를 줄이고 단백질 섭취를 늘립니다.")
    print("특이사항 : 유산소 운동을 통해 체지방을 줄이는 것이 좋습니다.")
else:
    print("비만입니다.")
    print("운동 추천: 유산소 운동")
    print("식단 추천: 탄수화물 섭취를 줄이고 단백질 섭취를 늘립니다.")
    print("특이사항 : 유산소 운동을 통해 체지방을 줄이는 것이 좋습니다.")