# 番茄钟 (Pomodoro Timer)

一个基于 Python 和 Tkinter 的简易番茄钟程序，帮助用户**强制黑屏**，多多休息。

---

## 作业流程

1. **工作阶段**
   - 弹出小窗口倒计时（默认 25 分钟）
   - 每秒更新显示
   - 倒计时结束自动切换到休息阶段

2. **休息阶段**
   - 全屏黑色窗口倒计时（默认 5 分钟）
   - 屏蔽关闭按钮和常用退出快捷键（如 `Esc`、`Alt+F4`、`Ctrl+W`、`Ctrl+Q`、`Ctrl+Alt+.`）
   - 倒计时结束自动弹出提示窗口

3. **休息结束提示**
   - 弹出小窗口提示休息结束
   - 点击按钮后重新进入下一轮工作阶段
   - 循环进行工作/休息周期

---

## 使用方法

两种，一种是把`pomodoro.py`拷贝下来，然后执行`pyinstaller --onefile pomodoro.py`进行编译，再点构建出来的.exe就能用了。

另一种是直接下载.exe，[下载地址](https://github.com/Urfread/pomodoro/releases/tag/v0.1.0)。只下载这个`pomodoro.exe`就行，我做成单文件的了。

