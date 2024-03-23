# Read ISBN number from barcode image.
import re
import os
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def is_valid_ISBN13(num: int) -> bool:
    """Function to validate if a given value is ISBN-13."""
    num_str = str(num)
    pattern = r"^97[89]"
    
    # check if `num` matches pattern
    if re.match(pattern, num_str):
        return True
    else:
        return False
    
def draw_rectangle(frame, barcodes, outpath: str):

    for bar in barcodes:
        pts = [(pt.x, pt.y) for pt in bar.polygon]
        print(pts)
        cv2.polylines(frame, [np.int32(pts)], True, (0, 255, 0), 2)
        
    cv2.imwrite(outpath, frame)

def read_ISBN_barcode(image_path: str) -> int:
    """
    Function to return ISBN-13 value which detected in given image.
    This function only returns the first ISBN even if more than two values were found.

    Parameters
    ----------
    image_path: str
        Path of image file.
    
    Returns
    -------
    isbn: int
        Detected value of ISBN-13.
    """
    # read image as gray scale
    frame = cv2.imread(image_path)
    basename = os.path.basename(image_path)

    if frame is None:
        raise FileNotFoundError("Failed in loading image")
    
    # detect barcodes
    barcodes = decode(frame)
    print(barcodes)

    draw_rectangle(frame, barcodes, os.path.join("barcode/out", basename))
    
    # return ISBN-13 values
    values = [b.data.decode() for b in barcodes]
    print(values)
    isbn = [v for v in values if is_valid_ISBN13(v)]
    return isbn

if __name__ == "__main__":
    # バーコードが写った画像ファイルのパス
    test_samples = [
        # "barcode/img/barpreview.png",   # pass
        "barcode/img/arukikata_taiwan.jpg",     # fail (incorrect value)
        # "barcode/img/arukikata.jpg",    # fail (can't detect)
        # "barcode/img/sample.jpg"        # pass
    ]
    
    for img_path in test_samples:
        # バーコードを読み取って数値を出力
        barcode_data = read_ISBN_barcode(img_path)
        print(barcode_data)