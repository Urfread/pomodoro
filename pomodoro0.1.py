import tkinter as tk

# 倒计时时间（秒），这里测试时用 300 秒，实际可以改成 5 分钟 = 300
TOTAL_SECONDS = 300  

# 创建主窗口
root = tk.Tk()
# 设置窗口全屏
root.attributes("-fullscreen", True)
# 设置窗口始终置顶（避免被其他窗口遮挡）
root.attributes("-topmost", True)   
# 设置窗口背景为黑色
root.configure(bg="black")

# 创建一个大号字体的标签，用来显示倒计时
label = tk.Label(root, text="", font=("Arial", 72), fg="white", bg="black")
label.pack(expand=True)

# 定义倒计时秒数
seconds = TOTAL_SECONDS

# 禁用关闭按钮（防止用户点击右上角 X 关闭窗口）
def disable_event():
    pass
root.protocol("WM_DELETE_WINDOW", disable_event)

# 定义拦截键盘的函数
def block_keys(event):
    # 返回 "break" 表示阻止该事件继续传递，相当于屏蔽这个按键
    return "break"

# 绑定全局快捷键，屏蔽退出相关的组合键
for seq in ("<Escape>", "<Alt-F4>", "<Control-w>", "<Control-q>", "<Control-Alt-period>"):
    root.bind_all(seq, block_keys)

# 倒计时更新函数
def update_timer():
    global seconds
    if seconds > 0:
        # 把秒数转成 分钟:秒 格式
        mins, secs = divmod(seconds, 60)
        label.config(text=f"{mins:02d}:{secs:02d}")
        # 倒计时 -1 秒
        seconds -= 1
        # 1000 毫秒（1 秒）后再次调用 update_timer → 循环更新
        root.after(1000, update_timer)
    else:
        # 倒计时结束，销毁窗口
        root.destroy()

# 启动第一次倒计时更新
update_timer()

# 进入 Tkinter 事件循环（程序不会退出，一直等待事件）
root.mainloop()
