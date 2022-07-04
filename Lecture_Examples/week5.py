# Example 1
# Receives a list of numbers as an argument
# and returns the index of the minimum value and the actual minimum
# value as a Tuple. Return None for an empty list.

def example1(list):
    if not list:
        return None
    min_index = 0
    for i in range(len(list)):
        if(list[i] < list[min_index]):
            min_index = i
    return (min_index, list[min_index])

# print(example1([])) # None
# print(example1([1])) # (0, 1)
# print(example1([2, 3, -1, 5, 2])) # (2, -1)
# print(example1([-1, 2, 3, 4])) # (0, -1)
# print(example1([10, 2, 4, -1])) # (3, -1)

# Example 2
# Receives a list of Tuples in the form: (<Actor>, <Movie>, <Year>). 
# Returns two Dictionaries in a Tuple. Dict1{Actor: Movie}, Dict2{Year: Movies}
def example2(list):
    dict1 = {}
    dict2 = {}
    for t in list:
        if not t[0] in dict1:
            dict1[t[0]] = [t[1]]
        else:
            dict1[t[0]].append(t[1])

        if not t[2] in dict2:
            dict2[t[2]] = [t[1]]
        else:
            if not t[1] in dict2[t[2]]:
                dict2[t[2]].append(t[1])
    return (dict1, dict2)


entertainment = [("Robert De Niro", "Goodfellas", 1990), ("Robert De Niro", "The Godfather", 1972), ("Robert De Niro", "The Irishman", 2019), 
                ("Al Pacino", "The Godfather", 1972), ("Al Pacino", "Scarface", 1983), ("Al Pacino", "The Irishman", 2019), 
                ("Leonardo DiCaprio", "The Wolf of Wall Street", 2013), ("Leonardo DiCaprio", "Titanic", 1997), ("Leonardo DiCaprio", "Django Unchained", 2012), 
                ("Joaquin Phoenix", "Joker", 2019), ("Joaquin Phoenix", "Gladiator", 2000), ("Joaquin Phoenix", "Her", 2013),  
                ("Heath Ledger", "BrokebackMountain", 2005), 
                ("Russell Crowe", "Les Misérables", 2012), ("Russell Crowe", "Gladiator", 2000), ("Russell Crowe", "Man Of Steel", 2013),  
                ("Christian Bale", "The Dark Knight", 2008), ("Christian Bale", "American Psycho", 2000), ("Christian Bale", "Batman Begins", 2005), 
                ("George Clooney", "Michael Clayton", 2007), ("George Clooney", "Ocean's Eleven", 2001)]
a, b = example2(entertainment) 
print(f"{a}\n\n{b}")
