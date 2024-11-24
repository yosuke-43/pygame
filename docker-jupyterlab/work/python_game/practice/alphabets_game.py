import random
import datetime
import string
ALP = list(string.ascii_uppercase)
r = random.choice(ALP)
alp = ""

for i in ALP:
  if i != r:
    alp += i

print(alp)
st = datetime.datetime.now()
ans = input("抜けているアルファベットは？")

if ans == r:
  print("正解です")
  et = datetime.datetime.now()
  print(f"{(et - st).seconds}秒かかりました")
else:
  print("不正解です")

