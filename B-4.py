# 3都府県のいくつかの駅名とある日の最高気温のデータを辞書として持っています
# このデータを使って3つの問を満たす実装をしてください


def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # 気温の合計
    total_temp = sum(data["temperature"] for data in weather_information)
    # 平均気温 = 気温の合計 ／ 気温の要素数
    avg_temp = total_temp / len(weather_information)

    print(f"{avg_temp:.1f}")

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    osaka_station = [
        data["station"]
        for data in weather_information
        if data["prefecture"] == "大阪府"
    ]
    print(osaka_station)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)

    fukuoka_total_temp = sum(
        data["temperature"]
        for data in weather_information
        if data["prefecture"] == "福岡県"
    )
    fukuoka_area_num = len(
        [data for data in weather_information if data["prefecture"] == "福岡県"]
    )
    fukuoka_temp_ave = fukuoka_total_temp / fukuoka_area_num
    print(fukuoka_temp_ave)


if __name__ == "__main__":
    main()
