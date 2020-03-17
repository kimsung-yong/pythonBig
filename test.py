# 연산자
#   기본적인 +,-,*,%
#   a ** b a의 b승 값을 돌려준다
#   기타

# python의 자료형
#   문자열
#   숫자
#   리스트
#   딕셔너리
# 문자열
#   기본사항
#   문자열은 "" 또는 ''로 감싼다
#   특이사항
#   \' 또는 \"하면 감싸는 '',""가 아닌 '',"" 문자 자체를 나타 낸다
#   여러줄인 문자열 작성 방법
#   1) \n 계행코드
#   2) """ 3개를 사용해서 문장을 감싸면 된다

# 인덱싱과 슬라이싱
#   인덱싱이란 배열이나 리스트에 값을 추출하는것을 말한다.
#   ex) a = [1,2,3,4] 라고 설정했을때
#       a[0] 은 1의 값을 나타낸다
#       이것을 변수에 저장할려면 b = a[0]으로 나타낸수 있다
#   슬라이싱이란
#   배열 또는 리스트를 기준점을 잡아 나눠서 추출하는 방법
#   ex) a = [1,2,3,4]
#       a[0:2] 0번째 인덱스 부터 2개를 꺼낸다는 뜻이다. 수식으로 나타내면 0 <= a < 2 그러므로 값 '3'은 꺼내지지 않는다
#       a[:] a객체의 값을 전부 꺼낸다
#       a[:3] 처음부터 3번째 인덱스 까지 꺼낸다

# 문자 포메팅
#   문자 포메팅이란 문자열 내에 어떤 값을 삽입하는 방법을 말한다
#   ex) print("i eat %d apples" % 3)
#   %s 문자열
#   %d 정수형
#   %c 문자 한개
#   %f 부동소수
#   %% % 자체
#   (ex print("error is %d%%" %55) )
#   실행결과
#   error is 55%
#   특이사항 %s를 사용하면 어떤 타입이든 자동으로 형변환이 된다. 변수에 숫자 3을 대입하면 %d로 해석된다
#   메소드 종류 upper , count , find , index , join , lower , rstrip , strip , replace , split , swapcase
#   a.upper() 문자열 a를 모두 대문자로 바꾸어 준다.
#   a.count(x) 문자열 a중 x와 일치하는 것의 갯수를 반환한다.
#   a.find(x) 문자열 a중 x가 처음으로 나온 위치를 반환한다. 없으면 -1를 반환한다.
#   a.index(x) 문자열 a중 문자 x가 처음으로 나온 위치를 반환한다. 없으면 애러를 발생시킨다.
#   a.join(s)  s라는 문자열의 각각의 요소 문자 사이에 문자열 a를 삽입한다
#   a.lower() 문자열 a를 모두 소문자로 바꾸어 준다.
#   a.lstrip() 문자열 a의 왼쪽 공백을 모두 지운다.
#   a.rstrip() 문자열 a의 오른쪽 공백을 모두 지운다.
#   a.strip() 문자열 a의 양쪽 공백을 모두 지운다.
#   a.replace() 문자열 a의 s라는 문자열을 r이라는 문자열로 치환한다.
#   a.split([s]) 문자열 a를 공백으로 나누어 리스트값을 돌려준다.
#   a.swapcase() 문자열 a의 대문자는 소문자로, 손문자는 대문자로 각각 바꾸어 준다.

# 리스트 함수
#   a.append() 리스트에 요수 추가 - 리스트의 맨 마지막에 추가시킴
#   a.sort() 정렬
#   a.reverse() 인덱스 역순으로 한다.
#   a.index(x) x번째 값을 반환한다. 값이 있을 경우
#   a.insert(0,4) 0번쨰 자리에 4의 값을 삽입하라는 뜻이다
#   a.remove(x) x랑 같은 값이 리스트에 존재할경우 삭제한다. 주의 x는 인덱스 번호가 아니라 문자 그자체 이다.
#   a.pop() 리스트의 맨 마지막 요소를 반환후 리스트에서 제거한다.
#   a.count(x) 리스트 값 중에서 x가 몇개 있는지 조사후 반환
#   a.extend([x]) a의 리스트에 x리스트를 마지막에 추가시킨다.

# 딕셔너리
#   딕셔너리란 자바에 map과 같음
#   a,keys() 딕셔너리 a의 key들을 모아놓은 리스트를 돌려준다.
#   a.values() 딕셔너리 a의 value들을 모아놓은 리스트를 돌려준다.
#   a.item() 딕셔너리 a의 key,value들을 모아놓은 리스트를 돌려준다.
#   a.clear() 딕셔너리 a의 key,value 초기화 시킨다.
#   a.get(x) 딕셔너리 a의 key가 x인 것의 value를 돌려준다.
# 딕셔너리 예제
# dic = {'name': 'pey', 'phone': '0119993323', 'birth': 1118}
# 딕셔너리 접근법
# print(type(dic['birth']))
# print(dic['birth'])
# 딕셔너리 쌍 추가
# dic['address'] = '대전'
# 딕셔너리 요소 삭제
# del dic['name']
# 딕셔너리 전체삭제
# dic.clear()
# 딕셔너리 values 리스트로 반환
# dic.values()
# 딕셔너리 key,value 값 쌍 얻기
# dic.items()
# 딕셔너리 key값 확인
# print(dic.keys())


# 변수 리스트 복사
# ex) a=b(주소를 복사한다 그러므로 같은 주소를 가르키게 되므로 b를 변경하면 a도 변경된다) , a=b[:] , from copy import copy(카피 메소드 선언 후) a = copy(b)
# a와b의 비교 a와 b의 주소 비교 a is b 

