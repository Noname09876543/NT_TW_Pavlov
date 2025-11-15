import sys

def min_moves_to_equal(nums):
    """Вычисляет минимальное количество ходов для приведения к одному числу"""
    nums.sort()
    n = len(nums)
    
    # Медиана минимизирует сумму абсолютных отклонений
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        # Для четного количества можно взять любую из двух средних
        median = nums[n // 2 - 1]
    
    # Вычисляем сумму абсолютных разностей
    moves = sum(abs(num - median) for num in nums)
    
    return moves

def main():
    if len(sys.argv) != 2:
        print("Использование: python task4.py numbers_file")
        return
    
    numbers_file = sys.argv[1]
    
    try:
        # Чтение чисел из файла
        with open(numbers_file, 'r') as f:
            numbers = [int(line.strip()) for line in f if line.strip()]
        
        if not numbers:
            print("Файл пуст")
            return
        
        moves = min_moves_to_equal(numbers)
        
        if moves <= 20:
            print(moves)
        else:
            print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
    
    except FileNotFoundError:
        print(f"Файл {numbers_file} не найден")
    except ValueError:
        print("Файл должен содержать только целые числа")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()