def get_valid_input(prompt):
    while True:
        value = input(prompt)  
        if value in ['1', '2', '3', '4', '5']:  # '1'~'5' 문자만 허용
            return int(value)  # 유효한 값이면 숫자로 변환하여 반환
        else:
            print("1부터 5까지의 값만 입력하세요.")

# 설문조사 시작
survey_results = {}

print("설문조사에 오신 것을 환영합니다!")
print("각 문항에 대해 다음과 같이 응답해주세요:")
print("1: 매우 그렇지 않다, 2: 그렇지 않다, 3: 보통이다, 4: 그렇다, 5: 매우 그렇다")

# 참가자 이름 입력 받기
name = input("이름을 입력해주세요: ")

# 성격 유형
print("1. 성격 유형")
survey_results["성격"] = {
    "외향성": get_valid_input("외향성 (1~5): "),
    "적극성": get_valid_input("적극성 (1~5): "),
    "친화성": get_valid_input("친화성 (1~5): "),
    "성실성": get_valid_input("성실성 (1~5): "),
    "책임감": get_valid_input("책임감 (1~5): "),
    "수용성": get_valid_input("수용성 (1~5): "),
    "성격이 빠름": get_valid_input("성격이 빠름 (1~5): ")
}

# 통찰력
print("\n2. 통찰력")
survey_results["통찰력"] = {
    "창의적 문제 해결 능력": get_valid_input("창의적 문제 해결 능력 (1~5): "),
    "분석적 사고 수준": get_valid_input("분석적 사고 수준 (1~5): "),
    "직관적 사고 수준": get_valid_input("직관적 사고 수준 (1~5): ")
}

# 팀 내 역할 담당
print("\n3. 팀 내 역할 담당")
survey_results["팀 내 역할 담당"] = {
    "리더십": get_valid_input("리더십 (1~5): "),
    "자료 수집": get_valid_input("자료 수집 (1~5): "),
    "프로젝트 정리 및 시각적 자료 제작": get_valid_input("프로젝트 정리 및 시각적 자료 제작 (1~5): "),
    "발표": get_valid_input("발표 (1~5): ")
}

# 소통
print("\n4. 소통")
survey_results["소통"] = {
    "적극적으로 의견 교환": get_valid_input("적극적 의견 교환 (1~5): "),
    "대화 흐름 주도": get_valid_input("대화 흐름 주도(1~5): "),
    "갈등 상황시 문제 해결 방식": input("갈등 상황시 문제 해결 방식(1: 타협, 2: 혼자): ")
}

# 평소 팀 프로젝트의 결과
print("\n5. 평소 팀 프로젝트의 결과")
survey_results["팀 프로젝트 결과"] = get_valid_input("평가 (1~5): ")

# 능력
print("\n6. 능력")
print("1: 경험없음, 2: 배운 적만 있음, 3: 기초적 작업 가능, 4: 능숙함 , 5: 매우 능숙함")
survey_results["능력"] = {
    "코딩 실력": get_valid_input("코딩 실력 (1~5): "),
    "수학 실력": get_valid_input("수학 실력 (1~5): "),
    "이론 실력": get_valid_input("이론 실력 (1~5): "),
    "실무 능력": get_valid_input("실무 능력 (1~5): ")
}

# 출력된 설문조사 결과
print("\n설문조사 결과:")
for category, responses in survey_results.items():
    print(f"{category}: {responses}")
