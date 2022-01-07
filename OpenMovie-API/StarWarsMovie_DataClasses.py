import dataclasses as dc
import datetime
import typing
@dc.dataclass
class StarWarsFilm:
    # from SW API
    episode_id: int
    title: str = dc.field(default=None)
    opening_crawl: str = dc.field(default=None)
    director: str = dc.field(default=None)
    producer: str = dc.field(default=None)
    release_date: int = dc.field(default=None)
    characters: list = dc.field(default=None)
    # from OMDB API
    plot: str = dc.field(default=None)
    RottenTomatoes_rating: int = dc.field(default=None)
    BoxOffice_gross: int = dc.field(default=0,metadata={'units':'U.S. dollars'})

    def __gt__(self,other):
        return self.episode_id > other.episode_id

    def __ge__(self,other):
        return self.episode_id >= other.episode_id

    def __eq__(self,other):
        return self.episode_id == other.episode_id

@dc.dataclass
class StarWarsCharacter:
    # star wars character class, all from SW API
    name: str
    height: int = dc.field(default=0,metadata={'units':'centimeters'})
    weight: int = dc.field(default=0,metadata={'units':'kilograms'})

    def __str__(self):
        return str(self.__dict__)

@dc.dataclass
class MovieLibrary:
    Movielist: list
    Showlist: list
    LastUpdated: datetime.date


    def sort(self):




if __name__ == '__main__':
    # ep4 = StarWarsFilm(4,'stuf','other stuff')
    # if ep4.director == None:
    #     print('diretor is none')
    # print(ep4.__dict__)
    luke = StarWarsCharacter('luke')
    print(luke)
