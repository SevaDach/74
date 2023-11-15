#!/usr/bin/env -S python3 -B
from r2point import R2Point as Point
from convex import Void
from convex2 import tri


A = tri(Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0))
f = Void(A)
# = Void2()

try:
    # d = d.ad(R2Point())
    # d = d.ad(R2Point())
    # d = d.ad(R2Point())

    while True:
        f = f.add(Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, graniei = {f.otvet()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
