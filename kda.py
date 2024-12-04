import pandas as pd
import os

def get_score(question):
    while True:
        try:
            score = int(input(question))  
            if 1 <= score <= 7:
                return score
            else:
                print("1부터 7까지의 값만 입력해주세요.")
        except ValueError:
            print('유효한 숫자를 입력해주세요.')

def conduct_survey():
    scores = {"성격": 0, "통찰력": 0, "팀 내 역할 담당": 0, "소통": 0, "팀 프로젝트 결과": 0, "능력": 0}
 
    print("설문조사에 오신 것을 환영합니다!")
    user_name = input("이름을 입력해주세요: ")
    print("각 문항에 대해 다음과 같이 응답해주세요:")
    print("1: 매우 그렇지 않다, 2: 그렇지 않다, 3: 조금 그렇지 않다, 4: 보통이다, 5: 조금 그렇다, 6: 그렇다, 7: 매우 그렇다\n")

    questions = {
        "성격": [
            "외향성 (1~7): ",
            "친화성 (1~7): ",
            "수용성 (1~7): ",
            "독립성 (1~7): ",
            "이성적 (1~7): ",
            "도전적 (1~7): ",
            "강한 멘탈 (1~7): ",
            "성실성 (1~7): ",
            "책임감 (1~7): " ,
            "성격이 빠름 (1~7): ",
            "유연성 (1~7): ",
            "계획성 (1~7): "
        ],
        "통찰력": [
            "문제 해결 능력 (1~7): ",
            "창의적 사고 (1~7): ",
            "전략적 사고 (1~7): ",
            "분석적 사고 수준 (1~7): ",
            "경험적 사고 (1~7): ",
            "직관적 사고 수준 (1~7): "
        ],
        "팀 내 역할 담당": [
            "리더 (1~7): ",
            "자료 수집 (1~7): ",
            "프로젝트 정리 및 시각적 자료 제작 (1~7): ",
            "발표 (1~7): "
        ],
        "소통": [
            "적극적으로 의견 교환 (1~7): ",
            "대화 흐름 주도 (1~7): ",
            "갈등 상황시 문제 해결 능력이 뛰어남 (1~7): ",
            "피드백 교환 능력 (1~7): ",
            "정보 공유 능력 (1~7): ",
        ],
        "팀 프로젝트 결과": [
            "1: 매우 실패함, 2: 대체로 실패함, 3: 어려움이 많음, 4: 보통, 5: 다소 성공적, 6: 대체로 성공적, 7: 매우 성공적\n평가 (1~7): "
        ],
        "능력": [
            "1: 경험없음, 2: 이론만 배운 적 있음, 3: 기초적 작업과 개념 이해, 4: 기초적 작업 가능, 5: 중급 수준, 6: 능숙함, 7: 매우 능숙함\n코딩 실력 (1~7): ",
            "수학 실력 (1~7): ",
            "이론 실력 (1~7): ",
            "실무 능력 (1~7): "
        ]
    }

    # 설문 진행 및 점수 계산
    for category, question_list in questions.items():
        print(f"{category}")
        for question in question_list:
            score = get_score(question)
            scores[category] += score

    print("설문조사 결과:")
    print(scores)
    return user_name, scores

name, score = conduct_survey()

# 벡터 생성후 행 벡터로 변경
df = pd.DataFrame([list(score.values())+[name]])

file_name = "score_list.csv"
if os.path.exists(file_name):
    df.to_csv(file_name, mode='a',header=False)
else:
    df.to_csv(file_name, mode='w',header=False)