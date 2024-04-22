from random import choice 

def get_divisions(max_dividend: int=100, max_divisor: int=100, only_integers: bool=True) -> list[list]:
    """Get the operation and their respetives results on divisions

    Parameters
    ----------
    max_dividend : int
        Maximum value for the dividend. Default value is 100
    max_divisor : int
        Maximum value for the divisor. Default value is 100
    only_integers : bool
        A bool value for the integer results. Type False to receive any type of division

    Returns
    -------
        A two dimentional list with the operation on a string format and the result on a int format
    """

    results = []

    for i in range(max_dividend + 1):
        for y in range(1, max_divisor + 1):
            
            problem, result = f"{i} ÷ {y}", i // y

            if only_integers:
                if i % y == 0 : results.append([ problem, result ])
            else:
                results.append([problem, result])
    
    return results

def fill_line(values: list, length: int) -> list[list[str, int]]:
    """Fill an one dimetional array

    Parameters
    ----------
    values : list
        A list of choices
    length : int
        An integer value for the length of the array
    
    Returns
    -------
        A random array
    """

    value = []

    for i in range(length):
        list_pointer = choice(values)

        if not list_pointer in value:
            value.append(list_pointer)
        else:
            i -= 1

    return value

if __name__ == "__main__":
    d = get_divisions(max_dividend=10,max_divisor=10)
    l = fill_line(d, 4)
    print(d)
    print(l)
