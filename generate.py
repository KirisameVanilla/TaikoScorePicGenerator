from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import filedialog, messagebox

def draw_small_pic(small_img_path, pic, position, scale = 1):
    img = Image.open(small_img_path)
    new_size = (int(img.width * scale), int(img.height * scale))
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    pic.paste(img, position, img)  # 小图需要带透明度通道（RGBA）


def draw_text(text, pic, size, position, font_type):
    draw = ImageDraw.Draw(pic)
    if (font_type == "日文字库"):
        font = ImageFont.truetype('res/J002-A-OTF-KanteiryuStd-Ultra.otf', size)
    else:
        font = ImageFont.truetype('res/AaKanTingLiu-2.ttf', size)

    outline_width = 3
    x, y = position
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:  # 避免中心重复绘制
                draw.text((x + dx, y + dy), text, font=font, fill="orange")

    draw.text(position, text, font=font, fill="black")
    return pic

def draw_score_rank(pic, type=95, scale = 1):
    if (type == "粉雅"):
        img_path = "res/90.png"
    if (type == "彩雅"):
        img_path = "res/95.png"
    if (type == "极"):
        img_path = "res/100.png"
    draw_small_pic(img_path, pic, (1000, 100), scale)

def draw_difficulty(pic, difficulty = 0, scale = 1):
    if (difficulty == "鬼"):
        img_path = "res/difficulty_Oni.png"
    if (difficulty == "里鬼"):
        img_path = "res/difficulty_UraOni.png"
    draw_small_pic(img_path, pic, (1050, 400), scale)

def draw_small_taiko(pic, scale):
    draw_small_pic("res/my_taiko.png", pic, (150,350), scale)

def draw_crown(pic, type=0, scale = 1):
    if (type == "通关"):
        img_path = "res/crown_Clear.png"
    if (type == "全连"):
        img_path = "res/crown_gold.png"
    draw_small_pic(img_path, pic, (1050, 600), scale)

def generate_image():
    try:
        text1 = entry_text1.get()
        text2 = entry_text2.get()
        score_type = combo_score_type.get()
        difficulty = combo_difficulty.get()
        crown = combo_crown.get()
        font_type = combo_font.get()

        background = Image.open('res/background.png')
        background = draw_text(text1, background, 120, (250, 150), font_type)
        background = draw_text(text2, background, 120, (250, 300), font_type)
        draw_score_rank(background, score_type, scale=2)
        draw_small_taiko(background, scale=2)
        draw_difficulty(background, difficulty, scale=2)
        draw_crown(background, crown, scale=2)

        output_path = 'result.png'
        background.save(output_path)
        background.show()
        messagebox.showinfo("成功", f"图片已保存为 {output_path}")
    except Exception as e:
        messagebox.showerror("错误", f"生成图片时出错：{e}")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("太鼓成绩图生成器")

    # 输入文本1
    tk.Label(root, text="曲名").grid(row=0, column=0, padx=10, pady=5)
    entry_text1 = tk.Entry(root, width=30)
    entry_text1.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="字库").grid(row=1, column=0, padx=10, pady=5)
    combo_font = Combobox(root, values=["日文字库", "中文字库"], state="readonly", width=28)
    combo_font.set("日文字库")  # 默认值
    combo_font.grid(row=1, column=1, padx=10, pady=5)

    # 输入文本2
    tk.Label(root, text="分数").grid(row=2, column=0, padx=10, pady=5)
    entry_text2 = tk.Entry(root, width=30)
    entry_text2.grid(row=2, column=1, padx=10, pady=5)

    # 输入分数类型
    tk.Label(root, text="分数类型").grid(row=3, column=0, padx=10, pady=5)
    combo_score_type = Combobox(root, values=["粉雅", "紫雅", "极"], state="readonly", width=28)
    combo_score_type.set("粉雅")  # 默认值
    combo_score_type.grid(row=3, column=1, padx=10, pady=5)

    # 难度
    tk.Label(root, text="难度").grid(row=4, column=0, padx=10, pady=5)
    combo_difficulty = Combobox(root, values=["鬼", "里鬼"], state="readonly", width=28)
    combo_difficulty.set("鬼")  # 默认值
    combo_difficulty.grid(row=4, column=1, padx=10, pady=5)

    # 皇冠
    tk.Label(root, text="皇冠").grid(row=5, column=0, padx=10, pady=5)
    combo_crown = Combobox(root, values=["通关", "全连"], state="readonly", width=28)
    combo_crown.set("通关")  # 默认值
    combo_crown.grid(row=5, column=1, padx=10, pady=5)

    # 生成图片按钮
    btn_generate = tk.Button(root, text="生成图片", command=generate_image)
    btn_generate.grid(row=6, column=0, columnspan=2, pady=20)

    # 运行主循环
    root.mainloop()
    # background = Image.open('res/background.png')
    # background = draw_text("旋風ノ舞【地】", background, 120, (250, 150))
    # background = draw_text("980930", background, 120, (250, 300))
    # draw_score_rank(background, 95, scale = 2)
    # draw_small_taiko(background, scale = 2)
    # draw_difficulty(background, difficulty = 0, scale = 2)
    # draw_crown(background, type = 1, scale = 2)
    # background.save('result.png')
    # background.show()