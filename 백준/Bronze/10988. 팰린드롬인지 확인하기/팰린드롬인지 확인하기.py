string = input().replace(" ", "").lower()  # 공백 제거 및 소문자로 변환
if string == string[::-1]:  # 문자열을 뒤집어서 원래 문자열과 같은지 비교
    print(1)  # 펠린드롬이면 1 출력
else:
    print(0)  # 펠린드롬이 아니면 0 출력
