import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox

# 讀取 CSV（UTF-8 編碼）
df = pd.read_csv(r'd:\Python\題目\大數據\air_1atm.csv', encoding='utf-8')

# 將所有欄位轉為數值型別
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

def query():
    try:
        query_temp = float(entry.get())
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
    output.delete('1.0', tk.END)
    output.insert(tk.END, "查詢結果：\n")
    for k, v in result.items():
        if isinstance(v, float):
            output.insert(tk.END, f"{k}: {v:.4g}\n")
        else:
            output.insert(tk.END, f"{k}: {v}\n")

# 建立 GUI
root = tk.Tk()
root.title("Properties of air at 1 atm")

tk.Label(root, text="請輸入溫度（Temp）：").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="查詢", command=query).pack()

output = tk.Text(root, height=15, width=40)
output.pack()

root.mainloop()