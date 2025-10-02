import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox

# 讀取 CSV（UTF-8 編碼）
df = pd.read_csv(r'd:\Python\題目\大數據\air_1atm.csv', encoding='utf-8')

# 將所有欄位轉為數值型別
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

def query_air_properties():
    try:
        query_temp = float(entry_temp.get())
    except ValueError:
        messagebox.showerror("錯誤", "請輸入有效的數字")
        return

    if query_temp < df['Temp'].min() or query_temp > df['Temp'].max():
        messagebox.showwarning("警告", "超出資料範圍")
        return

    result = {}
    for col in df.columns:
        if col == 'Temp':
            result[col] = query_temp
        else:
            result[col] = np.interp(query_temp, df['Temp'], df[col])
    output_air.delete('1.0', tk.END)
    output_air.insert(tk.END, "查詢結果：\n")
    for k, v in result.items():
        if isinstance(v, float):
            output_air.insert(tk.END, f"{k}: {v:.4g}\n")
        else:
            output_air.insert(tk.END, f"{k}: {v}\n")

def calculate_Nu():
    try:
        Re = float(entry_Re.get())
        Pr = float(entry_Pr.get())
    except ValueError:
        messagebox.showerror("錯誤", "請輸入有效的數字")
        return

    # 這裡寫你的計算公式
    Nu_in = (0.62 * (Re ** 0.5) * (Pr ** (1/3)) / (1 + (0.4 / Pr) ** (2/3)) ** (1/4))
    Nu = 0.3 + Nu_in * (1 + (Re / 282000) ** (5/8)) ** (4/5)

    output_Nu_var.set(f"計算結果 Nu_cyl = {Nu:.4g}")

root = tk.Tk()
root.title("1 atm 空氣數據 & Nu 計算器")
root.geometry("500x450")

# --- 空氣性質查表區塊 ---
frame_air = tk.LabelFrame(root, text="空氣性質查表 (1 atm)", padx=10, pady=10)
frame_air.pack(fill="both", expand=True, padx=10, pady=5)

tk.Label(frame_air, text="請輸入溫度（Temp，°C）：").pack()
entry_temp = tk.Entry(frame_air)
entry_temp.pack()

tk.Button(frame_air, text="查詢", command=query_air_properties).pack(pady=2)

output_air = tk.Text(frame_air, height=10, width=50)
output_air.pack()

# --- Nu 計算區塊 ---
frame_nu = tk.LabelFrame(root, text="Nu 計算(cylinders)", padx=10, pady=10)
frame_nu.pack(fill="both", expand=True, padx=10, pady=5)

tk.Label(frame_nu, text="請輸入 Re：").pack()
entry_Re = tk.Entry(frame_nu)
entry_Re.pack()

tk.Label(frame_nu, text="請輸入 Pr：").pack()
entry_Pr = tk.Entry(frame_nu)
entry_Pr.pack()

tk.Button(frame_nu, text="計算", command=calculate_Nu).pack(pady=2)

output_Nu_var = tk.StringVar()
tk.Label(frame_nu, textvariable=output_Nu_var, height=2).pack()

root.mainloop()

