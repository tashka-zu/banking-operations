import os


def log(filename=""):
    """Декоратор для логирования выполнения функций"""
    def my_decorator(func):
        """Декоратор, который используется внутри функции для регистрации событий"""
        def wrapper(*args, **kwargs):
            """Обертка для функции, которая добавляет логирование"""
            try:
                result = func(*args, **kwargs)
                if os.path.isfile(filename):
                    with open(filename, "a") as file:
                        output = f"{func.__name__} ok\n"
                        file.write(output)
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if os.path.isfile(filename):
                    with open(filename, "a") as file:
                        output = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                        file.write(output)
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")

        return wrapper

    return my_decorator
