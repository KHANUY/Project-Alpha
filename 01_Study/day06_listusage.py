#append() : 맨 마지막에 덧붙이다, 첨부하다
a = [3,2,1]

a.append(4)

a.append([5,6])
#a.sort() 는 정렬함수이지만, 리스트가 요소로 들어가면 정렬이 불가능
#숫자, 문자 등을 순서대로(오름차순) 정리해준다.
print(a)

a.reverse()#reverse는 리스트 배열?을 그대로 뒤집어줌.

print("reverse : ",a)

#index : 리스트에 있는 값의 위치값을 리턴 뭐 찾을 때 좋을 듯..

b = a.index([5,6])
c = a.index(3)
print("index : ",b)
print("숫자 3의 위치 : ",c,"번째")

#insert(a,b) : a번째 위치에 b를 삽입. 삽입 되는 것이지 본래 있던
#위치의 요소가 사라지는게 아니고 한 칸씩 뒤로 밀림.

a = [1,2,3]
print(a)
a.insert(0,4)
print("insert : ",a)

#remove(x) : 리스트를 왼쪽부터 세나가서 가장 먼저 만나는 x를 삭제

a = [1,2,3,4,2]
print("new a :",a)
a.remove(2)
print(a)

#pop() : 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제.

b = a.pop()
print(a)
print("pop한거 b에다 넣기 :",b)
a.pop(1)#a[1] 요소 값 리턴하고 삭제.
print(a)

#count(x) : 리스트 안에 x값이 몇 개 있는지 조사하여 그 개수 리턴
a = [1,2,3,2,1,4]
b = a.count(2)
print("count:",b)

#extend([x,y]) : 리스트 만을 원래의 리스트에 더한다.
a = [1,2,3]
a.extend([4,1])
print(a)
b = [5,6]
a.extend(b)
print(a)

if 5 in a:
    d = a.index(5)
    print("5가 존재합니다.")
    print("5의 위치 :",d)

#len() : 길이(length)를 구하는 함수.

workouts = ["벤치프레스", "스쿼트", "데드리프트"]
print(len(workouts))

name = "Bench"
print(len(name))

for i in range(len(workouts)):
    print(workouts[i])

print(f"총 운동 개수 : {len(workouts)}개")

foods = ["닭가슴살", "계란", "고구마", "바나나"]
print(len(foods))
print(foods[len(foods)-1])

workouts = ["벤치프레스","스쿼트"]
workouts.append("데드리프트")
workouts.append("숄더프레스")

print(len(workouts))
print(workouts[2])
print(workouts[len(workouts)-2])
