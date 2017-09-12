
def float_args_and_return(function):
    def wrapper(*args, **kwargs):
        args = [float(arg) for arg in args]
        return float(function(*args, **kwargs))
    return wrapper

@float_args_and_return  # 等价于“mean = float_args_and_return(mean)”
def mean(first, second, *rest):
    numbers = (first, second) + rest
    return sum(numbers) / len(numbers)

print(mean(5, '6', '7.6'))
