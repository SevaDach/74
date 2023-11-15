from r2point import R2Point
from convex import Figure, Void
from convex2 import tri


def test_000():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0, 0))
    assert f.area() == 0 and f.perimeter() == 0 and f.otvet() == 0


def test_001():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.9, 0.8))
    f = f.add(R2Point(0.9, 0.7))
    assert f.area() == 0 and f.perimeter() < 0.21 and\
           f.perimeter() > 0.2 and f.otvet() == 1


def test_002():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.9, 0.8))
    assert f.area() == 0 and f.perimeter() == 0 and f.otvet() == 0


def test_003():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.9, 0.8))
    f = f.add(R2Point(0.9, 0.8))
    f = f.add(R2Point(0.9, 0.8))
    f = f.add(R2Point(0.9, 0.8))
    assert f.area() == 0 and f.perimeter() == 0 and f.otvet() == 0


def test_004():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.9, 0.8))
    f = f.add(R2Point(0.9, 0.7))
    f = f.add(R2Point(0.9, 0.75))
    assert f.area() == 0 and f.perimeter() > 0.2 and\
           f.perimeter() < 0.21 and f.otvet() == 1


def test_005():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.9, 0.7))
    f = f.add(R2Point(0.9, 0.6))
    f = f.add(R2Point(0.8, 0.6))
    assert f.area() > 0.004 and f.area() < 0.005 and\
           f.perimeter() > 0.341 and\
           f.perimeter() < 0.342 and f.otvet() == 3


def test_006():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.9, 0.7))
    f = f.add(R2Point(0.9, 0.6))
    f = f.add(R2Point(0.8, 0.6))
    f = f.add(R2Point(0.8, 0.7))
    assert f.area() > 0.009 and f.area() < 0.01 and\
           f.perimeter() > 0.39 and\
           f.perimeter() < 0.4 and f.otvet() == 4


def test_007():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.1, 0.7))
    f = f.add(R2Point(0.9, 0.6))
    f = f.add(R2Point(0.8, 0.6))
    assert f.area() > 0.0049 and f.area() < 0.005 and\
           f.perimeter() > 1.61 and\
           f.perimeter() < 1.62 and f.otvet() == 1


def test_008():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0, 0))
    f = f.add(R2Point(1, 0))
    f = f.add(R2Point(1, 1))
    assert f.area() == 0.5 and f.perimeter() > 3.41 and\
           f.perimeter() < 3.42 and f.otvet() == 0


def test_009():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.9, 0.7))
    f = f.add(R2Point(0.9, 0.6))
    f = f.add(R2Point(0.8, 0.6))
    f = f.add(R2Point(0.5, 1))
    assert f.area() > 0.039 and f.area() < 0.04 and\
           f.perimeter() == 1.2 and f.otvet() == 2


def test_010():  # базовая проверка работы программы
    A = tri(R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0))
    f = Void(A)
    f = f.add(R2Point(0.9, 0.7))
    f = f.add(R2Point(0.9, 0.6))
    f = f.add(R2Point(0.8, 0.6))
    f = f.add(R2Point(0.5, 1))
    f = f.add(R2Point(1.5, 0.3))
    assert f.area() > 0.095 and f.area() < 0.096 and\
           f.perimeter() > 2.4 and\
           f.perimeter() < 2.5 and f.otvet() == 0
