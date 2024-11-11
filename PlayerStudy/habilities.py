class Hability:
    """
    A class that represents a Football/Soccer player habilities

    Attributes
    ----------
    position : str
        Two capital letters that represents the players position
     positioning : int
        A integer that value for player positioning GK only
    reflexes : int
        A integer that value for player reflexes GK only
    diving : int
        A integer that value for player diving GK only
    standing_tackle : int
        A integer that value for player standing tackle Non GK players
    physical : int
        A integer that value for player physical Non GK players
    passing : int
        A integer that value for player passing Non GK players
    dribbling : int
        A integer that value for player dribbling Non GK players
    long_shot : int
        A integer that value for player long shot Non GK players
    finishing : int
        A integer that value for player finishing Non GK players
    
    Properties
    ----------
    gk_average
        Calculates goal keeper skills average
    defense_average
        Calculates defensive players skills average
    attacking_average
        Calculates defensive players skills average
    overall
        Calculates full players skills average
    """

    def __init__(self, position: str, positioning: int, reflexes: int,
                 diving: int, standing_tackle: int, physical: int, passing: int,
                 dribbling: int, long_shot: int, finishing: int) -> None:
        
        self.__position = position
        self.__positioning = positioning 
        self.__reflexes = reflexes
        self.__diving = diving
        self.__standing_tackle = standing_tackle
        self.__physical = physical
        self.__passing = passing 
        self.__dribbling = dribbling
        self.__long_shot = long_shot
        self.__finishing = finishing

    def show_habilities(self) -> dict:
        """Show all the habilities
        """
        return {
            "position": self.__position,
            "positioning": self.__positioning,
            "reflexes": self.__reflexes,
            "diving": self.__diving,
            "standing_tackle": self.__standing_tackle,
            "physical": self.__physical,
            "passing": self.__passing,
            "dribbling": self.__dribbling,
            "long_shot": self.__long_shot,
            "finishing": self.__finishing,
        }
    
    def evolve(self, factor: float) -> None:
        """This value hast to be higher and lower than 1 and -1.
        So factor > 1 and factor < -1.
        """

        if -1 <= factor <= 1:
            raise ValueError('The value {} is not acceptable, try again!'.format(factor))
        
        val =  round((factor * 0.98)) - (factor // (self.overall * 0.25)) 
        
        if val > 0:
            val += 1

        self.upgrade_habilties(val)
        
        return None

    def upgrade_habilties(self, value: int) -> None:
        """Upgrade player habilities

        Paramters
        ---------
        value : int
            A value that will increase or decrease the habilities points
        
        Returns
        -------
            None
        """

        # TODO
        # only upgrades if the value is lower than 100

        if self.__position == 'GK':
            self.__positioning += value
            self.__reflexes += value
            self.__diving += value
            
            return None 

        if self.defense_overall > self.attacking_overall:
            # upgrade defense players
            self.__standing_tackle += value
            self.__physical += value
            self.__passing += value
            
            return None 
        
        # update attacking players 
        self.__dribbling += value 
        self.__long_shot += value
        self.__finishing += value

    @property
    def gk_average(self) -> int:
        """Calculates the goal keeper average
        
        Returns
        -------
            Average of position, reflexes & diving
        """

        return (self.__positioning + self.__reflexes + self.__diving) // 3
    
    @property
    def defense_overall(self) -> int:
        """Calculates the defensive players average
        
        Returns
        -------
            Average of stading_tackle, physical & passing
        """

        return (self.__standing_tackle + self.__physical + self.__passing) // 3

    @property
    def attacking_overall(self) -> int:
        """Calculates the attacking players average

        Returns
        -------
            Average of driblling, long_shot & finishing
        """
        
        return (self.__dribbling + self.__long_shot + self.__finishing) // 3

    @property
    def overall(self) -> int:
        """Calculates the full skill players average
        
        Returns
        -------
        int : gk_average if is a goalkeeper or the full average if it's not a goalkeeper. 
        """
        
        if self.__position == 'GK':
            return int(self.gk_average)
        
        if self.defense_overall > self.attacking_overall:
            over = self.defense_overall * 2 + self.attacking_overall
        else:
            over = self.attacking_overall * 2 + self.defense_overall

        return int(over // 3)