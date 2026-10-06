#
#
#

class MakeRelation():
    def __init__(self, name: str, starter_set: list[any]) -> None:
        self.name = name 
        self.relations = None 
        self.starter_set = starter_set
    
    def reflexive(self) -> list[list]: 
        return [ [i,y] for i in self.starter_set for y in self.starter_set if i != y ]

class Relation:
    def __init__(self, name: str, relations: list[list]) -> None:
        self.name = name
        self.relations = relations 
        self.__reflexive_relations = [ [i,i] for i in self.domain ]
        self.__symmetrical_relations = [ [i,y] for i in self.domain for y in self.domain if i != y ]

    def __repr__(self) -> str:
        return f"{self.relations}" 

    @property
    def domain(self) -> set[int]:
        """
        """
        return set([ relation[0] for relation in self.relations ])

    @property
    def image(self) -> set[int]:
        """
        """
        return set([ relation[-1] for relation in self.relations ])
    
    @property
    def reverse(self) -> list[list]:
        """
        """
        return [ [relation[-1], relation[0]] for relation in self.relations ]
    
    def reflexive(self) -> bool:
        """For each element in the domain and image the element will relate to itself

        Returns
        -------
        bool : For the number of reflexive occurrences to be equal to the number of possible reflexive relations
        """
        n = 0

        for i in self.relations:
            if i in self.__reflexive_relations: 
                n += 1
        return n == len(self.__reflexive_relations)

    def anti_reflexive(self) -> bool:
        """For each element in the domain and image the element will not relate to itself
        
        Returns
        -------
        bool : For zero occurrences in the possibilities of reflexive relationships
        """
        n = 0

        for i in self.relations:
            if i in self.__reflexive_relations:
                n += 1
        return n == 0

    def symmetrical(self) -> bool:
        """For each element in the domain that is different from its image, it must relate to its opposite

        Returns
        -------
        bool : For the number of symmetrical occurrences to be equal to the number of possible symmetrical relations
        """
        n = 0

        for i in self.relations:
            if i in self.__symmetrical_relations:
                n += 1
        return n == len(self.__symmetrical_relations)

    def anti_symmetrical(self) -> bool:
        """For each element in the domain and image apply the follow rule:
            xRy and yRx -> x == y\n
            x != y -> not xRy or not yRx

        Returns
        -------
        bool : For the number of non-symmetric occurrences to be equal to the number of elements in the relations
        """
        n = 0

        for i in self.relations:
            x, y = i[0], i[-1]

            if x != y:
                reverse_relation = i[::-1]

                if not reverse_relation in self.relations:
                    n += 1
            else:
                n += 1

        return n == len(self.relations)
    
    def transitive(self) -> bool:
        """For each x, y and z in the relations xRy and yRz -> xRz

        Returns
        -------
        bool : 
        """
        
        n = 0

        for rel in self.relations:
            x, y = rel[0], rel[-1]

            if x == y:
                n += 1
                break
            else:
                for rel_2 in self.relations:
                    ...




if __name__ == "__main__":
    # rel = [[1,1], [2,2], [2,1]]
    # R = Relation('R', rel)
    # print(f"R: {R}")
    # print(f"D(R): {R.domain}")
    # print(f"Im(R): {R.image}")
    # print(f"R⁻¹: {R.reverse}")
    # print(f"R is reflexive? {R.reflexive()}")
    # print(f"R is anti reflexive? {R.anti_reflexive()}")
    # print(f"R is symmetrical? {R.symmetrical()}")
    # print(f"R is anti symmetrical? {R.anti_symmetrical()}")

    a = [1,2,3]
    b = MakeRelation('R', a)
    print(b.reflexive())