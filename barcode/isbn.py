# Read ISBN number from barcode image.
import re
import cv2
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
    frame = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if frame is None:
        return None
    
    # detect barcodes
    barcodes = decode(frame)
    
    # return ISBN-13 values
    values = [b.data.decode("utf-8") for b in barcodes]
    isbn = [v for v in values if is_valid_ISBN13(v)][0]
    return isbn

if __name__ == "__main__":
    # バーコードが写った画像ファイルのパス
    image_path = "barcode/sample.jpg"  # ここに実際のファイルパスを指定してください
    
    # バーコードを読み取って数値を出力
    barcode_data = read_ISBN_barcode(image_path)
    print(barcode_data)