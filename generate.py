from PIL import Image, ImageDraw, ImageFont

def draw_small_pic(small_img_path, pic, position, scale = 1):
    img = Image.open(small_img_path)
    new_size = (int(img.width * scale), int(img.height * scale))
    img = img.resize(new_size, Image.Resampling.LANCZOS)
    pic.paste(img, position, img)  # 小图需要带透明度通道（RGBA）


def draw_text(text, pic, size, position):
    draw = ImageDraw.Draw(pic)
    font = ImageFont.truetype('J002-A-OTF-KanteiryuStd-Ultra.otf', size)

    outline_width = 3
    x, y = position
    for dx in range(-outline_width, outline_width + 1):
        for dy in range(-outline_width, outline_width + 1):
            if dx != 0 or dy != 0:  # 避免中心重复绘制
                draw.text((x + dx, y + dy), text, font=font, fill="orange")

    draw.text(position, text, font=font, fill="black")
    return pic

def draw_score_rank(pic, type=95, scale = 1):
    if (type == 90):
        img_path = "90.png"
    if (type == 95):
        img_path = "95.png"
    if (type == 100):
        img_path = "100.png"
    draw_small_pic(img_path, pic, (1000, 100), scale)

def draw_difficulty(pic, difficulty = 0, scale = 1):
    if (difficulty == 0):
        img_path = "difficulty_Oni.png"
    if (difficulty == 1):
        img_path = "difficulty_UraOni.png"
    draw_small_pic(img_path, pic, (1050, 400), scale)

def draw_small_taiko(pic, scale):
    draw_small_pic("my_taiko.png", pic, (150,350), scale)

def draw_crown(pic, type=0, scale = 1):
    if (type == 0):
        img_path = "crown_Clear.png"
    if (type == 1):
        img_path = "crown_gold.png"
    draw_small_pic(img_path, pic, (1050, 600), scale)

if __name__ == '__main__':
    background = Image.open('background.png')
    background = draw_text("弩蚊怒夏", background, 120, (250, 150))
    background = draw_text("1000000", background, 120, (250, 300))
    draw_score_rank(background, 95, scale = 2)
    draw_small_taiko(background, scale = 2)
    draw_difficulty(background, scale = 2)
    draw_crown(background, type = 0, scale = 2)
    background.save('result.png')
    background.show()