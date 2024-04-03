import math

def simple_average(values: list, decimal_places: int=2) -> float:
    """Calculates a simple average value from a list

    Parameters
    ----------
    values : list
        A list containing numeric values
    decimal_places : int
        Number of decimal places of the result. default value = 2

    Returns
    -------
        A float value for the aritimetic value
    """

    result = sum(values) / len(values)

    return round(result, decimal_places)

def standart_deviation(values: list, decimal_places: int=2) -> float:
    """Calculates the standart deviation from a list of values

    Parameters
    ----------
    values : list
        A list containing numeric values
    decimal_places : int
        Number of decimal places of the result. default value = 2

    Returns
    -------
        A float value for the standart deviation
    """

    # Get the average value
    avg = simple_average(values)

    # calculates the sum of the values minus the average squared
    dif = sum([ (val - avg)**2 for val in values ]) / 2

    # returns the standart deviation
    result = math.sqrt(dif)

    return round(result, decimal_places)

def weighted_average(values: list, decimal_places: int=2) -> float:
    """Calculates a weighted average value from a list of values

    Parameters
    ----------
    values : list
        A two dimensional list containing a numerica value and a weight in each line
    decimal_places : int
        Number of decimal places of the result. default value = 2

    Returns
    -------
        A float value for the weighted aritimetic value
    """
    multiplied_values = [ i[0] * i[-1] for i in values ]
    summed_weights = sum([ i[-1] for i in values ])

    result = sum(multiplied_values) / summed_weights

    return round(result, decimal_places)

if __name__ == "__main__":
    from random import randint 

    ages = [ randint(12, 16) for _ in range(3) ]
    
    print(ages)
    print(simple_average(ages))
    print(standart_deviation(ages))

    # for the weighted average 
    grades = [
        [10.0, 2],
        [6, 4],
        [8.7, 4],
        [10.0, 3],
        [7, 2],
        [4, 4],
        [1, 2],
        [0, 4],
        [6, 4]
    ]

    print(weighted_average(grades))