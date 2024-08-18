# Решето Эратосфена

# n = int(input())
# A = [True] * n
# A[0] = A[1] = False
# for k in range(2, n):
#     for m in range(2 * k, n, k):
#         A[m] = False
# print(A)
# for k in range(n):
#     print(k, "-", "простое" if A[k] else "составное")


# Циклический сдвиг в массиве

# Сдвиг влево
A = [0, 1, 2, 3, 4, 5, 6]
n = len(A)
tmp = A[0]  # временная переменная
for k in range(n - 1):
    A[k] = A[k + 1]
A[n - 1] = tmp
print(A)

# Сдвиг вправо
A = [0, 1, 2, 3, 4, 5, 6]
n = len(A)
tmp = A[n - 1]  # временная переменная
for k in range(n - 2, -1, -1):
    A[k + 1] = A[k]
A[0] = tmp
print(A)

# Построение функции для обращения массива
A = [1, 2, 3, 4, 5]
B = []


def invert_array(A: int, N: int):
    """ Обращение массива (поворот задом-наперёд).
        В рамках индексов от 0 до N - 1.
    """
    A = [1, 2, 3, 4, 5]
    print(A)
    for k in range(N):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]
    print(A) # [1, 2, 3, 4, 5]
        # A[k] = B[N-1-k]
    for k in range(N // 2):
        A[k], A[N - 1 - k] = A[N - 1 - k], A[k]
    print(A) #[5, 4, 3, 2, 1]


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array()
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print("Ok")
    else:
        print("Fail")


invert_array(A=[1, 2, 3, 4, 5], N=len(A))
