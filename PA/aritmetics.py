#
#
#
from functools import wraps
import time


def timeit(func):
    """Compare the time to run a function
    
    Retruns
    -------
    function : the same function that enters
    """

    @wraps(func)
    def timeit_wrapper(*args: any, **kwargs: any):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


class PA:
    def __init__(self, first_term: int | float, difference: int | float, n_last_term: int | float):
        self.first_term = first_term
        self.n_last_term = n_last_term
        self.difference = difference

    @timeit
    def pa(self) -> list:
        return [ self.first_term + ( i * self.difference ) for i in range(self.n_last_term) ]


class PA_Formula:
    def __init__(self, first_term: int | float, difference: int | float, n_last_term: int | float):
        self.first_term = first_term
        self.n_last_term = n_last_term
        self.difference = difference
    
    @timeit
    def get_last(self) -> float:
        return self.first_term + (self.n_last_term - 1) * self.difference

if __name__ == "__main__":
    a = PA(2233, 22222582, 12444448)
    print(a.pa()[-1])

    b = PA_Formula(2233, 22222582, 12444448)
    print(b.get_last())