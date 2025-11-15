import sys
import math

def point_relative_to_circle(circle_file, points_file):
    """Определяет положение точек относительно круга"""
    try:
        # Чтение параметров круга
        with open(circle_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            
            # Читаем координаты центра из первой строки
            center_line = lines[0].split()
            x_center, y_center = map(float, center_line)
            
            # Читаем радиус из второй строки
            radius_line = lines[1].split()
            if len(radius_line) == 2:
                # Если два числа, берем только первое как радиус
                radius = float(radius_line[0])
            else:
                # Если одно число, используем его
                radius = float(radius_line[0])
        
        # Чтение точек
        with open(points_file, 'r') as f:
            points = [line.strip().split() for line in f if line.strip()]
        
        results = []
        for point in points:
            x, y = map(float, point)
            # Вычисление расстояния от центра круга до точки
            distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)
            
            if abs(distance - radius) < 1e-10:  # Учет погрешности вычислений
                results.append(0)  # На окружности
            elif distance < radius:
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
        print("Использование: python task2.py circle_file points_file")
        print("В данном задании используйте: python task2.py circle.txt dot.txt")
        return
    
    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    
    point_relative_to_circle(circle_file, points_file)

if __name__ == "__main__":
    main()