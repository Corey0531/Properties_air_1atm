import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        Re = float(entry_Re.get())
        Pr = float(entry_Pr.get())
    except ValueError:
        messagebox.showerror("錯誤", "請輸入有效的數字")
        return

    Nu_in =  (0.62 * (Re ** 0.5) * (Pr ** (1/3)) / (1 + (0.4 / Pr) ** (2/3)) ** (1/4))
    Nu = 0.3 + Nu_in*(1+ (Re / 282000) ** (5/8))**(4/5)

    output_var.set(f"計算結果 Nu = {Nu:.4g}")

root = tk.Tk()
root.geometry("400x150")
root.title("Nu 計算器")

tk.Label(root, text="請輸入 Re：").pack()
entry_Re = tk.Entry(root)
entry_Re.pack()

tk.Label(root, text="請輸入 Pr：").pack()
entry_Pr = tk.Entry(root)
entry_Pr.pack()

tk.Button(root, text="計算", command=calculate).pack()

output_var = tk.StringVar()
tk.Label(root, textvariable=output_var, height=2).pack()

root.mainloop()

