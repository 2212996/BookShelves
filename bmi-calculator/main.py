# -*- coding: utf-8 -*-

import sys
sys.path.append("/Users/tsutsuitomoya/Documents/GitHub/BookShelves/bmi-calculator")
import webbrowser
from pathlib import Path

from flask import Flask, render_template, request
from flask_cors import CORS

def base_dir():
    if hasattr(sys, "_MEIPASS"):
        # 実行ファイルで起動した場合、展開先ディレクトリを基点とする。
        return Path(sys._MEIPASS)
    else:
        # python コマンドで起動した場合、プロジェクトディレクトリを基点とする。
        return Path("..")


app = Flask(
    __name__,
    template_folder=base_dir() / "dist",
    static_folder=base_dir() / "dist/static",
)
CORS(app)

@app.route("/api/get_bmi", methods=["POST"])
def get_bmi():
    """BMI、標準体重を計算して返す API

    Returns:
        dict: レスポンス
    """
    data = request.get_json(force=True)

    # 入力を数値に変換する。
    try:
        height_cm = float(data["height"])
        weight_kg = float(data["weight"])
    except:
        return {"success": False, "message": "入力データが不正です。"}

    if height_cm <= 0 or weight_kg <= 0:
        return {"success": False, "message": "入力データが不正です。"}
    print(F"リクエストを受け取りました。({weight_kg:.1f}cm, {height_cm:.1f}kg)")

    # BMI 及び標準体重を計算する。
    height_m = height_cm / 100
    bmi = weight_kg / height_m**2
    normal_weight = height_m ** 2 * 22

    return {"success": True, "bmi": bmi, "normal_weight": normal_weight}

@app.route("/")
def index():
    """フロントエンド側のページを表示する。

    Returns:
        str: HTML
    """
    return render_template("index.html")

def main():
    webbrowser.open("http://localhost:5000/", new=2, autoraise=True)
    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()