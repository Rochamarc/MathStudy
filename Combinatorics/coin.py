

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
    def value(self) -> any:
        """Return coin value based on the side"""
        
        if self.__side == 'A':
            return str(self.__value_a)
        return str(self.__value_b)
    

if __name__ == "__main__":
    from random import randint

    # coin = Coin(1, 2)
    # print(coin)
    # coin.flip()
    # print(coin.value)
    # coin.flip()
    # print(coin.value)

    # lançando 
    coin = Coin('Heads', 'Tails')
    print(coin)
    coin.flip()
    print(coin)


    for _ in range(randint(2,1000)):
        coin.flip()

    print(coin)