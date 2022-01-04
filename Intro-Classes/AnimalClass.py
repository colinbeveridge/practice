class Animal:
    '''Animal Class'''
    def __init__(self,name,species,family,genus,age=None):
        self._name = name
        self._species = species
        self._family = family
        self._genus = genus
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self,species):
        self._species = species

    @property
    def family(self):
        return self._family
    
    @family.setter
    def family(self,family):
        self._family = family

    @property
    def genus(self):
        return self._genus
    
    @genus.setter
    def genus(self,genus):
        self._genus = genus
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        self._age = age
    
    def move(self):
        print('Moving')

    def eat(self):
        print('Eating')
    
    def play(self):
        print('Playing')

if __name__ == '__main__':
    zebra1 = Animal('Bob','Zebra','Horses','Equus',25)
    zebra2 = Animal('Tom','Zebra','Horses','Equus',18)
    lion1 = Animal('John','P. Leo','Felidae','Panthera',12)
    lion2 = Animal('Steve','P. Leo', family=None,genus='Panthera',age=20)
    print(lion2.genus)
    print(lion2.family)
    cat = Animal('Meowth')