import sys

def point_relative_to_ellipse(ellipse_file, points_file):
    """Определяет положение точек относительно эллипса"""
    try:
        # Чтение параметров эллипса
        with open(ellipse_file, 'r') as f:
            center_line = f.readline().strip().split()
            radius_line = f.readline().strip().split()

            x_center, y_center = map(float, center_line)
            rx, ry = map(float, radius_line)

        # Чтение точек
        with open(points_file, 'r') as f:
            points = [line.strip().split() for line in f if line.strip()]

        results = []
        for point in points:
            x, y = map(float, point)
            # Вычисление уравнения эллипса
            value = ((x - x_center) / rx) ** 2 + ((y - y_center) / ry) ** 2

            if abs(value - 1) < 1e-10:  # Учет погрешности вычислений
                results.append(0)  # На окружности
            elif value < 1:
                results.append(1)  # Внутри
            else:
                results.append(2)  # Снаружи

        # Вывод результатов
        for result in results:
            print(result)

    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    if len(sys.argv) != 3:
        print("Использование: python task2.py ellipse_file points_file")
        return

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    point_relative_to_ellipse(ellipse_file, points_file)

if __name__ == "__main__":
    main()