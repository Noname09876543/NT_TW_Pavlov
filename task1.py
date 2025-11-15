import sys

def circular_array_path(n, m):
    """Вычисляет путь для кругового массива"""
    path = []
    current = 1
    first_element = True

    while first_element or current != 1:
        first_element = False
        path.append(str(current))
        # Вычисляем следующую начальную позицию
        current = (current + m - 2) % n + 1

    return ''.join(path)

def main():
    if len(sys.argv) != 5:
        print("Использование: python task1.py n1 m1 n2 m2")
        return

    try:
        n1, m1, n2, m2 = map(int, sys.argv[1:5])

        path1 = circular_array_path(n1, m1)
        path2 = circular_array_path(n2, m2)

        print(path1 + path2)

    except ValueError:
        print("Все аргументы должны быть целыми числами")

if __name__ == "__main__":
    main()