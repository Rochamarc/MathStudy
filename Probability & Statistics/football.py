# Football statistics functions

def stats_per_game(stats: int, games: int, decimal_places: int=2) -> float:
    """Calculates statistics per games

    Parameters
    ----------
    stats : int
        A integer value for any statistics like: goals, assists, tacles, etc.
    games : int
        A integer value for number of games
    decimal_places : int
        A integer value number of decimal places
    
    Returns
    -------
        Return a float value for stat
    """

    return round((stats / games), decimal_places)

if __name__ == "__main__":
    print(stats_per_game(10, 38, decimal_places=1)) 
