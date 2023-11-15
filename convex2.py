from r2point import R2Point as Point


class tri:

    def __init__(self, a, b, c):
        self.spisok = [a, b, c]

    def add(self, point):
        self.spisok.append(point)

    def pprint(self):
        for i in range(len(self.spisok)):
            print(self.spisok[i].x, self.spisok[i].y)


def sk(v1, v2):
    return v1.x * v2.x + v1.y * v2.y


def is_in_triangle(p, A):

    a = A.spisok[0]
    b = A.spisok[1]
    c = A.spisok[2]

    v0 = Point(c.x - a.x, c.y - a.y)
    v1 = Point(b.x - a.x, b.y - a.y)
    v2 = Point(p.x - a.x, p.y - a.y)

    dot00 = sk(v0, v0)
    dot01 = sk(v0, v1)
    dot02 = sk(v0, v2)
    dot11 = sk(v1, v1)
    dot12 = sk(v1, v2)

    inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    return (u > 0) and (v > 0) and (u + v < 1)


A = tri(Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0))
triangle = [Point(0, 0), Point(1, 1), Point(0, 1)]
# print(is_in_triangle(point, A))
# a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
# A.pprint()
