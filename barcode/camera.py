# https://note.com/nao_py/n/ne77c782226d3 より
# import winsound
import cv2
import numpy as np
from pyzbar.pyzbar import decode

# クリップボードにコピー＆ペーストするライブラリ
# import pyautogui as pag
# import pyperclip

# Webカメラの読み込み
cap = cv2.VideoCapture(0)
# 出力ウィンドウの設定
cap.set(3,640)
cap.set(3,480)

while True:
    ret,frame = cap.read()
    key = cv2.waitKey(1) & 0xFF

    result = []
    for barcode in decode(frame):
        # QRコードを読み取り、画面にバウンディングボックスと文字列を表示する
        myData = barcode.data.decode('utf-8')
        result.append(myData)

        pts = np.array([barcode.polygon], np.int32)
        cv2.polylines(frame, [pts], True, (255,0,0), 5)
        pts2 = barcode.rect
        cv2.putText(
            frame, myData, (pts2[0],pts2[1]),
            cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2
        )
        
        # クリップボードにQRコードの内容をコピー
        # pyperclip.copy(myData)
        # ペーストする。
        # pag.hotkey('ctrl','v')
        # ペーストしたら「ラ」のビープ音を鳴らす
        # winsound.Beep(440,1000)
        
    # imshow()関数で出力ウィンドウを表示
    cv2.imshow('test',frame)
    if result:
        print(result)
    
    # qキーが押されたらループを終了する
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()