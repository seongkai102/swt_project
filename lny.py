import pandas as pd
import os

def get_score(question):
    while True:
        try:
            score = int(input(question))
            if 1 <= score <= 5:
                return score
            else:
                print("1부터 5까지의 값만 입력해주세요.")
        except ValueError:
            print('유효한 숫자를 입력해주세요.')

def conduct_survey():
    scores = {"성격": 0, "통찰력": 0, "팀 내 역할 담당": 0, "소통": 0, "팀 프로젝트 결과": 0, "능력": 0}

    print("설문조사에 오신 것을 환영합니다!")
    user_name = input("이름을 입력해주세요: ")
    print("각 문항에 대해 다음과 같이 제대로 응답해주세요:")
    print("1: 매우 그렇지 않다, 2: 그렇지 않다, 3: 보통이다, 4: 그렇다, 5: 매우 그렇다\n")

    questions = {
        "성격": [
            "외향성 (1~5): ",
            "친화성 (1~5): ",
            "성실성 (1~5): ",
            "책임감 (1~5): ",
            "수용성 (1~5): ",
            "성격이 빠름 (1~5): "
        ],
        "통찰력": [
            "창의적 문제 해결 능력 (1~5): ",
            "분석적 사고 수준 (1~5): ",
            "직관적 사고 수준 (1~5): "
        ],
        "팀 내 역할 담당": [
            "리더 (1~5): ",
            "자료 수집 (1~5): ",
            "프로젝트 정리 및 시각적 자료 제작 (1~5): ",
            "발표 (1~5): "
        ],
        "소통": [
            "적극적으로 의견 교환 (1~5): ",
            "대화 흐름 주도 (1~5): ",
            "갈등 상황시 문제 해결 (1~5): "
        ],
        "팀 프로젝트 결과": [
            "1: 실패한 경우가 많음, 2: 어려움이 많음, 3: 보통, 4: 대체로 성공적, 5: 항상 성공적\n평가 (1~5): "
        ],
        "능력": [
            "1: 경험없음, 2: 배운 적만 있음, 3: 기초적 작업 가능, 4: 능숙함, 5: 매우 능숙함\n코딩 실력 (1~5): ",
            "수학 실력 (1~5): ",
            "이론 (1~5): ",
            "실무 능력 (1~5): "
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