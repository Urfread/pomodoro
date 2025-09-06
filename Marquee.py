import tkinter as tk
import colorsys

class RectMarquee:
    def __init__(self, root, num_blocks=40, speed=2, block_size=20, ratio=0.4, lines=4):
        """
        speed: 每次跳动的格数
        block_size: 方块的固定大小
        ratio: 点亮比例
        lines: 跑马灯条数（默认 4）
        """
        self.root = root
        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.num_blocks = num_blocks
        self.speed = max(1, int(speed))
        self.block_size = block_size
        self.step_offset = 0
        self.ratio = ratio
        self.lines = lines

        self.animate()

    def animate(self):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        perimeter = 2.0 * (w + h)
        step_size = perimeter / self.num_blocks
        lit_blocks = max(1, int(self.num_blocks * self.ratio))

        # 计算每条灯带之间的间隔
        line_gap = perimeter / self.lines

        for i in range(lit_blocks):
            for line in range(self.lines):
                delta = line * line_gap
                pos = ((i + self.step_offset) * step_size + delta) % perimeter
                x, y = self.get_xy(pos, w, h)

                # 彩色渐变
                hue = ((i + self.step_offset) / float(lit_blocks)) % 1.0
                r, g, b = [int(v * 255) for v in colorsys.hsv_to_rgb(hue, 1, 1)]

                # 亮度：头暗尾亮
                progress = i / float(max(1, lit_blocks - 1))
                brightness = 0.3 + 0.7 * progress
                r = int(r * brightness)
                g = int(g * brightness)
                b = int(b * brightness)
                color = f"#{r:02x}{g:02x}{b:02x}"

                # 固定大小方块
                size = self.block_size
                self.canvas.create_rectangle(
                    x - size // 2, y - size // 2,
                    x + size // 2, y + size // 2,
                    fill=color, outline=""
                )

        # 每次跳几个格
        self.step_offset = (self.step_offset + self.speed) % self.num_blocks
        self.root.after(60, self.animate)

    def get_xy(self, pos, w, h):
        """路径位置 → 坐标"""
        if pos < w:  # 上边
            return pos, 0
        elif pos < w + h:  # 右边
            return w, pos - w
        elif pos < 2 * w + h:  # 下边
            return 2 * w + h - pos, h
        else:  # 左边
            return 0, 2 * (w + h) - pos


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="black")
    root.attributes("-fullscreen", True)

    RectMarquee(root,
                num_blocks=100,
                speed=2,
                block_size=40,
                ratio=0.1,
                lines=4)   # 设置 3 条跑马灯
    root.mainloop()