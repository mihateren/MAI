from math import sin, cos, dist


x1, y1 = map(float, input().split())
p, fi = map(float, input().split())
x2 = p * cos(fi)
y2 = p * sin(fi)
print(dist((x1, y1), (x2, y2)))