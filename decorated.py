from functools import wraps


def positive_required(n):
    def decorator(f=-1):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if(n < 0):
                return 'number must be positive'

            return f(*args, **kwargs)

        return decorated_function
    return decorator


@positive_required
def check_number(n):
    print(n)


f = check_number(5)
print(f.__closure__)
