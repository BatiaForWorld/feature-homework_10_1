def log(filename=None):
    """
    Декоратор, который автоматически регистрирует детали выполнения функций,
    такие как время вызова, имя функции, передаваемые аргументы,
    результат выполнения и информация об ошибках.
    Это позволит обеспечить более глубокий контроль и анализ поведения программы в процессе ее выполнения.

    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                '''После успешного выполнения функции записывается сообщение вида "<имя_функции> ok".'''
                log_message = f"{func.__name__} ok"
            except Exception as e:

                '''Если во время выполнения функции возникает исключение, оно перехватывается,
     и в лог записывается сообщение вида "<имя_функции> error: <описание_ошибки>.'''
                log_message = f"{func.__name__} error: {str(e)}. Inputs: {str(args)}, {str(kwargs)}"
                result = None
            if filename:
                '''Имя файла для записи логов. Если указано, логирование происходит в файл,
      иначе — вывод в стандартный поток вывода (консоль).'''
                with open(filename, "a") as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)
            return result

        return wrapper

    return decorator
