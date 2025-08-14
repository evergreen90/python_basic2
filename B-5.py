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
        total += int(i)
    return total

print(f"合計値: {sum_number(data_sp)}")

# 最大値
def max_number(data_sp):
    max_number = 0
    for n in data_sp:
        if int(n) > max_number:
         max_number = int(n)
    return max_number

print(f"最大値: {max_number(data_sp)}")


# 最小値
def min_number(data_sp):
    min_value = data_sp[0]
    for n in data_sp[1:]:
        if n < min_value:
         min_value = n
    return min_value

print(f"最小値: {min_number(data_sp)}")


# 平均値
def sum(data_sp):
    total = 0
    for i in data_sp:
        total += int(i)
    return total

average = sum(data_sp) / data_sp_length 
print(f"平均値: {average:.0f}")

