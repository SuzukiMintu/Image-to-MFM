import copy, numpy as np
from PIL import Image

# 特定の文字数だけ0で埋める関数
def zero_fill(val, n):
    if len(val) < n:
        val = "0"*(n-1) + val
    return val

with open("file_set.txt", "r", encoding="UTF-8") as file:
    file_split = file.read().splitlines()
    print(file_split)
    mode = file_split[0]
    filename = file_split[1]

# pngファイル読み込み
img = np.array(Image.open(filename).convert("RGBA"))
canvas_size = [img.shape[1], img.shape[0]]
dot_size = 16/canvas_size[0]*50 if canvas_size[0] > canvas_size[1] else 16/canvas_size[1]*50
dot = [[[tuple(img[y][x]), [x*dot_size, y*dot_size], 1 if img[y][x][3] != 0 else 0] if x != canvas_size[0] and y != canvas_size[1] else [(255, 255, 255, 0), [x*dot_size, y*dot_size], 0] for x in range(canvas_size[0]+1)] for y in range(canvas_size[1]+1)]

# MFMアートの保存
if mode == "0":
    mfm, bg_color = "$[scale.y=0.75 ", [["ff", "ff", "ff", 0], ["ff", "ff", "ff", 0]]
    for y in range(canvas_size[1]):
        mfm_space, now_paint = "", 0
        for x in range(canvas_size[0]):
            bg_color[1] = bg_color[0]
            bg_color[0] = [format(dot[y][x][0][0], 'x'), format(dot[y][x][0][1], 'x'), format(dot[y][x][0][2], 'x'), dot[y][x][0][3]]
            bg_color[0][0], bg_color[0][1], bg_color[0][2] = zero_fill(bg_color[0][0], 2), zero_fill(bg_color[0][1], 2), zero_fill(bg_color[0][2], 2)
            if bg_color[0][3] != 0 and bg_color[0] != bg_color[1]:
                mfm += "]" if bg_color[1][3] != 0 and x != 0 and now_paint == 1 else ""
                mfm += f"{mfm_space}$[bg.color={bg_color[0][0]}{bg_color[0][1]}{bg_color[0][2]} "
                mfm_space = ""
                now_paint = 1
            elif bg_color[0][3] == 0 and now_paint == 1:
                mfm += "]"
                now_paint = 0
            mfm_space += "　" if now_paint == 0 else ""
            mfm += "　" if now_paint == 1 else ""
        mfm += "]" if now_paint == 1 else ""
        if y != canvas_size[1]-1:
            mfm += "\n"
        bg_color = [["ff", "ff", "ff", 0], ["ff", "ff", "ff", 0]]
    mfm += "]"
    with open(f"{filename.split('/')[-1].replace('.png', '')}.txt", "w", encoding="UTF-8") as mfm_txt:
        mfm_txt.write(mfm)

# 減色バージョン
elif mode == "1":
    mfm, bg_color = "$[scale.y=0.75 ", [["f", "f", "f", "0"], ["f", "f", "f", "0"]]
    for y in range(canvas_size[1]):
        mfm_space, now_paint = "", 0
        for x in range(canvas_size[0]):
            bg_color[1] = bg_color[0]
            bg_color[0] = [format(dot[y][x][0][0], 'x'), format(dot[y][x][0][1], 'x'), format(dot[y][x][0][2], 'x'), format(dot[y][x][0][3], 'x')]
            bg_color[0][0], bg_color[0][1], bg_color[0][2], bg_color[0][3] = list(zero_fill(bg_color[0][0], 2))[0], list(zero_fill(bg_color[0][1], 2))[0], list(zero_fill(bg_color[0][2], 2))[0], list(zero_fill(bg_color[0][3], 2))[0]
            if bg_color[0][3] == "f":
                bg_color[0][3] = ""
            if bg_color[0][3] != "0" and bg_color[0] != bg_color[1]:
                mfm += "]" if bg_color[1][3] != "0" and x != 0 and now_paint == 1 else ""
                mfm += f"{mfm_space}$[bg.color={bg_color[0][0]}{bg_color[0][1]}{bg_color[0][2]}{bg_color[0][3]} "
                mfm_space = ""
                now_paint = 1
            elif bg_color[0][3] == "0" and now_paint == 1:
                mfm += "]"
                now_paint = 0
            mfm_space += "　" if now_paint == 0 else ""
            mfm += "　" if now_paint == 1 else ""
        mfm += "]" if now_paint == 1 else ""
        if y != canvas_size[1]-1:
            mfm += "\n"
        bg_color = [["f", "f", "f", "0"], ["f", "f", "f", "0"]]
    mfm += "]"
    with open(f"{filename.split('/')[-1].replace('.png', '')}.txt", "w", encoding="UTF-8") as mfm_txt:
        mfm_txt.write(mfm)
