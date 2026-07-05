print("안녕하세요!")

name = input("이름을 입럭하세요 : ")
print("반갑습니다, ",  name)

height = float(input("키(cm) : "))
weight = float(input("몸무게(kg) :"))
#float()함수는 문자열이나 정수를 실수(부동 소수점)로 변환하는 데 사용
#되는 내장 클래스이다. 주로 input()함수로 입력받은 계산 가능한 숫자로
#바꾸거나, 정수형(int)데이터를 실수형으로 변환할 때 활용한다.

height = height / 100

print(height)
print(weight)

bmi = weight / (height **2)
print ("BMI : " , round(bmi,2))
#round() 함수는 숫자를 지정된 소수점 자릿수(ndigits)만큼 반올림한다.
#자릿수를 생략하면 가장 가까운 정수를 반환한다.특히, 5를 반올림할 때
#앞자리가 짝수면 내림하고 홀수면 올림하는 오사오입방식을 사용한다.
if bmi>=25:
    print("비만")
elif bmi>23:
    print("과체중")
elif bmi>= 18.5:
    print("정상")
else:
    print("저체중")






''' a = 10
b = 18
c = 11

d = a*(b**2)+2*c
print(d)

food = 'Pythons"s favorite food is perl'
#문자열 안에 " 사용 시 ' '로 묶어주기
print(food)


say = " \"python is very easy\" "
#문자열 안에 " 사용 시 \"  방법도 있다.
print(say)

multiline = """ Life \nis too short
you need python"""
print(multiline)
#\n은 줄바꿈, 그 외에 한 번에 줄바꿈 하고 싶으면 """나 '''
# '''를 사용하면 된다.'''
'''print("="*50)
print("My Program")
print("="*50)
#문자에 *를 하면 그 문자를 *n 만큼 반복하라는 것임

d = "Life a"
len(d)
print(len(d))'''
