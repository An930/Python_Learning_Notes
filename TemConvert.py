#TemConvert.py
TemStr = input("请输入带符号的温度值：")
if TemStr[-1] in ['F','f']:
  C = (eval(TemStr[0:-1] - 32)) / 18
  print("转换后的温度值为摄氏{:.2f}度".format(C))
 elif TemStr[-1] in ['C','c']:
  F = 1.8 * eval(TemStr[0:-1] + 32
  print("转换后的温度值为华氏{:.2f}度".format(F))
 else:
  print("您输入的值有误，请重新输入！")
