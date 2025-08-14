# スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
# 合計値
# 最大値
# 最小値
# 平均値
# ただし、計算用の組み込み関数やライブラリは使わないこと(sum()やnp.mean()などはNG print()はOK)
# 1つの統計量につき、それ専用の関数を実装すること

# 例)
# データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
# 合計値: 54
# 最大値: 21
# 最小値: 1
# 平均値: 6

data = input("データを入力してください（スペース区切り）：")
data_sp = data.split()
data_sp_length = len(data_sp)

# 合計値
def sum_number(data_sp):
    total = 0
    for i in data_sp:
        total += i
    print(f"合計値: {sum_number(data_sp)}")



# 最大値


# 最小値


# 平均値


