import sys
import json

def fill_values(test_structure, values_dict):
    """Рекурсивно заполняет значения в структуре тестов"""
    if isinstance(test_structure, dict):
        # Если у элемента есть id, заполняем value
        if 'id' in test_structure and test_structure['id'] in values_dict:
            test_structure['value'] = values_dict[test_structure['id']]
        
        # Рекурсивно обрабатываем вложенные элементы
        for key, value in test_structure.items():
            if isinstance(value, (dict, list)):
                fill_values(value, values_dict)
    
    elif isinstance(test_structure, list):
        for item in test_structure:
            fill_values(item, values_dict)

def main():
    if len(sys.argv) != 4:
        print("Использование: python task3.py tests.json values.json report.json")
        return
    
    tests_file, values_file, report_file = sys.argv[1:4]
    
    try:
        # Чтение файлов
        with open(tests_file, 'r', encoding='utf-8') as f:
            tests_data = json.load(f)
        
        with open(values_file, 'r', encoding='utf-8') as f:
            values_data = json.load(f)
        
        # Создание словаря значений для быстрого доступа
        values_dict = {item['id']: item['value'] for item in values_data['values']}
        
        # Заполнение значений в структуре тестов
        fill_values(tests_data, values_dict)
        
        # Запись результата
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(tests_data, f, indent=2, ensure_ascii=False)
        
        print(f"Отчет успешно сохранен в {report_file}")
    
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()