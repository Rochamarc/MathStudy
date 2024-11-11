

class Coin():
    def __init__(self, value_a: any, value_b: any):
        self.__side = 'A'
        self.__value_a = value_a
        self.__value_b = value_b

    def flip(self) -> None:
        """Change the side of the coin
        """

        if self.__side == 'A':
            self.__side = 'B'
            return None
        
        self.__side = 'A'
    
    @property
    def value(self):
        """Return coin value based on the side"""
        
        if self.__side == 'A':
            return self.__value_a
        return self.__value_b
    

if __name__ == "__main__":
    coin = Coin(1, 2)
    print(coin.value)
    coin.flip()
    print(coin.value)
    coin.flip()
    print(coin.value)
