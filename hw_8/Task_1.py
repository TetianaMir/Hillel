import functools


class UnexpectedTypeException(Exception):
    pass


def expected(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if is_boolean_checker(result):
                result = bool
            try:
                if not isinstance(result, expected_types):
                    raise UnexpectedTypeException("It's unexpected type")
                else:
                    print("The result of functions:", func(*args, **kwargs), "is :", expected_types)
            except UnexpectedTypeException as exc:
                print(exc)

        return wrapper

    return decorator


@expected(str, int)
def func(value):
    return value


def is_boolean_checker(type):
    return isinstance(type, bool)


def main():
    func(7.6)  # unexpected type
    func(7)  # expected
    func(True)  # unexpected type


if __name__ == '__main__':
    main()
