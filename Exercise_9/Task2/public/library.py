#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.movie import Movie
from public.moviebox import MovieBox

class Library(MovieBox):

    # Create private variables 
    def __init__(self):
        self.__movies = []

    def add_movie(self, movie):
        if not movie in self.__movies: 
            self.__movies.append(movie)

    def get_movies(self):
        movie_dict = {}
        out = []
        for m in self.__movies:
            if isinstance(m, MovieBox): 
                for e in m.get_movies():
                    movie_dict[e.get_title()] = e
            else: movie_dict[m.get_title()] = m

        for key in sorted(movie_dict):
            out.append(movie_dict[key])
        return out

    def get_total_duration(self):
        total_duration = 0
        for movie in self.__movies:
            total_duration += movie.get_duration()
        return total_duration
