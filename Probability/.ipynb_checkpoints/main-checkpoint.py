from random import randint 


def make_choice(value: int) -> bool:
    """Generates a decision based on a value

    Parameters
    ----------
    value : int
        A value between 0 and 100
    """
    
    if not (0 <= value <= 100):
        raise(ValueError, 'the interval of the value is not value')
    
    return randint(0,100) < value

def calculate_probability(values: list) -> dict:
    total = len(values)
    truths = sum([ i for i in values if i ]) / total
    falses = round(((total / 10) - truths), 1)
    return { 'true': truths, 'false': falses }
    
if __name__ == "__main__":
    for _ in range(10):
        print(make_choice(50))