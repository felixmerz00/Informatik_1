#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):
        # Input validation
        if not title or not actors:
             raise Warning("This bitch empty. Invalid: Either the title or the actors list was empty.")
        if duration < 1: 
            raise Warning("Size matters ;)")
        # Create instance variables
        self.__title = title
        self.__actors = actors
        self.__duration = duration

    def __repr__(self):
        out = f'Movie("{self.get_title()}", {self.get_actors()}, {self.__duration})'
        return out.replace("'", "\"") # Replace ' with "

    def __eq__(self, other):
        if self.get_title() == other.get_title() and self.get_actors() == other.get_actors() and self.get_duration() == other.get_duration():
            return True
        else:
            return False
    
    def __hash__(self):
        return hash((self.__title, tuple(self.get_actors()), self.__duration))

    def get_title(self):
        return self.__title

    def get_actors(self):
        return self.__actors.copy()

    def get_duration(self):
        return self.__duration
