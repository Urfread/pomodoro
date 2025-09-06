import tkinter as tk  # 导入 Tkinter 库，用于创建 GUI 窗口
from Marquee import RectMarquee

# 时间参数（单位：秒）
WORK_SECONDS = 1   # 工作时间，实际 30 分钟
REST_SECONDS = 1    # 休息时间，实际 10 分钟


def start_work():
    """进入工作阶段（小窗口倒计时）"""
    work_root = tk.Tk()  # 创建一个工作阶段窗口
    work_root.title("番茄钟")  # 窗口标题
    work_root.geometry("300x150")  # 窗口大小（宽300，高150）
    
    # 创建一个显示倒计时的标签
    label = tk.Label(work_root, text="", font=("Arial", 40))
    label.pack(expand=True)  # 标签居中显示并占满窗口

    seconds = WORK_SECONDS  # 初始化倒计时秒数

    def update_work_timer():
        """每秒更新倒计时"""
        nonlocal seconds
        if seconds > 0:
            # 将秒数转换成分钟和秒
            mins, secs = divmod(seconds, 60)
            # 更新标签文字
            label.config(text=f"{mins:02d}:{secs:02d}")
            seconds -= 1  # 秒数递减
            # 1秒后再次调用自身，实现倒计时循环
            work_root.after(1000, update_work_timer)
        else:
            # 倒计时结束，关闭工作窗口，进入休息阶段
            work_root.destroy()
            start_rest()

    update_work_timer()  # 启动倒计时
    work_root.mainloop()  # 进入事件循环，窗口保持显示并响应事件


def start_rest():
    """进入休息阶段（全屏黑屏倒计时）"""
    rest_root = tk.Tk()  # 创建休息阶段窗口
    rest_root.attributes("-fullscreen", True)  # 全屏显示
    rest_root.attributes("-topmost", True)     # 窗口始终置顶
    rest_root.configure(bg="black")            # 背景设为黑色

    # === 跑马灯挂载 ===
    marquee = RectMarquee(
        rest_root,
        num_blocks=100,   # 总格数
        speed=2,          # 跳动速度
        block_size=40,    # 方块大小
        ratio=0.1,         # 点亮比例
        lines=3           # 来示 4 条灯带
    )
    
    # 创建大字体倒计时标签，白色文字
    label = tk.Label(marquee.canvas, text="", font=("Arial", 72), fg="white", bg="black")
    label.pack(expand=True)

    seconds = REST_SECONDS  # 初始化倒计时秒数

    # 禁用窗口关闭按钮
    def disable_event():
        pass
    rest_root.protocol("WM_DELETE_WINDOW", disable_event)

    # 屏蔽退出相关快捷键
    def block_keys(event):
        return "break"
    # 绑定全局快捷键，防止用户退出窗口
    for seq in ("<Escape>", "<Alt-F4>", "<Control-w>", "<Control-q>", "<Control-Alt-period>"):
        rest_root.bind_all(seq, block_keys)

    def update_rest_timer():
        """每秒更新休息倒计时"""
        nonlocal seconds
        if seconds > 0:
            mins, secs = divmod(seconds, 60)
            label.config(text=f"{mins:02d}:{secs:02d}")  # 更新显示
            seconds -= 1
            rest_root.after(1000, update_rest_timer)    # 1秒后再次调用
        else:
            # 倒计时结束，关闭休息窗口，弹出继续工作提示
            rest_root.destroy()
            show_continue_window()

    update_rest_timer()  # 启动倒计时
    rest_root.mainloop()  # 进入事件循环


def show_continue_window():
    """休息结束 → 弹出一个小窗口，点击按钮才能继续下一轮"""
    win = tk.Tk()
    win.title("休息结束")
    win.geometry("300x150")

    # 提示文字
    label = tk.Label(win, text="休息结束，点击继续工作", font=("Arial", 14))
    label.pack(pady=20)

    # 点击按钮 → 关闭提示窗口，重新进入工作阶段
    btn = tk.Button(win, text="继续工作", font=("Arial", 14),
                    command=lambda: (win.destroy(), start_work()))
    btn.pack(pady=20)

    win.mainloop()


if __name__ == "__main__":
    # 程序入口：先进入工作阶段
    start_work()
