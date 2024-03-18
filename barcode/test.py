import cv2
from pyzbar.pyzbar import decode

def read_barcode(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path)
    
    # グレースケールに変換
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # バーコードを検出
    barcodes = decode(gray)
    
    if barcodes:
        # # 最初に見つかったバーコードのデータを返す
        # return barcodes[0].data.decode("utf-8")
        result = [b.data.decode("utf-8") for b in barcodes]
        return result
    else:
        return "バーコードが見つかりませんでした"

if __name__ == "__main__":
    # バーコードが写った画像ファイルのパス
    image_path = "barcode/barcode.jpg"  # ここに実際のファイルパスを指定してください
    
    # バーコードを読み取って数値を出力
    barcode_data = read_barcode(image_path)
    print("バーコードに書かれている数値:", barcode_data)
