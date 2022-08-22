class NumericalSet:
    def __init__(self, *values):
        self.set = sorted(list(dict.fromkeys(values))) # remove duplicates and sort items in that order
        
    def unity(self, other_set):
        ''' Returns another NumericalSet with the unity of this set with the other set '''
        return NumericalSet(*(self.set + other_set.set))

    def inter(self, other_set):
        ''' Returns another NumericalSet with the intersection of the other set with this one '''
        return NumericalSet(*[ i for i in self.set if i in other_set.set ])

    def belongs_to(self, value):
        ''' Return True if the value belongs to this set'''
        return value in self.set

    def dont_belongs_to(self, value):
        ''' Return True if the value dont belongs to this set '''
        return value not in self.set 

    def is_contained(self, other_set):
        ''' Return True if the other set is contained in this set'''
        return other_set.set in self.set 

    def is_not_contained(self, other_set):
        ''' Return True if the other set is not contained in this set'''
        return other_set.set not in self.set

    def additional(self, other_set):
        ''' Returns another NumericalSet with the additional of other set '''
        return NumericalSet(*[ i for i in self.set if not i in other_set.set ]) 

    def __str__(self):
        s = str(self.set).replace('[', '').replace(']', '')
        return '{' + s + '}' 

    def __eq__(self, other_set):
        return self.set == other_set.set 

    def __sub__(self, other_set):
        return NumericalSet(*[ i for i in self.set if not i in other_set.set ]) 

    def __len__(self):
        return len(self.set)


if __name__ == "__main__":
    a = NumericalSet(1,2,3,4,5,6)
    b = NumericalSet(5,6,8,9)
    print(a - b)
    
    print(len(a))