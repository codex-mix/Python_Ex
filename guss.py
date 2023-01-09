from random import *  # 랜덤 함수 라이브 불러옴

com = randint(1, 100)  # 랜덤으로 숫자1~100 사이 난수 발생
con = 1     # 카운트 1부터


while True:
    # 메시지 출력
    print("#########################숫자 맞추기 게임################################")
    print("["+str(con)+"]"+"째 도전")        # 도전카운트 출력
    num = input("숫자를 입력하세요?")        # 숫자 입력 받음
    if not num.isdigit():                    # 숫자가 아니면 강제로 True
        print(">>>>>>문자는 안돼요<<<<<<<")
        continue                             # 다시 루프처음으로
    num = int(num)                          # 입력받은 문자를 숫자로 변환
    con += 1                                # 카운트 증가
    if con == 10:                           # 10회동안 정답을 맞추지 못하면 클리어 실패 종료
        print("클리어 실패 !!!")
        break
        # 받은 숫자와 컴퓨터가 생각한 숫자와 비교
    if num == com:                              # 이력숫자가 와 랜덤숫자 같을때
        print("정답입니다.!!", com, "입니다.")
        break
    elif num < com:                             # 입력숫자가 클때
        print(">>>더 큰 수를 입력하세요!")
    elif num > com:
        print(">>>작은 수를 입력하세요!", con)   # 압력숫자가 작을때
