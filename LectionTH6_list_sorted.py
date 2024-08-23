# A = [1, 2, 3, 4, 5, 7, 12, 6, -1, -10, 44, 14]
# B = []
# for x in A:
#     if x % 2 == 0:
#         B.append(x)
# print(B)
# B = [x**2 for x in A if x % 2 == 0]
# print(B)
# B = [0 if x < 0 else x**2 for x in A if x % 2 == 0]
# print(B)
# Квадратичные сортировки

# Сортировка вставками

def insert_sort(A):
    """ Сортировка списка А вставками.""" # help(insert_sort) - вызов док-строки функции
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def choice_sort (A):
    """ Сортировка списка А выбором."""
    N = len(A)
    for pos in range(0, N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """Сортировка списка А пузырьком."""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N - bypass):
            if A[k] > A[k + 1]:
                A [k], A[k + 1] = A[k + 1], A[k]
    pass


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10)) # списки моежно конкатенировать [0] *10 == [0] + [0] + ... == list(b) + list(C)
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")


test_sort(insert_sort)
test_sort(choice_sort)
test_sort(bubble_sort)

# Сортировка подсчетом

