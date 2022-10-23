import functools


class UnexpectedTypeException(Exception):
    pass


def expected(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, expected_types):
                raise UnexpectedTypeException("It's unexpected type")
            else:
                print("The result of functions:", func(*args, **kwargs), "is :", expected_types)
                return result
        return wrapper
    return decorator


@expected(str, int)
def func(value):
    return value


def main():
    print(func("example"))  # expected


if __name__ == '__main__':
    main()
