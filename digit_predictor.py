import random
import math

minNum = int(input("最小数を入力してください: "))
maxNum = int(input("最大数を入力してください: "))
while minNum >= maxNum:
    print("最小数は最大数より小さくなければなりません。")
    minNum = int(input("最小数を入力してください: "))
    maxNum = int(input("最大数を入力してください: "))

randomNum = random.randint(minNum, maxNum)
difference = maxNum - minNum

loop = math.ceil(math.log2(difference + 1))

print(f"あなたは{loop}回以内に{minNum}から{maxNum}の間の数を当てなさい。")

while loop > 0:
    guess = int(input("数を入力してください: "))
    if guess == randomNum:
        print("正解です。")
        break
    elif guess < randomNum:
        print("もっと大きいです。")
    else:
        print("もっと小さいです。")
    loop -= 1
    if loop == 0:
        print(f"正解は{randomNum}です。")
        break
    print(f"残り{loop}回です。")
