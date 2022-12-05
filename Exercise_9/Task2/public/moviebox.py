#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.movie import Movie

class MovieBox:

    def __init__(self, title, movies):
        if not title or not movies:
            raise Warning("Please do not provide an empty movie list or title")
        for m in movies: 
            if not isinstance(m, Movie): 
                raise Warning("Faulty movie provided")
        self.__title = title
        self.__movies = movies

    def __repr__(self):
        out = f'MovieBox("{self.get_title()}", {self.get_movies()})'
        return out.replace("'", "\"")

    def __eq__(self, other):
        if self.get_title() == other.get_title() and self.get_movies() == other.get_movies():
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.get_title(), tuple(self.get_movies()))) 

    def get_title(self):
        return self.__title

    def get_actors(self):
        actors = []
        for m in self.__movies:
            actors.extend(m.get_actors())
        out = sorted(set(actors))
        return out

    def get_duration(self):
        duration = 0
        for m in self.__movies:
            duration += m.get_duration()
        return duration

    def get_movies(self):
        return self.__movies.copy()
