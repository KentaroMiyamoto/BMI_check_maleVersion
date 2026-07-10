import sys
import os

import pandas as pd

sys.path.append("./consts_files")

import default_parameter


def main():
    height = default_parameter.my_height
    weight = 0
    data = "data/weight.csv"

    try:
        # 入力
        # --- 身長 ---
        height = float(input("あなたの身長[m]を入力してください(例: 173cm/1.73m → 1.73)"))
        # --- 体重 ---
        weight = int(input("あなたの体重[kg]を入力してください(例: 50kg → 入力: 50)"))
        print("【体重】")
        print(f"あなたの現在の体重は{weight}kgです")

        # bmi計算
        if weight > 0:
            print("【bmi】")
            bmi = round(weight / height / height)
            print(f"あなたのbmiは{bmi}です")

        # bmi評価
        print("【評価】")
        if bmi < 18.5:
            print("あなたは痩せすぎです。もっと食べましょう。")
        elif bmi >= 25:
            print("あなたは太りすぎの肥満です。痩せましょう。")
        else:
            print("あなたは標準的な体重です。このまま、健康的な生活をしましょう。")

        # データ保存
        if os.path.isfile(data):
          pass
    except ValueError:
        print("【警告】")
        print("整数を入力してください")
        print("最初から再実行してください。")

if __name__ == "__main__":
    main()