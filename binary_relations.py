class Relation():
    def __init__(self, x: any, y: any) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x},{self.y})"
    
    def invert(self) -> object:
        return Relation(self.y, self.x)
    
    @property
    def equal(self) -> bool:
        """Returns if the x and y value are equal
        """
        return self.x == self.y
    
    def __eq__(self, other_relation: object) -> bool:
        """Checks if the x and y of another relation are equal
        """
        return (other_relation.x == self.x) and (other_relation.y == self.y)

class BinaryRelation():
    def __init__(self, set_group: list[any], relations: list[Relation]) -> None:
        self.set = set_group
        self.relations = relations
        self.__occurrences = [ Relation(a,a) for a in self.set ]
        self.__against_occurrences = [ i.invert() for i in self.relations if not i.equal ]

    def __repr__(self) -> str:
        return f"{self.relations}"
    
    def reflective(self) -> bool:
        """To be true all elements in the self.relations have to relate to himself
        """
        return self.__occurrences == self.equal_occurrences
    
    def anti_reflective(self) -> bool:
        """To be true all elements in the self.relations can't relate to himself
        """
        return len(self.equal_occurrences) == 0

    def symmetrical(self) -> bool:
        """To be true, all elements x different from y in the relations must contain 
        an inverse relationship
        """
        against = [ i for i in self.relations if not i.equal ]
        
        for rel in enumerate(against):
            it = rel[0]
            relation = rel[-1]
    

    @property
    def equal_occurrences(self) -> bool:
        return [ rel for rel in self.relations if rel.equal ]

if __name__ == "__main__":
    # Define a general set
    a = [1, 2, 3]
    r = [ Relation(x,y) for x in a for y in a ]

    R = BinaryRelation(a, r)
    print(R)
    print(R.reflective())
    print(R.anti_reflective())
    print(R.symmetrical())

    print('\n')
    
    S = BinaryRelation(a, [Relation(1,2), Relation(2,1), Relation(2,2)])
    print(S)
    print(S.reflective())
    print(S.anti_reflective())
    print(S.symmetrical())

    print('\n')

    T = BinaryRelation(a, [Relation(1,2), Relation(2,1), Relation(3,2)])
    print(T)
    print(T.reflective())
    print(T.anti_reflective())
    print(T.symmetrical())
