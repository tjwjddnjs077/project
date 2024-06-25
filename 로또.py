import tkinter as tk
import random

def 추첨():
    번호들 = random.sample(range(1, 100), 6)
    번호들.sort()
    
    홀수 = [num for num in 번호들 if num % 2 != 0]
    짝수 = [num for num in 번호들 if num % 2 == 0]
    
    if len(홀수) == 2 and len(짝수) == 4:
        결과 = "당첨!"
    else:
        결과 = "다음 기회에..."

    번호_label.config(text="로또 번호: " + ", ".join(map(str, 번호들)))
    결과_label.config(text=결과)

# GUI 설정
root = tk.Tk()
root.title("로또 번호 추첨기")

프레임 = tk.Frame(root)
프레임.pack(pady=20)

추첨_버튼 = tk.Button(프레임, text="번호 추첨", command=추첨)
추첨_버튼.pack(pady=10)

번호_label = tk.Label(프레임, text="로또 번호: ", font=("Helvetica", 16))
번호_label.pack(pady=10)

결과_label = tk.Label(프레임, text="", font=("Helvetica", 16))
결과_label.pack(pady=10)

root.mainloop()

