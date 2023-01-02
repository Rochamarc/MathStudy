

def for_i_in_float(value):
    """
    I'm only working with one value after coma, but the idea is to automize 
    with an new argument specifying the number of decimal places
    """
    for i in range(10):
        yield (float(f'{value}.{i}'))

if __name__ == "__main__":

    for i in range(10):
        i += 1
        a = for_i_in_float(i)

        for i in a:
            print(i)