from tkinter import*
from tkinter import ttk

root=Tk()

w_label=ttk.Label(text="生徒番号")
w_entry=ttk.Entry(width=5)
w_button=ttk.Button(text="テスト結果表示")
w_label_jp=ttk.Label(text="日本語の得点")
w_label_sc=ttk.Label(text="0")

w_label.grid(row=0,column=0)
w_entry.grid(row=1,column=0)
w_button.grid(row=3,column=0)
w_label_jp.grid(row=2,column=0)
w_label_sc.grid(row=3,column=1)

root.mainloop()