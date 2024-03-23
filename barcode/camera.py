# https://note.com/nao_py/n/ne77c782226d3 より
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from isbn import is_valid_ISBN13

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

        value = barcode.data.decode('utf-8')
        if is_valid_ISBN13(value):
            result.append(value)

            # draw detected area as polygon, value as text
            pts = np.array([barcode.polygon], np.int32)
            cv2.polylines(frame, [pts], True, (255,0,0), 5)
            pts2 = barcode.rect
            cv2.putText(
                frame, value, (pts2[0],pts2[1]),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2
            )
            # skip other values
            break
        
    # show current frame
    cv2.imshow('test', frame)
    if result:
        print(result)
    
    # press 'q' to quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()