import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib
import random

class Teammate:
  """팀 인연 맺기 프로젝트 ><"""
  def __init__(self):
    """기본값 설정(모델, 데이터에 포함된 이름)"""
    self.knn = joblib.load('sknn_model.pkl')
    self.data = pd.read_csv(r'ssdata.csv').iloc[:, -1]
    self.role = ["팀장", "ppt", "코딩총괄", "발표", "자료조사", "응원단장"]
    self.place = {"스페이스코웍": [6,8,10,25], "테이블웍스": [3,6,25], "스타온 비즈센터": [4,6],
                  "크럼(카페)":[2,3,4], "전주대 도서관 스터디룸":[3,4,5,6,7,8,9,10], 
                  "전주대 공학1관 423": [1,2,3,4,5,6,7,8]}
    self.profile = None
    self.name = None
    self.my_team = None


  def my_profile(self):
    """팀원 추천을 위한 개인 정보수집"""
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

    scores = {"성격": 0, "통찰력": 0, "팀 내 역할 담당": 0, "소통": 0, "팀 프로젝트 결과": 0, "능력": 0}
    
    print("프로필 생성입니다.")
    user_name = input("이름입력 : ")
    print("각 문항에 대해 다음과 같이 제대로 응답해주세요:")
    print("1: 매우 그렇지 않다, 2: 그렇지 않다, 3: 보통이다, 4: 그렇다, 5: 매우 그렇다\n")

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

    profile = list([0] + list(scores.values())) # csv에 행번호문제로 0추가해야함
    self.name = user_name
    self.profile = profile


  def random_team(self):
    """이름중 random으로 팀 만들기"""
    label = self.data.tolist()
    random.shuffle(label)

    print("랜덤 팀원 뽑기 입니다.")
    n = int(input('원하는 팀원의 수 입력 : '))

    # 팀 나누기
    team = [] 
    for i in range(0, len(label), n):
      try:
        team.append((label[i:i+n]))
      except:
        team.append((label[i:])) # 오류 일어나면 남은것 떄문임 그래서 이와 같이 설정
        break

    #남은 인원 분배
    h = len(team[-1])  
    if h != n:
        seq = list(random.sample(range(len(team[:-2])), h))
        for s, name in zip(seq, team[-1]):
          team[s].append(name)

        del team[-1]

    for num, name in enumerate(team):
       print(f"{num+1}번째팀 : {' '.join(name)}")
       

  def model(self):
    """팀원 추천하는 모델"""
    try:
      n = int(input('원하는 팀원의 수 입력 : '))+1

      # 인덱스 추출
      _, peoples = self.knn.kneighbors([self.profile], n_neighbors=n, return_distance=True)
      peoples = peoples[0].tolist() # 가까운순으로 되어 있음
      data_y = self.data

      # 본인 제거
      for i in peoples:
        if self.name == data_y.iloc[i]:
            del peoples[peoples.index(i)]
            break
      else:
          peoples = peoples[:(n-1)]
      print(f"추천된 팀원")
    
      myt = [self.name]
      for most, label in enumerate(peoples):
        print(f"{most+1}번째로 가까운 사람 : {data_y.iloc[label]}") 
        myt.append(data_y.iloc[label])
      print()
      
      self.my_team = myt
    
    except NameError:
      print("profile 설정X")
    except ValueError:
      print("제대로된 값 입력")
  
  def role_assign(self):
    role = self.role
    sublist = role[1:]
    random.shuffle(sublist)
    role[1:] = sublist

    t = self.my_team
    random.shuffle(t)

    for r, name in zip(role ,t):
      print(f'"{name}" 에게 주어진 역할 : {r}')

    if len(role) < len(self.my_team):
       print("남으신 분들은 자율적으로 정해주세요.")

  def recommend(self):
      team_size = len(self.my_team)
      low = team_size - 1
      high = team_size + 1
      v = {
          name: capacities
          for name, capacities in self.place.items()
          if any(low <= size <= high for size in capacities)
      }

      print("추천하는 장소")
      for p, n in v.items():
         print(f"장소 : {p}\n수용가능인원 : {', '.join(map(str, n))}")

def main():
  """GUI"""

if __name__ == '__main__':
  s1 = Teammate()
  #s1.random_team()
  s1.my_profile()
  s1.model()
  #s1.recommend()
  #s1.role_assign()
