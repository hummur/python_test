"""
第11章 プログラミング入門 チャレンジ
1．りんごと言われて思い浮かぶ、4つの属性を考えよう。その4つの属性をインスタンス変数に持つ、Appleクラスを定義しよう。
2．円を表すCircleクラスを定義しよう。そのクラスに、面積を計算して返すメソッドareaを持たせよう。面積の計算には、Pythonの組み込みモジュールmathのpi定数が使えます。次に、Circleオブジェクトを作って、areaメソッドを呼び出し、結果を出力しよう。

3．三角形を表すTriangleクラスを定義して、面積を返すareaメソッドを持たせよう。そしてTriangleオブジェクトを作って、areaメソッドを呼び出して、結果を出力しよう。
4．六角形を表すHexagonクラスを定義しよう。そのクラスには、外周の長さを計算して返すメソッドcalculate_perimeterを定義しよう。そして、Hexagonオブジェクトを作ってcalculate_perimeterメソッドを呼び出し、結果を出力しよう。

解答：http://tinyurl.com/gpqe62e
"""


# 1．りんごと言われて思い浮かぶ、4つの属性を考えよう。その4つの属性をインスタンス変数に持つ、Appleクラスを定義しよう。
class Apple:
    def __init__(self, c, s, pr, pl):
        self.color = c
        self.size = s
        self.price = pr
        self.place = pl


apple01 = Apple('blue', 'big', 200, '青森')
print(Apple)
print(apple01)
print(apple01.color)
print(apple01.size)
print(apple01.price)
print(apple01.place)


#2．円を表すCircleクラスを定義しよう。そのクラスに、面積を計算して返すメソッドareaを持たせよう。面積の計算には、Pythonの組み込みモジュールmathのpi定数が使えます。次に、Circleオブジェクトを作って、areaメソッドを呼び出し、結果を出力しよう。

import math

class Circle():
    def __init__(self, r):
        self.radius = r
        print(self.radius)

    def calculate_area(self):
        self.area = self.radius **2 * math.pi
        print(self.area)

circle = Circle(2)
circle.calculate_area()


# 3．三角形を表すTriangleクラスを定義して、面積を返すareaメソッドを持たせよう。そしてTriangleオブジェクトを作って、areaメソッドを呼び出して、結果を出力しよう。

class Triangle():
    def __init__(self,b,h):
        self.base = b
        self.height = h

    def culculate_area(self):
        self.area_result = (self.base * self.height) / 2
        print(self.area_result)

triangle = Triangle(2,5)
triangle.culculate_area()


# 4．六角形を表すHexagonクラスを定義しよう。そのクラスには、外周の長さを計算して返すメソッドcalculate_perimeterを定義しよう。そして、Hexagonオブジェクトを作ってcalculate_perimeterメソッドを呼び出し、結果を出力しよう。

class Hexagon():
    def __init__(self,s):
        self.side =  s
        print(self.side)

    def calculate_perimeter(self):
        perimeter = self.side * 6
        print('perimeter',perimeter)

    def calculate_area(self):
        area = self.side **2 *2.6
        print('area',area)


hexagon01 = Hexagon(10)
hexagon01.calculate_area()
hexagon01.calculate_perimeter()
