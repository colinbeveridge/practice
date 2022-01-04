# this code creates a class called astronaut
import csv

class Astronaut:
    '''Astronaut Class
        Name, Flight (hr) and Status are required fields and all others are optional from CSV read
    
    '''
    def __init__(self,Name,FlightTime,Status,BirthDate,BirthPlace,Branch):
        self._Name = Name
        self._FlightTime = FlightTime
        self._Status = Status
        self._BirthDate = BirthDate
        self._BirthPlace = BirthPlace
        self._Branch = Branch
    
    def __str__(self):
        return f'{self._Name}, {self._Status}'

    def __gt__(self,other):
        print('__gt__ called')
        return self._FlightTime > other._FlightTime

    def __ge__(self,other):
        print('__ge__ called')
        return self._FlightTime >= other._FlightTime

    def __eq__(self,other):
        print('__eq__ called')
        return self._FlightTime == other._FlightTime
 
    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self,Name):
        self._Name = Name

    @property
    def FlightTime(self):
        return self._FlightTime

    @FlightTime.setter
    def FlightTime(self,FlightTime):
        self._FlightTime = FlightTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self,Status):
        self._Status = Status

    @property
    def BirthDate(self):
        return self._BirthDate

    @BirthDate.setter
    def BirthDate(self,BirthDate):
        self._BirthDate = BirthDate

    @property
    def BirthPlace(self):
        return self._BirthPlace

    @BirthPlace.setter
    def BirthPlace(self,BirthPlace):
        self._BirthPlace = BirthPlace

    @property
    def Branch(self):
        return self._Branch

    @BirthDate.setter
    def Branch(self,Branch):
        self._Branch = Branch

def make_dictionaries_from_csv(csvfile):
    with open(csvfile,'r',encoding='utf-8-sig') as inp:
        reader = csv.DictReader(inp)
        readerlist = list(reader)
        dictlist = []
        # now we have a list object to be converted to dictionaries
        for row in readerlist:
            # finaldict is one dictionary from one row of readerlist
            finaldict = dict(row)
            dictlist.append(dict(row))
    return dictlist



if __name__ == '__main__':
    dictlist = make_dictionaries_from_csv('astronauts.csv')
    numastronauts = len(dictlist)
    astronautlist = []
    fieldlist = list(dictlist[0].keys())
    print(fieldlist)
    # now loop through dictlist and assign each dictionary elements to an astronaut object
    for astrodict in dictlist:
        astronaut = Astronaut(astrodict[fieldlist[0]],astrodict[fieldlist[13]],astrodict[fieldlist[3]],astrodict[fieldlist[4]],astrodict[fieldlist[5]],astrodict[fieldlist[11]])
        astronautlist.append(astronaut)

    print(astronautlist)
    # all 6 properties created should be mutable, made getters and setters for all of them.
    print(astronautlist[10]<=astronautlist[14])
    print(astronautlist[25])

