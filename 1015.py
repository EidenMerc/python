import math

p1 = input().split(" ")
p2 = input().split(" ")

x1, y1 = p1
x2, y2 = p2

calc1 = (float(x2) - float(x1)) ** 2
calc2 = (float(y2) - float(y1)) ** 2
soma = calc1 + calc2

distancia = math.sqrt(soma)

print('%0.4f' %distancia)

