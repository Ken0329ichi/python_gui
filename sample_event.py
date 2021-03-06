import random
import tkinter as tk


# ↓↓↓ マウスとキーボードイベント定義 ↓↓↓
# マウスイベント定義
def mouse_motion(event):
    # マウスを動かした座標の取得
    x = event.x
    y = event.y
    # 白い丸にマウスの座標を設定
    c.coords('white_ball',
             x - 10,
             y - 10,
             x + 10,
             y + 10)

# キーボードの上矢印キーイベントの定義
def keyboard_up_motion(event):
    # 白い丸の現在の座標の取得
    (x0, y0, x1, y1) = c.bbox('white_ball')
    # 表示されているキャンパス内であれば、白い丸を上に動かす。
    if y0 > -1:
        c.move('white_ball', 0, -1)

# キーボードの下矢印キーイベントの定義
def keyboard_down_motion(event):
    # 白い丸の現在の座標の取得
    (x0, y0, x1, y1) = c.bbox('white_ball')
    # 表示されているキャンパス内であれば、白い丸を下に動かす。
    if y1 < 500:
        c.move('white_ball', 0, 1)

# キーボードの右矢印キーイベントの定義
def keyboard_right_motion(event):
    # 白い丸の現在の座標の取得
    (x0, y0, x1, y1) = c.bbox('white_ball')
    # 表示されているキャンパス内であれば、白い丸を右に動かす。
    if x1 < 700:
        c.move('white_ball', 1, 0)
        
# キーボードの左矢印キーイベントの定義
def keyboard_left_motion(event):
    # 白い丸の現在の座標の取得
    (x0, y0, x1, y1) = c.bbox('white_ball')
    # 表示されているキャンパス内であれば、白い丸を左に動かす。
    if x0 > -1:
        c.move('white_ball', -1, 0)    
# ↑↑↑ マウスとキーボードイベント定義 ↑↑↑

a = [random.randint(30, 470),
     random.randint(30, 470)]

b = (10, 10)

root = tk.Tk()

c = tk.Canvas(root,
              width = 700,
              height = 500)

c.pack()

c.create_rectangle(a[0]+15, a[1]-15,
                   a[0]-15, a[1]+15,
                  fill = 'black')

# 白い丸の定義
c.create_oval(b[0]+10, b[1]-10,
              b[0]-10, b[1]+10,
              fill = 'white',
              tag = 'white_ball') # tag定義の追加
        
c.create_polygon(480, 20,
                 480, 10,
                 482, 5,
                 485, 2,
                 490, 0,
                 495, 2,
                 498, 5,
                 500, 10,
                 500, 20,
                 fill = 'brown')

c.create_line(480, 10,
              500, 10)

c.create_rectangle(479, 10,
                   481,12,
                   fill = 'white')

c.create_rectangle(500, 0,
                   700, 500,
                   fill = 'yellow')

c.create_text(520, 5,
              text = '持ち物',
              font = ('FIxedSys', 10),
              fill = 'black')

# ↓↓↓ イベントの設定 ↓↓↓
c.tag_bind('white_ball', '<Button1-Motion>', mouse_motion) # 左クリックドラッグのマウスイベントの設定
c.bind('<Up>', keyboard_up_motion) # 上矢印キーを押したときのイベントの設定
c.bind('<Down>', keyboard_down_motion) # 下矢印キーを押したときのイベントの設定
c.bind('<Right>', keyboard_right_motion) # 右矢印キーを押したときのイベントの設定
c.bind('<Left>', keyboard_left_motion) # 左矢印キーを押したときのイベントの設定
c.focus_set() # キャンパスをフォーカス
# ↑↑↑ イベントの設定 ↑↑↑

root.mainloop