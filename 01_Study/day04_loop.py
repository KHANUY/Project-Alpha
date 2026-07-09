#1단계 for문 기본
#for문은 정해진 횟수만큼 반복할 때 좋다.
for i in range(5):
    print("안녕하세요")
    print(i)#i는 0부터 4까지 반복되면서 출력됨

for i in range(5):
    print(i+1, "세트 운동 완료")

count = int(input("몇 세트 운동을 하시겠습니까?"))

for i in range(count):
    print(i + 1, "세트 완료")

#2단계 while문 기본
#while문은 조건이 참인 동안 계속 반복할 때 사용한다.

count = 1

while count <=5:
    print(count, "회 반복")
    count = count + 1 # 이 부분 없으면 숫자가 안 늘어나서 무한 반복

workout_name = input("운동 이름을 입력하세요 : ")
workout_set = int(input("몇 세트 할까요?"))
count =1

for i in range(workout_set):
    print(workout_name,i+1,"완료(for)")
print("오늘 운동 끝!")

while count<=workout_set:
    print(workout_name,workout_set,"완료(while)")
    count = count + 1