# -----------------------------------------------------------------------------------------------------------------------------------------------------
#   파이썬 함수 및 for while if 사용시 주의 사항 파이썬은 줄맞춤이 중요하다
#   예를 들어 for 과 if가 중첩이 되어 있을경우 break위치에 따라 for의 break로 인식될수도 if의 break로 인식될수도 있다
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# if문
# if 조건문 :
# 실행문
# 실행문
# else
# 실행문
# 실행문

# if ~ elif문
# fi 조건문 :
# 실행문
# 실행문
#   elif 조건문 :
# 실행문
# 실행문
# else
# 실행문
# 실행문
# continue 처음으로 돌아간다
# pass 코드 해당 조건일때 아무것도 안하고 통과한다.

# while문
#   while 조건문 :
#         수행할 문장
#         수행할 문장
#         수행할 문장

# for문
#   for 변수 in 리스트(터플, 문자열):
#   수행할 문장
#   수행할 문장
#   수행할 문장

#   ex) 구구단

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end=' ')
#     print("\n")

# 함수
#   파이썬의 함수 구조
#   def 함수명(입력인수):
#   수행할 문장(ex return)
#   함수 호출 방법
#   리턴값을 받을 변수 = 함수명()
#   ex)입력변수의 갯수가 몇개가 되지 못할때
#   def sum(*args)
#   sum = 0
#   for i in args:
#   sum += i
#   return sum
# -----임의값과 원하는 연산방법을 입력받아 결과 값을 리턴시키는 사용자 함수
# def sum(ads, *args):
#     temp = 0
#     if ads == 'sum':
#         for i in args:
#             temp +=i
#         return temp
#     elif ads == 'mul':
#         temp = 1
#         for i in args:
#             temp *= i
#         return temp
# i = sum('mul', 1, 2, 3, 4)
# print(i)
# --------------------------------------------------------------------------------------------------------------------------------------
#   사용자 입력 함수
#   input()
#
# a = input("아무거나 입력")
# print(a)
# --------------------------------------------------------------------------------------------------------------------------------------
# 파일 읽고 쓰기
# 파일객체 = open("파일이름",'파일열기모드')
# 파일 열기모드(r - 읽기모드 w-쓰기모드 a-추가모드 : 파일의 마지막에 새로운 내용을 추가 시킬때 사용)
# 주의사항
# 파일을 쓰기 모드로 열게 되면 해당 파일이 존재할 경우 원래있던 내용이 모드 사라지게 된다.
# f = open("새파일.txt",'w')
# f.close()
# f = open("C:\Users\IT\PycharmProjects\새파일.txt", 'w')
# f.close()
# --------------------------------------------------------------------------------------------------------------------------------------
# File "C:/Users/IT/PycharmProjects/pythonBig/test.py", line 183
#     f = open("C:\Users\IT\PycharmProjects\새파일.txt", 'w')
#             ^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
# 단순히 절대경로를 적어주게 되면 unicode 오류가 뜬다.
# 이것을 해결할려면 open("C:\Users\IT\PycharmProjects\새파일.txt", 'w') 첫번쨰 따운표 앞에 r을 적어 주던가
# 역슬래쉬를 두개를 적어주면 된다.
# --------------------------------------------------------------------------------------------------------------------------------------
# open(r"C:\Users\IT\PycharmProjects\새파일.txt", 'w') or open("C:\\Users\\IT\\PycharmProjects\\새파일.txt", 'w')
# ex 텍스트 파일에 글 쓰기
# f = open("새파일.txt",'w')
# a = int(input("몇번째 줄까지 입력하시겠습니까?"))
# for i in range(1,a+1):
#     data = "%s 줄 입니다 \n" % i
#     f.write(data)
# f.close()
# --------------------------------------------------------------------------------------------------------------------------------------
# 파일을 읽는 방법
# 1. readline() 1줄만 읽는다 : line = f.readline()
# f = open("새파일.txt",'r')
# while 1:
#     line = f.readline()
#     if not line:break
#     print(line)
# f.close()
#
# 2. readlines() 파일의 전체를 읽는다 : line = f.readlines()
# f = open("새파일.txt",'r')
# line = f.readlines()
# print(line)
# f.close()
#
# 3. read() 파일을 전부 읽은 문자열을 돌려준다. : data = f.read()
# f = open("새파일.txt",'r')
# data = f.read()
# print(data)
# f.close

# #클래스란 메소드와 전역변수의 집합
# #클래스 사용 방법 및 예제
# class bank:
#     result = 0
#
#     def deposit(self, a):
#         self.result += a
#         return self.result
#
#     def whithdraw(self,a):
#         self.result -= a
#         return self.result
#
#     def checkbalance(self):
#         return self.result
#
#     def checkbalance1():
#         return print("출력")
#
# asd = bank()
# print(asd.deposit(2))
# print(asd.whithdraw(3))
# print("잔액은 %d입니다" %asd.checkbalance())
# gg = bank
# print(bank.deposit(asd,4))
# print(id(bank))
# print(type(asd))
# print(id(asd))
# class의 self란
# 클래스의 self는 항상 내부클래스의 인자값으로 들어와야 한다.
# self는 메소드를 담은 객체로 접근할수있고 self를 사용하지않으면 클래스명으로 접근해야한다.

# 외부 클래스 호출방법 import 파일이름
import range


class calc:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self,x,y):
        self.result = x + y
        return self.result
    def mul(self,x,y):
        r1 = range.prev
        self.result = r1.mul(self,x,y)
        return self.result


c1 = calc(3, 4)
print(c1.mul(c1.x,c1.y))
