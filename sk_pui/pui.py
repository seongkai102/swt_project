# swtbase.py, ssdata.csv, sknn_model.pkl 필요 (같은 디렉토리)
from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog
from swtbase import Teammate


def main_cover():

    mx, my = Teammate.win()

    cover = tk.Tk()
    cover.title("한/영키 팀 추천 프로그램")
    cover.geometry(f"500x600+{mx}+{my}")
    try:
        img = PhotoImage(file=r"이미지 경로", master=cover)
        img_lab = tk.Label(cover, image=img)
        img_lab.image=img
        img_lab.pack()
    except Exception:
        tk.Label(cover, text="이미지를 불러올 수 없습니다.").pack()
    
    tit_lab = tk.Label(cover, text="한/영키 팀 추천 프로그램")
    tit_lab.pack()

    def start_app():
        cover.destroy()
        main()
    start_button = tk.Button(cover, text="다음", command=start_app)
    start_button.pack()
    cover.mainloop()


def main():

    mx, my = Teammate.win()

    teammate = Teammate()
    root = tk.Tk()
    root.title("한/영키 팀 추천 프로그램")
    root.geometry(f"500x600+{mx}+{my}")

    output_area = tk.Text(root, height=20, width=60, wrap="word")
    output_area.pack(pady=10)

    # 프로필 생성
    def create_profile():
        try:
            teammate.my_profile()
            messagebox.showinfo("완료", f"{teammate.name}님의 프로필이 생성되었습니다!")
        except Exception as e:
            messagebox.showerror("오류", f"프로필 생성 중 오류 발생: {e}")

    # 랜덤 팀 생성
    def random_team():
        try:
            output_area.delete(1.0, tk.END) # 초기화
            n = simpledialog.askinteger("랜덤 팀 생성", "팀당 인원 수를 입력하세요:")
            if not n or n <= 0:
                messagebox.showerror("오류", "올바른 숫자를 입력해주세요.")
                return

            team = teammate.random_team(n)

            output_area.insert(tk.END, "랜덤 팀 생성 결과:\n")
            for idx, team in enumerate(team):
                output_area.insert(tk.END, f"{idx+1}팀: {', '.join(team)}\n")
        except Exception as e:
            messagebox.showerror("오류", f"랜덤 팀 생성 중 오류 발생: {e}")

    # 모델 기반 팀 생성
    def model_team():
        try:
            if not teammate.profile:
                messagebox.showerror("오류", "먼저 프로필을 생성하세요.")
                return

            output_area.delete(1.0, tk.END)
            n = simpledialog.askinteger("모델 기반 팀 생성", "팀당 추천 인원 수를 입력하세요:")
            if not n or n <= 0:
                messagebox.showerror("오류", "올바른 숫자를 입력해주세요.")
                return

            teammate.model(n)
            if not teammate.my_team:
                messagebox.showerror("오류", "추천된 팀원이 없습니다.")
                return

            output_area.insert(tk.END, "모델 기반 팀 추천 결과\n")
            for idx, member in enumerate(teammate.my_team[:n+1], 1):
                output_area.insert(tk.END, f"{idx}: {member}\n")
        except Exception as e:
            messagebox.showerror("오류", f"모델 기반 팀 생성 중 오류 발생: {e}")


    # 역할 배정
    def assign_roles():
        try:
            output_area.delete(1.0, tk.END)
            teammate.role_assign()
            output_area.insert(tk.END, "역할 배정 결과:\n")
            for name, role in zip(teammate.my_team, teammate.role):
                output_area.insert(tk.END, f"{name}: {role}\n")
            if len(teammate.my_team) > len(teammate.role):
                output_area.insert(tk.END, "역할이 남는 사람은 자율적으로 결정해주세요.\n")
        except Exception as e:
            messagebox.showerror("오류", f"역할 배정 중 오류 발생: {e}")


    # 추천 장소
    def recommend_places():
        try:
            output_area.delete(1.0, tk.END)
            if not teammate.my_team:
                messagebox.showerror("오류", "먼저 팀을 생성하세요.")
                return

            output_area.insert(tk.END, "추천 장소:\n")
            for place, capacities in teammate.place.items():
                output_area.insert(
                    tk.END, f"장소: {place}, 수용 가능 인원: {', '.join(map(str, capacities))}\n"
                )
        except Exception as e:
            messagebox.showerror("오류", f"추천 장소 중 오류 발생: {e}")


    # 버튼 추가
    buttons = [
        ("프로필 생성", create_profile),
        ("랜덤 팀 생성", random_team),
        ("모델 기반 팀 생성", model_team),
        ("역할 배정", assign_roles),
        ("추천 장소", recommend_places),
    ]
    for text, command in buttons:
        tk.Button(root, text=text, command=command, width=30).pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main_cover()