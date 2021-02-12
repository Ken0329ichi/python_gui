# ティーケーインター機能を使うための設定
import tkinter as tk
import tkinter.ttk as ttk
# メッセージウィンドウ機能を使うための設定
from tkinter import messagebox


# ボタンが押されたときの処理
def button_clicked(radiobutton_value):
    # 選択されたラジオボタンから値を取得
    value = radiobutton_value.get()
    # 表示するメッセージの設定
    message = "あなたは、「{}」をえらびました。".format(value)
    # メッセージウィンドウの表示
    messagebox.showinfo("えらんだ結果", message)


# guiの定義処理
def gui_define():
    # メインウィンドウの定義
    root = tk.Tk()
    # ウィンドウタイトルの設定
    root.title("サンプル")
    # ウィンドウのサイズ変更の無効化
    root.resizable(False, False)
    # ウィンドウの表示位置
    root.geometry("+200+200")

    # メインフレームの定義
    frame = ttk.Frame(root)
    # ラベル付きフレームの定義
    label_frame = ttk.LabelFrame(frame,
                                 text="えらんで")


    # ラジオボタンが選択された値を保存する変数(初期値は"a"を入れておく)
    selected_value=tk.StringVar(value="a")
    # ラジオボタン「a」の定義
    radio_1 = tk.Radiobutton(
        label_frame,
        text="a",
        value="a",
        variable=selected_value)

    # ラジオボタン「b」の定義
    radio_2 = tk.Radiobutton(
        label_frame,
        text="b",
        value="b",
        variable=selected_value)


    # ボタンの定義(クリックされたら「button_clicked」の処理をする)
    button = ttk.Button(frame,
                        text="ボタン",
                        width=10, #ボタンの長さを10にする
                        command=lambda: button_clicked(selected_value))


    # ウィンドウにウィジェットを配置
    # メインフレームの配置
    frame.pack()
    # ラベル付きフレームの配置
    label_frame.pack()
    # ラジオボタンの配置
    radio_1.pack()
    radio_2.pack()
    # ボタンの配置(上下左右に「5」すきまを開ける)
    button.pack(padx=5, pady=5)
    
    # ウィンドウ表示
    root.mainloop()
    
    
# メイン処理
if __name__ == "__main__":
    
    gui_define()