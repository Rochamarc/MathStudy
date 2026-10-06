from random import choice
import string
from time import sleep

options = string.ascii_uppercase + string.digits


class CustomHash:

    def __init__(self, hash_length: int, group: int) -> None:
        self._hash = self.generate_hash(hash_length)
        self.group = group

    @property
    def hash(self):
        return self._hash

    def __str__(self):
        if self.group:
            return ''.join([ '-' + self._hash[it] if ((it > 0) and (it % self.group == 0)) else self._hash[it] for it in range(len(self._hash)) ])
        return self._hash
    

    def generate_hash(self, hash_length: int):
        """
        """

        options = string.ascii_uppercase + string.digits
        return ''.join([ choice(options) for _ in range(hash_length)])


def generate_hash() -> str:
    """
    """
    key = ''

    for it in range(14):
        key += choice(options)
        if it == 3 or it == 7:
            key += '-'
    
    return key

def generate_simple_hash(length: int) -> str:
    """
    """
    key = ''

    for _ in range(length):
        key += choice(options)

    return key

def generate_hashes(length: int, groups: int) -> list[str]:
    """
    """
    
    key = []
    for i in range(length):
        pass

    return None

if __name__ == "__main__":

    c_hash = CustomHash(10,3)
    print(c_hash.hash)
    print(c_hash)

