# https://note.com/nao_py/n/ne77c782226d3 より
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from isbn import is_valid_ISBN13
from google_books import cui

# setup
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(3,480)
isbn = None

while True:
    ret, frame = cap.read()
    key = cv2.waitKey(1) & 0xFF

    for barcode in decode(frame):

        value = barcode.data.decode('utf-8')
        if is_valid_ISBN13(value):
            # draw detected area as polygon, value as text
            pts = np.array([barcode.polygon], np.int32)
            cv2.polylines(frame, [pts], True, (255,0,0), 5)
            pts2 = barcode.rect
            cv2.putText(
                frame, value, (pts2[0],pts2[1]),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2
            )
            # skip other values
            isbn = value
        
    # show current frame
    cv2.imshow('Capture barcode', frame)
    if isbn:
        print(isbn)
        cui(isbn)
        isbn = None
    
    # press 'q' to quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()