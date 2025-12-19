def convert_to_int(value: str | float) -> int:
    try:
        convertedValue = int(value)
    except ValueError:
        print(f"Преобразование {value} в целое число невозможно из-за некорректного значения")
    except Exception as e:
        print(f"Преобразование {value} в целое число завершилось ошибкой: {e}")
    finally:
        print(f"Попытка преобразования {value} в целое число завершена")
        
convert_to_int("123")
convert_to_int("asd")
convert_to_int([1, 2, 3])