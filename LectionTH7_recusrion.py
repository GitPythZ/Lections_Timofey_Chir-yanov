# def matryoshka(n):
#     if n == 1:
#         print("матрёшечка")
#     else:
#         print("Верх матрешки n=", n)
#         matryoshka(n -1)
#         print("Низ матрешки n=", n)
#
#
# matryoshka(5)

# import tkinter as tk
import graphics as gr
window = gr.GraphWin("Russian game", 800, 800)
alpha = 0.1


def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
        A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
        B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
        C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
        D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
        fractal_rectangle(A1, B1, C1, D1, deep - 1)


fractal_rectangle((100,100), (500,100), (500,500), (100,500), 10)

#gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
# gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
# gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
# gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)


def f(n:int):
    assert n >= 0, "Факториал отрицательных не определен"
    if n == 0:
        return 1
    return f(n-1) * n


print(f(5))


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(b, b - a)


print(gcd(8, 10))


def gcd1(a, b):
    if b == 0:
        return a
    else:
        return gcd1(b, a % b)


print(gcd1(80, 100))


def gcd2(a, b):
    return a if b == 0 else gcd2(b, a % b)


print(gcd2(125, 225))


def pow(a:float, n:int):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n-1) * a
    else:
        return pow(a ** 2, n // 2)


print(pow(2, 24))
