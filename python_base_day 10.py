#값을 입력하기
a=input('숫자를 하나 입력하세요. : ')
b=input('숫자를 하나 입력하세요. : ')
print(a+b)

#뭔가 이상하다?
a=int(input('숫자를 하나 입력하세요. : '))
b=int(input('숫자를 하나 입력하세요. : '))
print(a+b)

#두 개의 값을 입력 받기
a,b=input('숫자를 두 개 입력하세요. : ').split()
print(a,b)

#input은 str타입으로 저장하는 것!
a,b=input('숫자 두 개를 입력하세요: ').split()
a=int(a)
b=int(b)
print(a+b)

#int 변환이 귀찮아!
a,b=map(int, input('숫자 두 개를 입력하세요: ').split())
print(a+b)
