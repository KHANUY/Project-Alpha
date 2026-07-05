print("안녕하세요!")

name = input("이름을 입럭하세요 : ")
print("반갑습니다, ",  name)

height = float(input("키(cm) : "))
weight = float(input("몸무게(kg) :"))

height = height / 100

print(height)
print(weight)

bmi = weight / (height **2)
print ("BMI : " , round(bmi,2))

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
