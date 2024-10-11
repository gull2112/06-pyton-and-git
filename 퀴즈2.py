def check_length_of_message(message):
    length = len(message)
    if length <= 20:
        return 50  # 요금 50원
    else:
        return 100  # 요금 100원

# 사용자로부터 문자 메시지 입력받기
message = input("문자 메시지를 입력하세요: ")

# 문자 요금 산출
fee = check_length_of_message(message)

# 결과 출력
print(f'문자 요금은 {fee}원입니다.')