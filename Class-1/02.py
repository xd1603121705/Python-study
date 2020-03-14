"""
将华氏温度转变成摄氏温度

Version: 1.0
Author: junlee_happy@163.com
"""
import math

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

"""
输入半径计算圆的周长和面积

Version: 1.0
Author: jun
"""

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)
