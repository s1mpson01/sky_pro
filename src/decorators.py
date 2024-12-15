from functools import wraps


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(f"{message}")
            else:
                if filename:
                    with open(f"{filename}.txt", "w", encoding="utf-8") as file:
                        file.write(message + "\n")
                else:
                    print(f"{message}")
                return result

        return inner

    return wrapper
