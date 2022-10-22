from tkinter import *
from tkinter import ttk as tk
import json
# import tkinter as tk
def get_Jp(x):
    Japanese=data["students"][int(x)]['japanese']
    label3['text']=Japanese
f= open("student_score.json")
data = json.load(f)

root=Tk()
label1=tk.Label(text="生徒番号")
label1.grid(row=0,column=0)
entry=tk.Entry(width=5)
entry.grid(row=1,column=0)
button=tk.Button(text="テスト結果の表示",command=lambda:get_Jp(entry.get()))
button.grid(row=2,column=0)
label2=tk.Label(text="日本語の得点：")
label2.grid(row=3,column=0)
label3=tk.Label(text="0")
label3.grid(row=3,column=1)
root.mainloop()

f.close()
