import tkinter as tk
from tkinter import messagebox
import sqlite3
import random


# 连接到数据库
def connect_to_database():
    try:
        conn = sqlite3.connect("rental_data.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS rentals
                          (id INTEGER PRIMARY KEY,
                           property_type TEXT,
                           location TEXT,
                           price INTEGER)''')
        generate_data(cursor)
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("连接成功", "已成功连接到数据库并生成数据")
    except Exception as e:
        messagebox.showerror("连接错误", f"连接数据库时出现错误：\n{str(e)}")


# 生成示例数据
def generate_data(cursor):
    property_types = ["Apartment", "House", "Condo"]
    locations = ["City A", "City B", "City C"]
    prices = [1000, 1500, 2000, 2500, 3000]

    for i in range(10):
        property_type = random.choice(property_types)
        location = random.choice(locations)
        price = random.choice(prices)
        cursor.execute("INSERT INTO rentals (property_type, location, price) VALUES (?, ?, ?)",
                       (property_type, location, price))


# 创建主窗口
window = tk.Tk()
window.title("租房数据分析系统")
window.geometry("300x200")

# 创建连接数据库按钮
connect_button = tk.Button(window, text="连接数据库", command=connect_to_database)
connect_button.pack(pady=20)

# 运行主循环
window.mainloop()
