import json
from tkinter import ttk
from tkinter import*

def get_jp(x):
    Japanese =data["students"][int(x)]["japanese"]
    w_label_sc["text"] = Japanese

f = open("student_score.json")
data = json.load(f)

root=Tk()

w_label=ttk.Label(text="生徒番号")
w_entry=ttk.Entry(width=5)
w_button=ttk.Button(text="テスト結果表示",command = lambda:get_jp(w_entry.get()))
w_label_jp=ttk.Label(text="日本語の得点")
w_label_sc=ttk.Label(text="0")

w_label.grid(row=0,column=0)
w_entry.grid(row=1,column=0)
w_button.grid(row=3,column=0)
w_label_jp.grid(row=2,column=0)
w_label_sc.grid(row=3,column=1)

root.mainloop()

f.close()